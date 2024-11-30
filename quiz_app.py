import tkinter as tk
from tkinter import messagebox
import random
from questions_data import questions  # Import the questions from the separate file

class QuizApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Java Quiz")
        self.master.geometry("700x500")
        self.score = 0
        self.current_question = 0
        self.wrong_questions = []
        self.questions = questions.copy()
        random.shuffle(self.questions)
        self.total_questions = len(self.questions)

        self.create_widgets()
        self.display_question()

    def create_widgets(self):
        self.question_label = tk.Label(self.master, text="", wraplength=650, justify="left", font=("Arial", 12))
        self.question_label.pack(pady=20)

        self.option_buttons = []
        for i in range(5):  # this is for 5 options per question
            btn = tk.Button(self.master, text="", width=60, anchor="w", command=lambda idx=i: self.check_answer(idx))
            btn.pack(pady=5)
            self.option_buttons.append(btn)

        # For flashcards
        self.flip_button = tk.Button(self.master, text="Show Answer", command=self.show_flashcard_answer)
        self.flip_button.pack(pady=10)
        self.flip_button.pack_forget()  

        self.explanation_label = tk.Label(self.master, text="", wraplength=650, justify="left", font=("Arial", 12))
        self.explanation_label.pack(pady=20)
        self.explanation_label.pack_forget()  

        self.next_button = tk.Button(self.master, text="Next", command=self.next_question)
        self.next_button.pack(pady=10)
        self.next_button.pack_forget()  

        self.progress_label = tk.Label(self.master, text="")
        self.progress_label.pack(pady=10)

    def display_question(self):
        self.explanation_label.pack_forget()
        self.next_button.pack_forget()
        self.flip_button.pack_forget()
        for btn in self.option_buttons:
            btn.pack_forget()

        if self.current_question < len(self.questions):
            q = self.questions[self.current_question]
            self.question_label.config(text=f"Q{self.current_question + 1}: {q['question']}")
            self.progress_label.config(text=f"Question {self.current_question + 1} of {self.total_questions}")

            if q['type'] == 'mcq':
                options = q['options']
                for i, option in enumerate(options):
                    self.option_buttons[i].config(text=f"{chr(65 + i)}. {option}", bg="SystemButtonFace", state="normal")
                    self.option_buttons[i].pack(pady=5)
                for i in range(len(options), 5):
                    self.option_buttons[i].pack_forget()  # Hide unused buttons
            elif q['type'] == 'flashcard':
                self.flip_button.pack(pady=10)
        else:
            if self.wrong_questions:
                self.questions = self.wrong_questions.copy()
                self.wrong_questions = []
                self.current_question = 0
                random.shuffle(self.questions)
                self.total_questions = len(self.questions)
                messagebox.showinfo("Retry", "Now retrying the questions you got wrong.")
                self.display_question()
            else:
                messagebox.showinfo("Quiz Completed", f"You have completed the quiz!\nYour score: {self.score}")
                self.master.quit()

    def check_answer(self, idx):
        selected_option = chr(65 + idx)
        q = self.questions[self.current_question]
        correct_answer = q['answer']
        if selected_option == correct_answer:
            self.option_buttons[idx].config(bg="green")
            self.score += 1
            self.master.after(500, self.next_question)
        else:
            self.option_buttons[idx].config(bg="red")
            correct_idx = ord(correct_answer) - 65
            self.option_buttons[correct_idx].config(bg="green")
            self.wrong_questions.append(self.questions[self.current_question])
            # Show explanation
            self.show_explanation()
        # Disable all buttons after an answer is selected
        for btn in self.option_buttons:
            btn.config(state="disabled")

    def show_explanation(self):
        q = self.questions[self.current_question]
        self.explanation_label.config(text=f"Explanation: {q.get('explanation', 'No explanation provided.')}")
        self.explanation_label.pack(pady=20)
        self.next_button.pack(pady=10)

    def show_flashcard_answer(self):
        q = self.questions[self.current_question]
        self.explanation_label.config(text=f"Answer: {q.get('answer', 'No answer provided.')}\n\nExplanation: {q.get('explanation', '')}")
        self.explanation_label.pack(pady=20)
        self.flip_button.pack_forget()
        self.next_button.pack(pady=10)

    def next_question(self):
        self.current_question += 1
        # Reset UI elements
        self.explanation_label.config(text="")
        self.explanation_label.pack_forget()
        self.next_button.pack_forget()
        for btn in self.option_buttons:
            btn.config(state="normal", bg="SystemButtonFace")
        self.display_question()

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
