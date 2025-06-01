import customtkinter as ctk
from recommender import recommend_courses

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Smart Course Recommender v2")
app.geometry("500x500")

def show_recommendations():
    interest = interest_entry.get()
    try:
        score = int(score_entry.get())
    except ValueError:
        result_label.configure(text="Nilai harus berupa angka")
        return

    results = recommend_courses(interest, score)
    if results:
        message = "Rekomendasi:\n" + "\n".join(f"- {r}" for r in results)
        result_label.configure(text=message)
        global last_recommendation
        last_recommendation = message
    else:
        result_label.configure(text="Tidak ada kursus yang cocok.")

def save_result():
    try:
        with open("hasil_rekomendasi.txt", "w") as f:
            f.write(last_recommendation)
        result_label.configure(text="Hasil disimpan ke hasil_rekomendasi.txt")
    except:
        result_label.configure(text="Tidak ada hasil untuk disimpan.")

def save_feedback_like():
    with open("feedback.json", "a") as f:
        f.write('{"feedback": "like"}\n')
    result_label.configure(text="Terima kasih atas feedback 👍")

def save_feedback_dislike():
    with open("feedback.json", "a") as f:
        f.write('{"feedback": "dislike"}\n')
    result_label.configure(text="Terima kasih atas feedback 👎")

interest_entry = ctk.CTkEntry(app, placeholder_text="Masukkan minat Anda")
interest_entry.pack(pady=10)

score_entry = ctk.CTkEntry(app, placeholder_text="Masukkan nilai Anda (0-100)")
score_entry.pack(pady=10)

recommend_button = ctk.CTkButton(app, text="Dapatkan Rekomendasi", command=show_recommendations)
recommend_button.pack(pady=10)

result_label = ctk.CTkLabel(app, text="", wraplength=400)
result_label.pack(pady=20)

save_button = ctk.CTkButton(app, text="Simpan Hasil", command=save_result)
save_button.pack(pady=5)

like_button = ctk.CTkButton(app, text="👍", command=save_feedback_like)
like_button.pack(side="left", padx=40)

dislike_button = ctk.CTkButton(app, text="👎", command=save_feedback_dislike)
dislike_button.pack(side="right", padx=40)

app.mainloop()
