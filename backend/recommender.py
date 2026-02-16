def recommend_course(student):

    marks = student["marks"]
    interest = student["interest"]

    if interest == "AI":
        if marks >= 90:
            return "Machine Learning"
        elif marks >= 80:
            return "Data Science"
        else:
            return "Python Developer"

    if interest == "Web":
        return "Full Stack Developer"

    return "General Course"
