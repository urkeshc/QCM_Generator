import tkinter as tk
from tkinter import messagebox, simpledialog
import random
from questions_data import questions  # Importer les questions depuis le fichier séparé

class QuizApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Java Quiz")
        self.master.geometry("700x500")
        self.master.configure(bg="black")  # Définir l'arrière-plan en noir
        self.score = 0
        self.total_attempted = 0  # Pour calculer le pourcentage
        self.current_question = 0
        self.wrong_questions = []
        self.selection_made = False  # Indicateur pour empêcher les sélections multiples

        # Copier les questions et les mélanger
        self.all_questions = questions.copy()
        random.shuffle(self.all_questions)

        # Demander à l'utilisateur combien de questions il souhaite répondre
        num_questions = simpledialog.askinteger(
            "Nombre de questions",
            "Combien de questions souhaitez-vous répondre ?",
            minvalue=1,
            maxvalue=len(self.all_questions)
        )

        if num_questions is None:
            # L'utilisateur a annulé, quitter le quiz
            self.master.quit()
            return
        else:
            # Sélectionner aléatoirement le nombre de questions souhaité
            self.questions = random.sample(self.all_questions, num_questions)
            self.total_questions = len(self.questions)

        self.create_widgets()
        self.display_question()

        # Lier les événements de touches pour la saisie au clavier
        self.master.bind('<Key>', self.key_pressed)

    def create_widgets(self):
        self.question_label = tk.Label(
            self.master,
            text="",
            wraplength=650,
            justify="left",
            font=("Arial", 12),
            fg="white",  # Couleur du texte en blanc
            bg="black"   # Arrière-plan en noir
        )
        self.question_label.pack(pady=20)

        # Créer un Frame pour contenir les boutons d'options
        self.options_frame = tk.Frame(self.master, bg="black")
        self.options_frame.pack(pady=10)

        self.option_buttons = []
        for i in range(5):  # En supposant un maximum de 5 options par question
            btn = tk.Button(
                self.options_frame,
                text="",
                width=50,          # Fixer une largeur pour les boutons
                anchor="w",
                font=("Arial", 12),
                fg="white",        # Couleur du texte en blanc
                bg="black",        # Arrière-plan en noir
                wraplength=400,    # Gérer le retour à la ligne
                justify="left"     # Justifier le texte à gauche
            )
            btn.config(command=lambda idx=i: self.check_answer(idx))
            btn.pack(pady=5)
            self.option_buttons.append(btn)

        # Pour les flashcards
        self.flip_button = tk.Button(
            self.master,
            text="Afficher la réponse",
            font=("Arial", 12),
            fg="white",
            bg="black",
            command=self.show_flashcard_answer
        )
        self.flip_button.pack(pady=10)
        self.flip_button.pack_forget()  # Masquer initialement

        self.explanation_label = tk.Label(
            self.master,
            text="",
            wraplength=650,
            justify="left",
            font=("Arial", 12),
            fg="white",
            bg="black"
        )
        self.explanation_label.pack(pady=20)
        self.explanation_label.pack_forget()  # Masquer initialement

        self.next_button = tk.Button(
            self.master,
            text="Suivant",
            font=("Arial", 12),
            fg="white",
            bg="black",
            command=self.next_question
        )
        self.next_button.pack(pady=10)
        self.next_button.pack_forget()  # Masquer initialement

        self.progress_label = tk.Label(
            self.master,
            text="",
            font=("Arial", 12),
            fg="white",
            bg="black"
        )
        self.progress_label.pack(pady=10)

    def display_question(self):
        self.selection_made = False  # Réinitialiser l'indicateur de sélection
        self.explanation_label.pack_forget()
        self.next_button.pack_forget()
        self.flip_button.pack_forget()
        for btn in self.option_buttons:
            btn.pack_forget()

        if self.current_question < len(self.questions):
            q = self.questions[self.current_question]
            self.question_label.config(text=f"Q{self.current_question + 1}: {q['question']}")
            self.progress_label.config(text=f"Question {self.current_question + 1} sur {self.total_questions}")

            if q['type'] == 'mcq':
                options = q['options']
                # Créer une liste de tuples (option_text, original_index)
                option_list = list(enumerate(options))
                # Mélanger les options
                random.shuffle(option_list)
                # Mettre à jour le mapping des options pour cette question
                self.current_options = option_list  # Stocker les options actuelles
                # Trouver le nouvel index de la réponse correcte
                correct_answer = q['answer']
                correct_index = ord(correct_answer.upper()) - ord('A')  # Convertir en index
                # Trouver le nouvel index de la bonne réponse après le mélange
                for new_idx, (original_idx, option_text) in enumerate(option_list):
                    if original_idx == correct_index:
                        self.correct_option_index = new_idx
                        break
                # Afficher les options mélangées
                for i, (original_idx, option_text) in enumerate(option_list):
                    self.option_buttons[i].config(
                        text=f"{chr(65 + i)}. {option_text}",
                        bg="black",
                        fg="white",
                        state="normal"
                    )
                    self.option_buttons[i].pack(pady=5)
                for i in range(len(options), 5):
                    self.option_buttons[i].pack_forget()  # Masquer les boutons inutilisés
            elif q['type'] == 'flashcard':
                self.flip_button.pack(pady=10)
        else:
            # Calculer le pourcentage
            percentage = (self.score / self.total_attempted) * 100 if self.total_attempted > 0 else 0
            # Afficher le score après chaque passage
            messagebox.showinfo(
                "Fin du parcours",
                f"Vous avez terminé ce parcours !\nVotre score : {self.score}/{self.total_attempted}\nPourcentage : {percentage:.2f}%"
            )

            if self.wrong_questions:
                # Réinitialiser pour le prochain passage
                self.questions = self.wrong_questions.copy()
                self.wrong_questions = []
                self.current_question = 0
                random.shuffle(self.questions)
                self.total_questions = len(self.questions)
                # Réinitialiser le score et le total tenté pour le nouveau passage
                self.score = 0
                self.total_attempted = 0
                messagebox.showinfo("Réessayer", "Nous allons maintenant réessayer les questions auxquelles vous avez mal répondu.")
                self.display_question()
            else:
                messagebox.showinfo("Quiz Terminé", "Vous avez répondu correctement à toutes les questions !")
                self.master.quit()

    def check_answer(self, idx):
        if self.selection_made:
            return  # Ignorer si une sélection a déjà été faite
        self.selection_made = True

        selected_option = idx  # L'index de l'option sélectionnée
        self.total_attempted += 1  # Incrémenter le total des questions tentées

        if selected_option == self.correct_option_index:
            self.option_buttons[idx].config(bg="green", fg="white")
            self.score += 1
            self.master.after(500, self.next_question)
        else:
            self.option_buttons[idx].config(bg="red", fg="white")
            # Indiquer la bonne réponse
            correct_idx = self.correct_option_index
            if 0 <= correct_idx < len(self.option_buttons):
                self.option_buttons[correct_idx].config(bg="green", fg="white")
            self.wrong_questions.append(self.questions[self.current_question])
            # Afficher l'explication
            self.show_explanation()
        # Désactiver tous les boutons après une sélection
        for btn in self.option_buttons:
            btn.config(state="disabled")

    def show_explanation(self):
        q = self.questions[self.current_question]
        self.explanation_label.config(text=f"Explication : {q.get('explanation', 'Aucune explication fournie.')}")
        self.explanation_label.pack(pady=20)
        self.next_button.pack(pady=10)

    def show_flashcard_answer(self):
        q = self.questions[self.current_question]
        self.explanation_label.config(
            text=f"Réponse : {q.get('answer', 'Aucune réponse fournie.')}\n\nExplication : {q.get('explanation', '')}"
        )
        self.explanation_label.pack(pady=20)
        self.flip_button.pack_forget()
        self.next_button.pack(pady=10)

    def next_question(self):
        self.current_question += 1
        # Réinitialiser les éléments de l'interface utilisateur
        self.explanation_label.config(text="")
        self.explanation_label.pack_forget()
        self.next_button.pack_forget()
        for btn in self.option_buttons:
            btn.config(state="normal", bg="black", fg="white")
        self.display_question()

    def key_pressed(self, event):
        if self.selection_made:
            # Si une sélection a déjà été faite, n'autoriser que Entrée pour continuer
            if event.keysym == 'Return' and self.next_button.winfo_ismapped():
                self.next_question()
            return

        if event.char.lower() in ['a', 'b', 'c', 'd', 'e']:
            idx = ord(event.char.lower()) - ord('a')
            # S'assurer que idx est dans la plage des options affichées
            if 0 <= idx < len(self.current_options):
                self.check_answer(idx)
        elif event.keysym == 'Return':
            if self.next_button.winfo_ismapped():
                self.next_question()

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
