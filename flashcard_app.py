import tkinter as tk
from tkinter import messagebox
import random

class FlashcardApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Flashcard App")
        self.root.geometry("400x400")
        
        self.flashcards = []
        
        self.create_widgets()

    def create_widgets(self):
        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=20)
        
        self.add_flashcard_button = tk.Button(self.frame, text="Add Flashcard", command=self.add_flashcard)
        self.add_flashcard_button.grid(row=0, column=0, padx=10)

        self.quiz_mode_button = tk.Button(self.frame, text="Start Quiz", command=self.start_quiz)
        self.quiz_mode_button.grid(row=0, column=1, padx=10)
        
        self.review_button = tk.Button(self.frame, text="Review Flashcards", command=self.review_flashcards)
        self.review_button.grid(row=0, column=2, padx=10)

    def add_flashcard(self):
        self.add_window = tk.Toplevel(self.root)
        self.add_window.title("Add Flashcard")

        self.question_label = tk.Label(self.add_window, text="Enter Question:")
        self.question_label.pack(pady=5)
        self.question_entry = tk.Entry(self.add_window, width=40)
        self.question_entry.pack(pady=5)

        self.answer_label = tk.Label(self.add_window, text="Enter Answer:")
        self.answer_label.pack(pady=5)
        self.answer_entry = tk.Entry(self.add_window, width=40)
        self.answer_entry.pack(pady=5)

        self.add_button = tk.Button(self.add_window, text="Add Flashcard", command=self.save_flashcard)
        self.add_button.pack(pady=10)

    def save_flashcard(self):
        question = self.question_entry.get()
        answer = self.answer_entry.get()

        if question and answer:
            self.flashcards.append({"question": question, "answer": answer})
            messagebox.showinfo("Flashcard Added", "Flashcard added successfully!")
            self.add_window.destroy()
        else:
            messagebox.showerror("Input Error", "Both fields are required.")

    def start_quiz(self):
        if not self.flashcards:
            messagebox.showwarning("No Flashcards", "No flashcards available to quiz.")
            return
            
        random.shuffle(self.flashcards)

        self.quiz_window = tk.Toplevel(self.root)
        self.quiz_window.title("Quiz Mode")

        self.index = 0
        self.show_question()

    def show_question(self):
        current_flashcard = self.flashcards[self.index]
        self.question_label = tk.Label(self.quiz_window, text=current_flashcard["question"], font=("Arial", 14))
        self.question_label.pack(pady=20)

        self.answer_button = tk.Button(self.quiz_window, text="Show Answer", command=self.show_answer)
        self.answer_button.pack(pady=10)

    def show_answer(self):
        current_flashcard = self.flashcards[self.index]
        self.answer_label = tk.Label(self.quiz_window, text="Answer: " + current_flashcard["answer"], font=("Arial", 14))
        self.answer_label.pack(pady=20)

        self.next_button = tk.Button(self.quiz_window, text="Next", command=self.next_question)
        self.next_button.pack(pady=10)

    def next_question(self):
        self.index += 1
        if self.index < len(self.flashcards):
            for widget in self.quiz_window.winfo_children():
                widget.destroy()
            self.show_question()
        else:
            messagebox.showinfo("Quiz Completed", "You have completed the quiz!")
            self.quiz_window.destroy()

    def review_flashcards(self):
        if not self.flashcards:
            messagebox.showwarning("No Flashcards", "No flashcards available to review.")
            return

        self.review_window = tk.Toplevel(self.root)
        self.review_window.title("Review Flashcards")

        for flashcard in self.flashcards:
            flashcard_text = f"Q: {flashcard['question']}\nA: {flashcard['answer']}\n"
            flashcard_label = tk.Label(self.review_window, text=flashcard_text, font=("Arial", 12), justify="left")
            flashcard_label.pack(pady=10)

root = tk.Tk()
flashcard_app = FlashcardApp(root)
root.mainloop()
