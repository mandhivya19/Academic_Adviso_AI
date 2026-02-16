import os
from dotenv import load_dotenv

load_dotenv()

print("PATH:", os.getcwd())
print("Key:", os.getenv("LLM_API_KEY"))
print("Loaded:", bool(os.getenv("LLM_API_KEY")))
