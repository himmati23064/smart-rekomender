import json

def load_courses():
    with open("courses.json", "r") as f:
        return json.load(f)

def recommend_courses(interest, score):
    courses = load_courses()
    recommended = []
    for course in courses:
        if interest.lower() in course["required_interest"].lower() and score >= course["min_score"]:
            recommended.append(course)
    return recommended
