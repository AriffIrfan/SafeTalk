from antlr4 import *
from grammar_safetalkLexer import grammar_safetalkLexer
from grammar_safetalkParser import grammar_safetalkParser
from interpreter import SafeTalkInterpreter

def test_smart_interpreter():
    print("--- SafeTalk AI Hybrid Test ---")
    
    # 1. The Command
    # "huge" is not defined in Python. It MUST come from the AI.
    command = "find files where size > huge"
    print(f"INPUT: \"{command}\"")

    # 2. Setup
    input_stream = InputStream(command)
    lexer = grammar_safetalkLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = grammar_safetalkParser(stream)
    tree = parser.program()

    # 3. Run
    # MAKE SURE YOU PASTED YOUR API KEY IN interpreter.py FIRST!
    interpreter = SafeTalkInterpreter()
    interpreter.visit(tree)

if __name__ == '__main__':
    test_smart_interpreter()