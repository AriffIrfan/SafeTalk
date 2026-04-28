# SafeTalk AI 🛡️

**Transparent & Safe Natural Language Execution**

SafeTalk is a custom, natural-language-style interpreter built using Python, ANTLR4, and Google Gemini AI. It allows users to execute file-system-like commands in plain English while ensuring safety and strict structural integrity. By integrating Gemini 2.5 Flash, SafeTalk uniquely handles semantic ambiguity (e.g., words like `huge` or `recent`), translating subjective terms into precise, execution-ready numerical values without compromising the deterministic nature of the parser.

## 🚀 Features

- **Custom Grammar Engine**: Built with ANTLR4, providing robust, deterministic parsing of natural language commands into Abstract Syntax Trees (ASTs).
- **AI-Powered Ambiguity Resolution**: The interpreter uses Google Gemini to automatically resolve subjective and ambiguous terms (e.g., `huge`, `tiny`, `recent`) into contextual numerical values dynamically based on the attribute being evaluated.
- **Explainability built-in**: Use commands like `explain last` or `explain history`, and the system will output a clear, user-friendly justification of the executed actions and why they occurred.
- **User-Friendly Error Handling**: Includes a custom `SafeTalkErrorListener` that intercepts ANTLR stack traces and converts them into helpful, context-aware suggestions (e.g., "I was expecting a command verb").
- **Interactive UI**: A built-in Streamlit web application (`app.py`) provides an interactive chat interface, a live memory debugger, and an execution log.

## 🛠️ Technologies Used

- **Python 3**
- **ANTLR4** (`antlr4-python3-runtime`) for lexing and parsing.
- **Streamlit** for the web interface.
- **Google Generative AI** (`google-generativeai`) for LLM-driven ambiguity resolution.

## 📦 Setup and Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/AriffIrfan/SafeTalk.git
   cd SafeTalk
   ```

2. **Install dependencies**
   Make sure you have Python 3 installed, then run:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure API Key**
   To enable the AI capabilities (ambiguity resolution and explainability), create a `secrets_config.py` file in the root directory and add your Google Gemini API key:
   ```python
   GOOGLE_API_KEY = "your_google_api_key_here"
   ```
   *(If this is omitted, SafeTalk will run with LLM features disabled and use fallback values).*

4. **Regenerate ANTLR files (Optional)**
   If you modify the grammar in `grammar_safetalk.g4`, regenerate the Lexer, Parser, and Visitor using the included `.jar`:
   ```bash
   java -jar antlr-4.13.2-complete.jar -Dlanguage=Python3 -visitor grammar_safetalk.g4
   ```

## 💻 Usage

### Run the Streamlit Web App
To interact with SafeTalk through the interactive UI:
```bash
streamlit run app.py
```

### Run Tests via CLI
To test the core parser and interpreter via the command line:
```bash
python main.py
```

## 📝 Language Syntax Examples

SafeTalk supports natural-language statements parsed rigidly by ANTLR. Examples include:

- **Core Commands**: 
  `find files where size > huge`
  `delete documents`
- **Assignments**: 
  `set limit to 10 + 5 * 2`
  `let size be 100`
- **Conditionals**: 
  `if size > 50 then archive documents`
- **Explainability**: 
  `explain last`
  `explain history`
