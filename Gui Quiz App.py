import tkinter as tk
from tkinter import messagebox
import random

class QuizApp:
    """
        A simple quiz application built with Tkinter.
    """
    def __init__(self, root, questions):
        """
        Initializes the QuizApp.

        Args:
            root: The Tkinter root window.
            questions: A list of questions and answer choices.
        """
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

        self.user_answers = []  # Correctly initialized here

    def display_question(self):
        """Displays the current question and answer choices."""
        question, *choices = self.questions[self.current_question_index]
        random.shuffle(choices)
        self.correct_answer = next(opt for opt in choices if opt.endswith('*')).replace('*', '')

        self.question_label.config(text=question)
        self.var.set("-1")
        for idx, choice in enumerate(choices):
            self.options[idx].config(text=choice.replace('*', ''), value=choice.replace('*', ''))

    def next_question(self):
        """Handles the 'Next' button click, checks the answer, and moves to the next question."""
        if self.var.get() == "-1":
            messagebox.showwarning("Warning", "Please select an answer!")
            return

        selected_answer = self.var.get()
        self.user_answers.append(selected_answer)

        selected_answer = self.var.get()
        if selected_answer == self.correct_answer:
            self.score += 1

        self.current_question_index += 1
        if self.current_question_index < len(self.questions):
            self.display_question()
        else:
            self.show_result()

    def show_result(self):
        """Displays the final score and review of answers."""

        result_window = tk.Toplevel(self.root)  # Create a new window for results
        result_window.title("Quiz Results")

        score_label = tk.Label(result_window, text=f"Your Score: {self.score}/{len(self.questions)}",
                               font=("Arial", 14, "bold"))
        score_label.pack(pady=20)

        grade = self.score  * 4
        grade_label = tk.Label(result_window, text=f"Your Grade: {grade:.2f}",
                               font=("Arial", 14, "bold"))
        # Display grade
        grade_label.pack()

        # Canvas for scrolling
        canvas = tk.Canvas(result_window)
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)  # Fill and expand

        # Scrollbar
        scrollbar = tk.Scrollbar(result_window, orient="vertical", command=canvas.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        canvas.configure(yscrollcommand=scrollbar.set)  # Link scrollbar to canvas
        canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))  # Update scrollregion

        # Frame inside the canvas
        review_frame = tk.Frame(canvas)
        canvas.create_window((0, 0), window=review_frame, anchor="nw")  # Place frame in canvas

        for i, (question, *choices) in enumerate(self.questions):
            q_label = tk.Label(review_frame, text=f"{i + 1}. {question}", font=("Arial", 12))
            q_label.pack(anchor="w", pady=(10, 0))

            user_answer = self.user_answers[i]
            correct_answer = next((choice for choice in choices if choice.endswith('*')), "").replace('*', '')

            for choice in choices:
                choice = choice.replace("*", "")
                color = "green" if choice == correct_answer else "red" if choice == user_answer else "black"
                ans_label = tk.Label(review_frame, text=choice, font=("Arial", 10), fg=color)
                ans_label.pack(anchor="w", padx=20)

        close_button = tk.Button(result_window, text="Close", command=self.root.destroy, font=("Arial", 12))
        close_button.pack(pady=20)


def load_questions(filename):
    """
        Loads questions from a text file.

        Args:
            filename: The name of the file containing the questions.

        Returns:
            A list of questions and answer choices.
        """
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
