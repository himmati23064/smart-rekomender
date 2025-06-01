import customtkinter as ctk
from recommender import recommend_courses
from quiz import questions, calculate_score

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Smart Course Recommender - Kuis")
app.geometry("600x500")

user_answers = []
current_q = 0
score = 0
interest = ""

frame = ctk.CTkFrame(master=app)
frame.pack(pady=20, padx=20, fill="both", expand=True)

def clear_frame():
    for widget in frame.winfo_children():
        widget.destroy()

def show_question():
    global current_q
    clear_frame()
    q = questions[current_q]
    ctk.CTkLabel(frame, text=f"Soal {current_q+1}: {q['question']}", wraplength=500).pack(pady=10)
    for i, opt in enumerate(q["options"]):
        ctk.CTkButton(frame, text=opt, command=lambda i=i: save_answer(i)).pack(pady=5)

def save_answer(answer):
    global current_q
    user_answers.append(answer)
    current_q += 1
    if current_q < len(questions):
        show_question()
    else:
        show_result()

def show_result():
    global score
    score = calculate_score(user_answers)
    clear_frame()
    ctk.CTkLabel(frame, text=f"Skor Anda: {score}").pack(pady=10)
    ctk.CTkLabel(frame, text=f"Rekomendasi Kursus untuk Minat: {interest}").pack(pady=10)
    results = recommend_courses(interest, score)
    if not results:
        ctk.CTkLabel(frame, text="Tidak ada kursus yang cocok.").pack()
    for course in results:
        ctk.CTkLabel(frame, text=f"- {course['course']}").pack(pady=2)

def start_quiz():
    global interest, user_answers, current_q
    interest = interest_entry.get()
    user_answers = []
    current_q = 0
    show_question()

clear_frame()
ctk.CTkLabel(frame, text="Masukkan minat Anda (AI, Web, Data, Game Dev)").pack(pady=10)
interest_entry = ctk.CTkEntry(frame)
interest_entry.pack(pady=5)
ctk.CTkButton(frame, text="Mulai Kuis", command=start_quiz).pack(pady=10)

app.mainloop()
