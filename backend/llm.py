import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

# Unga API Key
api_key = "AIzaSyDM8-rHvE6AOGgib-u6245j5Mtrctxe8J0"

try:
    genai.configure(api_key=api_key)
except Exception as e:
    print(f"Config Error: {e}")

def ask_ai(prompt):
    try:
        # ✅ CORRECT MODEL NAME FROM YOUR LIST
        model = genai.GenerativeModel("gemini-2.5-flash") 
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"AI Error: {str(e)}"