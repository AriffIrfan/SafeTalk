import google.generativeai as genai

# 🔴 PASTE YOUR KEY HERE AGAIN
GENAI_API_KEY = "AIzaSyDGkj9VODlwe6slx-Y-zML5O1_NdxsU09Q"

genai.configure(api_key=GENAI_API_KEY)

print("Checking available models for your API key...")
try:
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            print(f"- {m.name}")
except Exception as e:
    print(f"Error: {e}")