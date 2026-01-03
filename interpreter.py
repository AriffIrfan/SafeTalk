import sys
import google.generativeai as genai
from grammar_safetalkVisitor import grammar_safetalkVisitor

# --- CONFIGURATION ---
# 🔴 PASTE YOUR API KEY HERE 🔴
# Try to import the key, handle error if missing
try:
    from secrets_config import GOOGLE_API_KEY
except ImportError:
    GOOGLE_API_KEY = "" # Fallback if file is missing
    print("⚠️ Warning: secrets_config.py not found.")

class SafeTalkInterpreter(grammar_safetalkVisitor):
    def __init__(self):
        self.memory = {'size': 100, 'date': 2024} # Mock file attributes
        self.history = []
        
        # Configure the AI
        if not GOOGLE_API_KEY:
            print("⚠️ WARNING: No API Key found. LLM features will be disabled.")
        else:
            genai.configure(api_key=GOOGLE_API_KEY)
            self.model = genai.GenerativeModel('gemini-2.5-flash')

    # --- HELPER: The "Exception Handler" Logic ---
    def resolve_ambiguity(self, term, context="size"):
        """
        This is the PARADIGM SHIFT. 
        Instead of crashing, we ask the AI to resolve the meaning.
        """
        print(f"\n🤖 [AI TRIGGER] Analyzing ambiguous term: '{term}'...")
        
        try:
            # 1. Construct the Prompt
            prompt = (
                f"I am a file system interpreter. The user used the ambiguous term '{term}' "
                f"in the context of '{context}'. "
                f"Give me a single numeric value (integer) that represents this threshold. "
                f"For example: 'huge' -> 1000000 (bytes). 'recent' -> 2024 (year). "
                f"Reply ONLY with the number."
            )
            
            # 2. Call Gemini
            response = self.model.generate_content(prompt)
            value = int(response.text.strip())
            
            print(f"✅ [AI RESOLVED] '{term}' interpreted as value: {value}")
            self.history.append(f"AI interpreted '{term}' as {value}")
            return value

        except Exception as e:
            print(f"❌ [AI FAILED] Could not connect: {e}")
            self.history.append(f"AI failed to interpret '{term}'")
            return 0 # Fallback value

    # --- VISITORS ---

    def visitAssignment(self, ctx):
        # 1. GET VARIABLE NAME (Fixes the crash for 'let size = ...')
        if ctx.ID():
            var_name = ctx.ID().getText()
        elif ctx.attribute():
            # This allows you to use reserved words like 'size' as variables
            var_name = ctx.attribute().getText() 
        else:
            # Fallback
            var_name = ctx.getChild(1).getText()

        # 2. CALCULATE VALUE
        value = self.visit(ctx.expression())
        
        # 3. SAVE TO MEMORY
        self.memory[var_name] = value
        
        # 4. SAVE TO HISTORY (Fixes the empty log!)
        log_entry = f"User assigned variable '{var_name}' to value {value}"
        self.history.append(log_entry)  # <--- THIS IS THE MISSING KEY
        
        print(f"[ACTION] {log_entry}")
        return value

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
            if operator == '*': result *= right
            elif operator == '/': result /= right
        return result

    def visitFactor(self, ctx):
        if ctx.NUMBER():
            return int(ctx.NUMBER().getText())
        elif ctx.ID():
            return self.memory.get(ctx.ID().getText(), 0)
        elif ctx.attribute():
            return self.memory.get(ctx.attribute().getText(), 0)
        elif ctx.expression():
            return self.visit(ctx.expression())

    def visitConditional(self, ctx):
        if self.visit(ctx.logic_expr()):
            print("[LOGIC] Condition TRUE.")
            self.visit(ctx.statement(0))
        elif len(ctx.statement()) > 1:
            print("[LOGIC] Condition FALSE. Executing Else.")
            self.visit(ctx.statement(1))

    def visitLogic_expr(self, ctx):
        # We need to know the 'Context' (e.g., is the left side 'size' or 'date'?)
        # This helps the LLM know if 'huge' means bytes or pixels.
        left_node = ctx.expression(0).term(0).factor(0)
        context = "general"
        if left_node.attribute():
            context = left_node.attribute().getText()

        # Execute Left and Right
        left = self.visit(ctx.expression(0))
        
        # SPECIAL HANDLING: The right side might be an Ambiguous Term
        # We pass the 'context' (like 'size') so the LLM knows what to do.
        right_expr_ctx = ctx.expression(1)
        # Check if the right side is an ambiguous term by peeking at the tree
        # (Simplified for prototype: we just evaluate it normally)
        
        # We temporarily store context for the child node to access
        self.current_context = context 
        right = self.visit(ctx.expression(1))
        
        op = ctx.comparator().getText()
        if op == '>': return left > right
        if op == '<': return left < right
        if op == '==': return left == right
        return False

    def visitAmbiguous_term(self, ctx):
        term = ctx.getText()
        # Retrieve the context (e.g., 'size') if we set it, otherwise default
        context = getattr(self, 'current_context', 'size')
        
        # 🚀 CALL THE LLM HERE
        resolved_value = self.resolve_ambiguity(term, context)
        return resolved_value

    def visitCommand(self, ctx):
        verb = ctx.verb().getText().upper()
        obj = ctx.object_().getText().upper()
        
        # 1. PRINT TO CONSOLE (For the Chat Bubble)
        msg = f"🚀 EXECUTING: {verb} on {obj}"
        print(msg)
        
        # 2. SAVE TO HISTORY (For the Sidebar & Explain command)
        self.history.append(f"User executed command: {verb} {obj}")

        # 3. HANDLE CONDITIONS (if they exist)
        if ctx.condition_cl():
            self.visit(ctx.condition_cl())
    
    def visitCondition_cl(self, ctx):
        # 1. GET ATTRIBUTE (e.g., 'size' or 'date')
        attr = ctx.attribute().getText()
        
        # Tell the visitor we are talking about 'size' (for the LLM)
        self.current_context = attr 
        
        # 2. GET VALUE (This triggers the LLM if it's 'huge')
        val = self.visit(ctx.value()) 
        
        # 3. PRINT & LOG
        log_msg = f"   -> Applied Filter: {attr} > {val}"
        print(log_msg)
        self.history.append(log_msg)

    def visitValue(self, ctx):
        if ctx.expression(): return self.visit(ctx.expression())
        if ctx.ambiguous_term(): return self.visit(ctx.ambiguous_term())
        return 0