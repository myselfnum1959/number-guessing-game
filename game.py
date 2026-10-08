import random
from tkinter import *
from tkinter import messagebox

class guessGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Number Guess Game")
        self.root.geometry('300x400')

        self.target_number = random.randint(1, 100)
        print(self.target_number)
        self.attempts = 0

        self.title_label = Label(self.root, text="Guess a number from 1-100", font=("Arial", 12, "bold"))

        self.guess_entry = Entry(self.root, font=("Arial", 14), width=10)
        self.guess_entry.pack(pady=5)
        self.guess_entry.focus()

        self.submit_btn = Button(self.root, text="Guess", command=self.check_guess)
        self.submit_btn.pack(pady=10)

        self.feedback_label = Label(self.root, text="Enter your guess!", font=("Arial", 10), fg='blue')
        self.feedback_label.pack(pady=10)

    def check_guess(self):
        try:
            user_guess = int(self.guess_entry.get())
        except ValueError:
            messagebox.showerror("INVALID!", "Enter only integers.")
            self.guess_entry.delete(0, END)
            return

        self.attempts += 1

        if self.attempts < 5:

            if user_guess < self.target_number:
                self.feedback_label.config(text=f'Higher! (Attempts: {self.attempts})')
            elif user_guess > self.target_number:
                self.feedback_label.config(text=f'Lower! (Attempts: {self.attempts})')
            else:
                self.feedback_label.config(text="CORRECT!", fg="green")
                messagebox.showinfo("YOU WON!", "Congratulations! You won the game!")

            self.guess_entry.delete(0, END)
        else:
            self.feedback_label.config(text="YOU LOSE!", fg='red')
            self.guess_entry.delete(0, END)
            self.guess_entry.config(state='disabled')


if __name__ == "__main__":
    root = Tk()

    g = guessGame(root)
    root.mainloop()
