import streamlit as st
import sys
import contextlib
from io import StringIO
from antlr4 import *
from grammar_safetalkLexer import grammar_safetalkLexer
from grammar_safetalkParser import grammar_safetalkParser
from interpreter import SafeTalkInterpreter

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="SafeTalk AI", page_icon="🛡️", layout="wide")

st.title("🛡️ SafeTalk AI Interpreter")
st.markdown("### Transparent & Safe Natural Language Execution")

# --- INITIALIZE SESSION STATE ---
if "interpreter" not in st.session_state:
    st.session_state.interpreter = SafeTalkInterpreter()
    st.session_state.messages = [] 

# --- FUNCTION TO EXECUTE COMMANDS ---
def run_command():
    user_input = st.session_state.user_input
    if not user_input:
        return

    # 1. Show User Message
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    # 2. CAPTURE OUTPUT (The Magic Trick)
    # We create a "fake terminal" (buffer) to catch print statements
    capture_buffer = StringIO()
    
    try:
        # Redirect all 'print' statements to our buffer instead of the console
        with contextlib.redirect_stdout(capture_buffer):
            # Setup ANTLR
            input_stream = InputStream(user_input)
            lexer = grammar_safetalkLexer(input_stream)
            stream = CommonTokenStream(lexer)
            parser = grammar_safetalkParser(stream)
            tree = parser.program()

            # Run Interpreter
            st.session_state.interpreter.visit(tree)
        
        # 3. Get the text from the buffer
        captured_text = capture_buffer.getvalue()
        
        # If the interpreter printed something, show it. If not, show a default message.
        if captured_text.strip():
            final_response = captured_text
        else:
            final_response = "✅ Command executed successfully (No visual output)."

        st.session_state.messages.append({"role": "assistant", "content": final_response})

    except Exception as e:
        st.session_state.messages.append({"role": "assistant", "content": f"❌ Error: {str(e)}"})

    # Clear input
    st.session_state.user_input = ""

# --- DISPLAY CHAT HISTORY ---
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.chat_message("user").write(msg["content"])
    else:
        # We use st.code for the assistant to make the logs look like a terminal
        with st.chat_message("assistant"):
            st.code(msg["content"], language="text")

# --- INPUT AREA ---
st.text_input("Enter command:", key="user_input", on_change=run_command, placeholder="Try: find files where size > huge")

# --- SIDEBAR (Live Memory Debugger) ---
st.sidebar.header("🧠 System Memory")
st.sidebar.json(st.session_state.interpreter.memory)

st.sidebar.markdown("---")
st.sidebar.subheader("History Log")
# Show the internal history list if available
if hasattr(st.session_state.interpreter, 'history'):
    st.sidebar.text("\n".join(st.session_state.interpreter.history))