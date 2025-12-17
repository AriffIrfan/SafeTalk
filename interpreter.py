import sys
from grammar_safetalkVisitor import grammar_safetalkVisitor
from grammar_safetalkParser import grammar_safetalkParser

class SafeTalkInterpreter(grammar_safetalkVisitor):
    def __init__(self):
        # 1. MEMORY (Symbol Table)
        self.memory = {}
        # Pre-set system attributes for testing
        self.memory['size'] = 100  
        self.memory['date'] = 2024
        self.history = [] # For 'explain' command

    # --- 2. ASSIGNMENT ---
    def visitAssignment(self, ctx):
        var_name = ctx.ID().getText()
        value = self.visit(ctx.expression())
        
        self.memory[var_name] = value
        self.history.append(f"Set '{var_name}' to {value}")
        print(f"[ACTION] Assigned variable '{var_name}' = {value}")
        return value

    # --- 3. ARITHMETIC ---
    def visitExpression(self, ctx):
        result = self.visit(ctx.term(0))
        for i in range(1, len(ctx.term())):
            right = self.visit(ctx.term(i))
            operator = ctx.getChild(2 * i - 1).getText()

            if operator == '+': result += right
            elif operator == '-': result -= right
        return result

    def visitTerm(self, ctx):
        result = self.visit(ctx.factor(0))
        for i in range(1, len(ctx.factor())):
            right = self.visit(ctx.factor(i))
            operator = ctx.getChild(2 * i - 1).getText()

            if operator == '*': 
                result *= right
            elif operator == '/':
                # ERROR HANDLING: Division by Zero
                if right == 0:
                    print(f"❌ [RUNTIME ERROR] Division by zero detected!")
                    return 0
                result /= right
            elif operator == '%':
                result %= right
        return result

    def visitFactor(self, ctx):
        if ctx.NUMBER():
            return int(ctx.NUMBER().getText())
        elif ctx.ID():
            var_name = ctx.ID().getText()
            if var_name in self.memory:
                return self.memory[var_name]
            else:
                # ERROR HANDLING: Undefined Variable
                print(f"❌ [RUNTIME ERROR] Variable '{var_name}' is not defined.")
                return 0
        elif ctx.attribute():
            attr_name = ctx.attribute().getText()
            return self.memory.get(attr_name, 0)
        elif ctx.expression():
            return self.visit(ctx.expression())

    # --- 4. CONDITIONAL LOGIC ---
    def visitConditional(self, ctx):
        condition_result = self.visit(ctx.logic_expr())
        
        if condition_result:
            print("[LOGIC] Condition is TRUE. Executing 'THEN' block...")
            return self.visit(ctx.statement(0))
        elif len(ctx.statement()) > 1:
            print("[LOGIC] Condition is FALSE. Executing 'ELSE' block...")
            return self.visit(ctx.statement(1))
        else:
            print("[LOGIC] Condition is FALSE. Skipping.")
            return None

    def visitLogic_expr(self, ctx):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        op = ctx.comparator().getText()

        if op == '>': return left > right
        if op == '<': return left < right
        if op == '==': return left == right
        # ... (add other operators if needed)
        return False

    # --- 5. COMMANDS & SAFETY ---
    def visitCommand(self, ctx):
        verb = ctx.verb().getText()
        # FIXED: .object_() because 'object' is reserved in Python
        obj = ctx.object_().getText() 
        
        # EXPLAINABILITY LOG
        self.history.append(f"Executed command: {verb} {obj}")

        # SAFETY CHECK (The "SafeTalk" Feature)
        if verb == "delete":
            # Mocking a count of files > 5
            file_count = 10 
            if file_count > 5:
                print(f"⚠️ [SAFETY WARNING] You are about to delete {file_count} files.")
                print(f"   (In a real app, we would ask for confirmation here)")
            print(f"🚀 EXECUTING: {verb.upper()} on {obj.upper()}")
        
        else:
            print(f"🚀 EXECUTING: {verb.upper()} on {obj.upper()}")
        
        if ctx.condition_cl():
            self.visit(ctx.condition_cl())

    # --- 6. EXPLAINABILITY ---
    def visitExplain_cmd(self, ctx):
        print(f"\n🧠 [EXPLAIN] Trace of last action:")
        if self.history:
            print(f"   -> {self.history[-1]}")
        else:
            print(f"   -> No actions recorded yet.")

    def visitAmbiguous_term(self, ctx):
        term = ctx.getText()
        print(f"\n⚡ [PARADIGM TRIGGER] Ambiguous term: '{term}' detected.")
        print(f"   -> Interpreter paused. Calling LLM for definition...")
        return term