import sys
import google.generativeai as genai
from grammar_safetalkVisitor import grammar_safetalkVisitor
from antlr4.error.ErrorListener import ErrorListener

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
            var_name = ctx.ID().getText()
            
            # 1. CHECK MEMORY (Is it a real variable?)
            if var_name in self.memory:
                return self.memory[var_name]

            # ---------------------------------------------------------
            # 🚀 NEW LOGIC: It's not a variable. Is it a SYNONYM?
            # ---------------------------------------------------------
            
            # Step A: Ask AI to map it to a grammar term
            mapped_term = self.match_grammar_term(var_name)
            
            if mapped_term:
                # Step B: If mapped (e.g. 'small' -> 'tiny'), resolve 'tiny'
                # We reuse the resolve_ambiguity function we wrote earlier!
                context = getattr(self, 'current_context', 'general')
                return self.resolve_ambiguity(mapped_term, context)
            
            # ---------------------------------------------------------
            # 🛑 FALLBACK: If AI says "NO", then it's a true Error.
            # ---------------------------------------------------------
            
            error_msg = f"⚠️ ERROR: The variable '{var_name}' has not been defined yet."
            print(error_msg)
            self.history.append(error_msg)
            return None 

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
    
    # --- ADD THIS METHOD TO interpreter.py ---
    def visitExplain_cmd(self, ctx):
        print("🤖 [EXPLAIN TRIGGERED] Generating explanation...")
        
        # 1. Check if we have history
        if not self.history:
            return "No previous commands to explain."

        # 2. Get the last action
        # If the user asks for 'history', show all; if 'last', show the specific last one.
        target = ctx.getChild(1).getText() # Gets 'last' or 'history'
        
        if target == 'last':
            last_action = self.history[-1]
            explanation = f"📝 EXPLANATION: The system executed '{last_action}'."
            
            # (Optional) Ask LLM to justify it for the "SafeTalk" requirement
            if self.model:
                 # Minimal prompt to save quota
                prompt = f"Explain clearly to a non-technical user why a file system would perform this action: '{last_action}'. Keep it under 20 words."
                try:
                    ai_reason = self.model.generate_content(prompt).text.strip()
                    explanation += f"\n   Reasoning: {ai_reason}"
                except:
                    pass
            
            print(explanation)
            return explanation
            
        elif target == 'history':
            return "\n".join([f"{i+1}. {cmd}" for i, cmd in enumerate(self.history)])
        
    # --- NEW HELPER: Synonym Matcher ---
    def match_grammar_term(self, unknown_term):
        """
        Ask GenAI if 'unknown_term' is a synonym for one of our strict grammar keywords.
        Returns the STRICT keyword (e.g., 'tiny') or None.
        """
        # Strict list from your grammar
        valid_terms = ['recent', 'old', 'huge', 'tiny', 'important']
        
        # 1. OPTIONAL: Mock Mode for fast testing
        # if unknown_term == 'small': return 'tiny'

        if not self.model:
            return None

        print(f"🕵️ [AI CHECK] Is '{unknown_term}' a synonym for a known grammar term?")
        
        try:
            prompt = (
                f"I have a strict list of valid system keywords: {valid_terms}. "
                f"The user input the unknown term '{unknown_term}'. "
                f"Is '{unknown_term}' a synonym for any word in my list? "
                f"If yes, return ONLY the exact word from the list. "
                f"If no, return 'NO'."
            )
            
            response = self.model.generate_content(prompt)
            result = response.text.strip().lower()
            
            # Clean up response (remove punctuation/quotes AI might add)
            result = result.replace("'", "").replace('"', "").replace(".", "")

            if result in valid_terms:
                print(f"   -> ✅ MATCH FOUND: '{unknown_term}' mapped to '{result}'")
                return result
            else:
                print(f"   -> ❌ NO MATCH. Treating as undefined variable.")
                return None

        except Exception as e:
            print(f"   -> AI Error: {e}")
            return None
        
class SafeTalkErrorListener(ErrorListener):
    def __init__(self):
        super(SafeTalkErrorListener, self).__init__()
        self.errors = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        """
        Custom Error Handler that manually decodes token names to avoid crashes.
        """
        bad_token = offendingSymbol.text if offendingSymbol else "unknown"
        
        # --- 1. ROBUSTLY GET EXPECTED TOKENS ---
        # Instead of relying on 'vocabulary', we use the list of names directly.
        expected_tokens_list = []
        try:
            if e:
                # Get the IDs of the tokens the parser wanted (e.g., [4, 5, 6])
                interval_set = e.getExpectedTokens()
                
                # Get the human-readable names from the parser (e.g., ['VERB', 'OBJECT', ...])
                # We prioritize literal names (like 'find') over symbolic names (like 'VERB')
                token_names = recognizer.literalNames
                symbolic_names = recognizer.symbolicNames
                
                for i in interval_set.intervals:
                    # Intervals can be ranges, but usually they are single tokens
                    for token_id in range(i.start, i.stop):
                        if 0 <= token_id < len(token_names):
                            # Try to get 'find' (literal), if None, get 'VERB' (symbolic)
                            name = token_names[token_id] or symbolic_names[token_id]
                            # Clean up quotes (ANTLR returns "'find'")
                            if name:
                                expected_tokens_list.append(name.replace("'", ""))
            
            expected_str = ", ".join(expected_tokens_list)
        except Exception:
            expected_str = "command components"

        # --- 2. CONTEXT-AWARE TIPS ---
        error_message = f"⚠️ GRAMMAR ERROR at '{bad_token}': "
        tip = ""

        # Case A: Wrong Start
        if column == 0:
            error_message += "I don't know this command."
            tip = "Start with a verb like: 'find', 'list', 'sort', 'set', 'if', 'explain'."

        # Case B: Structure violation (General Mismatch)
        elif "mismatched input" in msg:
            if "comparator" in expected_str or ">" in expected_str:
                error_message += "I was expecting a comparison here."
                tip = "Try adding '>', '<', or '==' between the values."
            elif "ID" in expected_str or "attribute" in expected_str:
                error_message += "I was expecting a variable or attribute."
                tip = f"Instead of '{bad_token}', try 'size', 'date', or a variable name."
            elif "verb" in expected_str: # If symbolic name VERB is found
                error_message += "I expected a command verb."
                tip = "Valid verbs: find, delete, sort, calculate."
            elif "object" in expected_str: # If symbolic name OBJECT is found
                error_message += "I expected a target object."
                tip = "Valid objects: files, images, documents, items."
            else:
                error_message += f"Unexpected word '{bad_token}'."
                # Show the manual list we built above
                tip = f"I was expecting one of these: {expected_str}"

        # Case C: Missing Component
        elif "missing" in msg:
            if "attribute" in msg or "ID" in msg:
                error_message += "Incomplete command."
                tip = "Tell me what to sort or filter by (e.g., 'size', 'date')."
            elif "expression" in msg or "value" in msg:
                error_message += "Missing value."
                tip = "Please provide a number or variable."
            else:
                error_message += f"Missing component: {msg}"
                tip = f"Try adding: {expected_str}"
        
        # Case D: Extra words
        elif "extraneous input" in msg:
             error_message += f"I don't understand '{bad_token}' here."
             tip = "Try removing this word."

        # Fallback
        else:
            error_message += msg
            tip = "Check the command structure."

        # Combine and Save
        final_msg = f"{error_message}\n   -> 💡 Tip: {tip}"
        
        if final_msg not in self.errors:
            self.errors.append(final_msg)

def run_safetalk_command(user_input):
    # 1. Setup Stream
    input_stream = InputStream(user_input)
    lexer = SafeTalkLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = SafeTalkParser(stream)
    
    # ---------------------------------------------------------
    # 🛡️ ATTACH THE CUSTOM ERROR LISTENER
    # ---------------------------------------------------------
    # Remove the default "ConsoleErrorListener" (which prints ugly red text)
    parser.removeErrorListeners()
    
    # Add our custom SafeTalk listener
    error_handler = SafeTalkErrorListener()
    parser.addErrorListener(error_handler)
    
    # 2. Parse the Command
    tree = parser.program()
    
    # 3. Check for Errors BEFORE executing
    if error_handler.errors:
        print("\n❌ Command Aborted due to Grammar Violation.")
        # We stop here so the interpreter doesn't crash trying to run broken code
        return "Grammar Check Failed"

    # 4. If No Errors, Execute
    interpreter = SafeTalkInterpreter()
    interpreter.visit(tree)
    return "Success"