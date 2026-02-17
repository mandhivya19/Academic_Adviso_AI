from fastapi import FastAPI
from backend.llm import ask_ai       # Chat function import
from backend.db import students_collection # Database import

app = FastAPI()

# 1. Home Route
@app.get("/")
def home():
    return {"message": "Academic Advisor API Running"}

# 2. Chat Route (AI kitta pesuradhukku)
@app.get("/chat")
def chat(q: str):
    response = ask_ai(q)
    return {"response": response}

# 3. Student Snapshot Route (Day 3 Target - Marks edukka)
@app.get("/student/snapshot")
def get_snapshot(name: str):
    # Database-la student-a thedurom
    student = students_collection.find_one({"name": name}, {"_id": 0})
    if student:
        return {"status": "found", "data": student}
    else:
        return {"status": "error", "message": "Student not found"}