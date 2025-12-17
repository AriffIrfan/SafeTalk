import sys
from antlr4 import *
from grammar_safetalkLexer import grammar_safetalkLexer
from grammar_safetalkParser import grammar_safetalkParser
from interpreter import SafeTalkInterpreter

def run_safetalk(interpreter, command):
    print(f"\n{'-'*60}")
    print(f"INPUT: \"{command}\"")
    
    # 1. Lexer & Parser Setup
    input_stream = InputStream(command)
    lexer = grammar_safetalkLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = grammar_safetalkParser(stream)
    
    # 2. Parse the Program
    tree = parser.program()
    
    # 3. Check for Syntax Errors (ANTLR handles this automatically)
    if parser.getNumberOfSyntaxErrors() > 0:
        print("❌ [SYNTAX ERROR] Your command grammar is invalid.")
        return

    # 4. Visit the tree (Run the code)
    interpreter.visit(tree)

def main():
    print("\n=======================================================")
    print("      SAFETALK INTERPRETER - MASTER TEST SUITE")
    print("=======================================================")
    
    # Create ONE interpreter to share memory across tests
    my_interpreter = SafeTalkInterpreter()
    
    # --- CASE 1: ARITHMETIC & ASSIGNMENT ---
    # We verify math works and variables are saved.
    run_safetalk(my_interpreter, "set limit to 10 + 5 * 2") 
    # Result should be 20.

    # --- CASE 2: CONDITIONAL (TRUE) ---
    # 'size' is 100 (default), 'limit' is 20. 100 > 20 is True.
    run_safetalk(my_interpreter, "if size > limit then list files")

    # --- CASE 3: CONDITIONAL (FALSE + ELSE) ---
    # 5 > 100 is False. Should trigger the 'else' block.
    run_safetalk(my_interpreter, "if 5 > 100 then delete files else archive documents")

    # --- CASE 4: USER ERROR (Undefined Variable) ---
    # 'ghost' was never defined. Should print a runtime error.
    run_safetalk(my_interpreter, "if ghost > 50 then delete files")

    # --- CASE 5: USER ERROR (Division by Zero) ---
    # Math rule violation. Should handle gracefully.
    run_safetalk(my_interpreter, "set danger to 100 / 0")

    # --- CASE 6: SAFETY CHECK (Project Title Feature) ---
    # 'delete' should trigger the mock safety warning.
    run_safetalk(my_interpreter, "delete files")

    # --- CASE 7: AMBIGUITY (Paradigm Trigger) ---
    # 'huge' is ambiguous. Should trigger the LLM placeholder.
    run_safetalk(my_interpreter, "find files where size > huge")

    # --- CASE 8: EXPLAINABILITY ---
    # Should show the history of the last command run.
    run_safetalk(my_interpreter, "explain last")

    print("\n=======================================================")
    print("                  TEST COMPLETE")
    print("=======================================================")

if __name__ == '__main__':
    main()