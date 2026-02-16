from backend.db import students_collection

student = {
    "name": "Divi",
    "marks": 92,
    "interest": "AI"
}

students_collection.insert_one(student)

print("Student inserted")
