import sys
from antlr4 import *
# UPDATED IMPORTS to match your grammar filename
from grammar_safetalkLexer import grammar_safetalkLexer
from grammar_safetalkParser import grammar_safetalkParser

def run_test(test_name, input_command):
    print(f"\n{'='*60}")
    print(f"TEST: {test_name}")
    print(f"INPUT: \"{input_command}\"")
    print(f"{'='*60}")

    input_stream = InputStream(input_command)
    
    # UPDATED CLASS NAMES
    lexer = grammar_safetalkLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = grammar_safetalkParser(stream)
    
    # Build the Tree
    tree = parser.program()
    
    # Print the LISP-style tree
    print(f"PARSE TREE:\n{tree.toStringTree(recog=parser)}")

def main():
    print("SafeTalk Parser - Comprehensive Test Suite")
    
    # --- TEST 1: Basic Natural Language Command ---
    run_test("Basic Command", "delete files")

    # --- TEST 2: Conditional Logic ---
    run_test("Conditional Statement", "if size > 50 then archive documents")

    # --- TEST 3: Arithmetic & Order of Operations ---
    run_test("Arithmetic Precedence", "set limit to 10 + 5 * 2")

    # --- TEST 4: Ambiguity Detection (Paradigm) ---
    run_test("Ambiguity Detection", "find files where size > huge")

    # --- TEST 5: Explainability ---
    run_test("Explainability Request", "explain last")

if __name__ == '__main__':
    main()