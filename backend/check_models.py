import google.generativeai as genai
import os

# Unga API Key
api_key = "AIzaSyDM8-rHvE6AOGgib-u6245j5Mtrctxe8J0"
genai.configure(api_key=api_key)

print("🔍 Checking available models for your Key...")

try:
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            print(f"✅ Found: {m.name}")
except Exception as e:
    print(f"❌ Error: {e}")