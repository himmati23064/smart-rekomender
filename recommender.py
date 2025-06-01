import json

def recommend_courses(interest, score):
    with open("data/courses.json") as f:
        courses = json.load(f)

    recommendations = []
    for course in courses:
        if interest.lower() in course["required_interest"].lower() and score >= course["min_score"]:
            recommendations.append(course["course"])
    return recommendations
