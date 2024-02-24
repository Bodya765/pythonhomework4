import tkinter as tk
from tkinter import messagebox
import random

def generate_number(lower, upper):
    try:
        return random.randint(lower, upper)
    except ValueError:
        messagebox.showerror("Помилка", "Введіть коректні значення для меж")

def check_guess(guess, secret_number, attempts_left, attempts_label, guess_entry):
    try:
        guess = int(guess)
        if guess == secret_number:
            messagebox.showinfo("Вітаємо!", f"Ви вгадали число {secret_number}!")
            guess_entry.config(state=tk.DISABLED)
            return attempts_left, True
        else:
            attempts_left -= 1
            if attempts_left > 0:
                messagebox.showinfo("Невірно", f"Загадане число {'більше' if guess < secret_number else 'менше'}")
                attempts_label.config(text=f"Спроба {5 - attempts_left + 1} з 5")
            else:
                messagebox.showinfo("Кінець гри", f"Ви не вгадали число {secret_number}!\nГра закінчена.")
                guess_entry.config(state=tk.DISABLED)
            return attempts_left, False
    except ValueError:
        messagebox.showerror("Помилка", "Введіть коректне число")
        return attempts_left, False

def restart_game(lower_bound_entry, upper_bound_entry, guess_entry, attempts_label):
    lower_bound_entry.delete(0, tk.END)
    upper_bound_entry.delete(0, tk.END)
    guess_entry.delete(0, tk.END)
    guess_entry.config(state=tk.DISABLED)
    attempts_label.config(text="Спроба 0 з 5")
    return generate_number(0, 100), 5

def start_new_game(lower_bound_entry, upper_bound_entry, guess_entry, attempts_label):
    lower = int(lower_bound_entry.get())
    upper = int(upper_bound_entry.get())
    return generate_number(lower, upper), 5

def main():
    root = tk.Tk()
    root.title("Вгадай число")

    lower_bound_label = tk.Label(root, text="Ліва межа:")
    upper_bound_label = tk.Label(root, text="Права межа:")
    lower_bound_entry = tk.Entry(root)
    upper_bound_entry = tk.Entry(root)
    generate_button = tk.Button(root, text="Генерувати", command=lambda: start_game(lower_bound_entry, upper_bound_entry, guess_entry, attempts_label))
    attempts_label = tk.Label(root, text="Спроба 0 з 5")
    guess_label = tk.Label(root, text="Введіть число:")
    guess_entry = tk.Entry(root, state=tk.DISABLED)
    guess_button = tk.Button(root, text="Вгадати", command=lambda: make_guess(guess_entry, secret_number, attempts_left, attempts_label))
    restart_button = tk.Button(root, text="Розпочати заново", command=lambda: restart_game(lower_bound_entry, upper_bound_entry, guess_entry, attempts_label))

    lower_bound_label.grid(row=0, column=0)
    lower_bound_entry.grid(row=0, column=1)
    upper_bound_label.grid(row=1, column=0)
    upper_bound_entry.grid(row=1, column=1)
    generate_button.grid(row=2, column=0, columnspan=2, pady=10)
    attempts_label.grid(row=3, column=0, columnspan=2)
    guess_label.grid(row=4, column=0)
    guess_entry.grid(row=4, column=1)
    guess_button.grid(row=5, column=0, columnspan=2, pady=10)
    restart_button.grid(row=6, column=0, columnspan=2)

    root.mainloop()

def start_game(lower_bound_entry, upper_bound_entry, guess_entry, attempts_label):
    secret_number, attempts_left = start_new_game(lower_bound_entry, upper_bound_entry, guess_entry, attempts_label)
    guess_entry.config(state=tk.NORMAL)

def make_guess(guess_entry, secret_number, attempts_left, attempts_label):
    attempts_left, game_over = check_guess(guess_entry.get(), secret_number, attempts_left, attempts_label, guess_entry)
    if game_over:
        guess_entry.config(state=tk.DISABLED)

if __name__ == "__main__":
    main()
