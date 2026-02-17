import os
import google.generativeai as genai

# Real key direct-ah kuduthu check pannuvom
api_key = "AIzaSyDM8-rHvE6AOGgib-u6245j5Mtrctxe8J0" 
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-pro")

print("AI-kitta question kekkuren... wait pannunga...")
try:
    response = model.generate_content("Hi, are you working?")
    print("AI Response:", response.text)
except Exception as e:
    print("Error:", e)