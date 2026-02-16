from backend.recommender import recommend_course
from fastapi import FastAPI
from backend.db import students_collection

app = FastAPI()

@app.get("/")
def home():
    return {"message": "API running"}

@app.get("/students")
def get_students():
    students = list(students_collection.find({}, {"_id": 0}))
    return {"students": students}
@app.get("/recommend")
def recommend():

    students = list(students_collection.find({}, {"_id": 0}))

    results = []
    for s in students:
        course = recommend_course(s)
        results.append({
            "name": s["name"],
            "recommended_course": course
        })

    return {"recommendations": results}
