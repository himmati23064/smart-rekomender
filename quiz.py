questions = [
    {
        "question": "Apa itu machine learning?",
        "options": ["Ilmu membuat mesin terbang", "AI yang belajar dari data", "Aplikasi Excel"],
        "answer": 1
    },
    {
        "question": "HTML digunakan untuk?",
        "options": ["Back-end", "Desain game", "Membuat halaman web"],
        "answer": 2
    },
    {
        "question": "Apa itu Unity?",
        "options": ["Framework web", "Game engine", "Basis data"],
        "answer": 1
    },
    {
        "question": "Python terkenal digunakan untuk?",
        "options": ["Data science", "Desain grafis", "Manajemen proyek"],
        "answer": 0
    },
    {
        "question": "Apa itu SQL?",
        "options": ["Bahasa pemrograman", "Bahasa query database", "Desain UI"],
        "answer": 1
    }
]

def calculate_score(user_answers):
    score = 0
    for i, q in enumerate(questions):
        if user_answers[i] == q["answer"]:
            score += 20
    return score