import tkinter as tk
import time
import random

texts = [
    "The quick brown fox jumps over the lazy dog.",
    "Python is a powerful programming language.",
    "Typing speed tests are a great way to improve accuracy.",
    "Practice makes perfect, especially when it comes to typing."
]
def start_typing():
    global start_time
    start_time = time.time()
    entry_text.delete("1.0", tk.END)
    result_label.config(text="Typing...")

def finish_typing():
    end_time = time.time()
    time_taken = end_time - start_time
    typed_text = entry_text.get("1.0", tk.END).strip()
    word_count = len(typed_text.split())
    
    speed = word_count / (time_taken / 60) 
    accuracy = calculate_accuracy(selected_text, typed_text)
    
    result_label.config(text=f"Speed: {speed:.2f} WPM | Accuracy: {accuracy:.2f}%")

def calculate_accuracy(original, typed):
    original_words = original.split()
    typed_words = typed.split()
    correct_words = sum(1 for o, t in zip(original_words, typed_words) if o == t)
    accuracy = (correct_words / len(original_words)) * 100
    return accuracy


root = tk.Tk()
root.title("Typing Speed Test")

selected_text = random.choice(texts)
text_label = tk.Label(root, text=selected_text,font=("Helvetica", 14), wraplength=500)
text_label.pack(pady=10)

entry_text = tk.Text(root, height=5, width=60, font=("Helvetica", 14))
entry_text.pack()

start_button = tk.Button(root, text="Start", command=start_typing)
start_button.pack(pady=5)

finish_button = tk.Button(root, text="Finish", command=finish_typing)
finish_button.pack(pady=5)

result_label = tk.Label(root, text="", font=("Helvetica", 12))
result_label.pack(pady=10)

root.mainloop()