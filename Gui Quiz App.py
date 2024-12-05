import tkinter as tk
from tkinter import messagebox
import random

class QuizApp:
    def __init__(self, root, questions):
        self.root = root
        self.root.title("Python Quiz")
        self.questions = questions
        self.current_question_index = 0
        self.score = 0
        random.shuffle(self.questions)

        # UI Elements
        self.question_label = tk.Label(root, text="", wraplength=400, font=("Arial", 14))
        self.question_label.pack(pady=20)

        self.var = tk.StringVar()
        self.options = []
        for i in range(4):
            rb = tk.Radiobutton(root, text="", variable=self.var, value=str(i), font=("Arial", 12))
            rb.pack(anchor="w", padx=50, pady=5)
            self.options.append(rb)

        self.next_button = tk.Button(root, text="Next", command=self.next_question, font=("Arial", 12))
        self.next_button.pack(pady=20)

        self.display_question()

    def display_question(self):
        question, *choices = self.questions[self.current_question_index]
        random.shuffle(choices)
        self.correct_answer = next(opt for opt in choices if opt.endswith('*')).replace('*', '')

        self.question_label.config(text=question)
        self.var.set("-1")
        for idx, choice in enumerate(choices):
            self.options[idx].config(text=choice.replace('*', ''), value=choice.replace('*', ''))

    def next_question(self):
        if self.var.get() == "-1":
            messagebox.showwarning("Warning", "Please select an answer!")
            return

        selected_answer = self.var.get()
        if selected_answer == self.correct_answer:
            self.score += 1

        self.current_question_index += 1
        if self.current_question_index < len(self.questions):
            self.display_question()
        else:
            self.show_result()

    def show_result(self):
        messagebox.showinfo("Quiz Completed", f"Your Score: {self.score}/{len(self.questions)}")
        self.root.quit()


def load_questions(filename):
    with open(filename, "r") as file:
        lines = [line.strip() for line in file if line.strip()]
        questions = []
        for i in range(0, len(lines), 5):
            questions.append(lines[i:i+5])
        return questions


if __name__ == "__main__":
    questions = load_questions("questions.txt")
    questions = questions[:25]  # Limit to 25 questions if there are more

    root = tk.Tk()
    app = QuizApp(root, questions)
    root.mainloop()
