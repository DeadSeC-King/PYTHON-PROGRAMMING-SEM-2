import tkinter as tk
from datetime import datetime, timedelta
import time
import threading

# ---------- MAIN WINDOW ----------
root = tk.Tk()
root.title("Next Date Calculator 🚀")
root.geometry("500x400")
root.configure(bg="#111")

# ---------- FUNCTIONS ----------
def start_calculation():
    result_label.config(text="")
    loading_label.config(text="")
    thread = threading.Thread(target=calculate_next_date)
    thread.start()

def calculate_next_date():
    try:
        date_str = entry.get()
        input_date = datetime.strptime(date_str, "%d-%m-%Y")

        funny_lines = [
            "🔍 Finding accurate date...",
            "🌍 Aligning Earth's rotation...",
            "🛰 Consulting astronomical calculations...",
            "🧮 Calculating leap year effects...",
            "⏳ Finalizing results..."
        ]

        for line in funny_lines:
            loading_label.config(text=line)
            time.sleep(12)  # 5 lines × 12 sec = 60 sec

        next_date = input_date + timedelta(days=1)
        result_label.config(
            text=f"✅ Next Date is: {next_date.strftime('%d-%m-%Y')}",
            fg="lime"
        )

    except ValueError:
        result_label.config(text="❌ Enter date as DD-MM-YYYY", fg="red")

# ---------- UI ELEMENTS ----------
title = tk.Label(
    root, text="Next Date Finder 🗓",
    font=("Arial", 18, "bold"),
    bg="#111", fg="white"
)
title.pack(pady=15)

entry = tk.Entry(
    root, font=("Arial", 14),
    justify="center"
)
entry.pack(pady=10)
entry.insert(0, "DD-MM-YYYY")

btn = tk.Button(
    root, text="Calculate Next Date",
    font=("Arial", 12, "bold"),
    bg="#00ADB5", fg="black",
    command=start_calculation
)
btn.pack(pady=15)

loading_label = tk.Label(
    root, text="",
    font=("Arial", 12),
    bg="#111", fg="cyan"
)
loading_label.pack(pady=10)

result_label = tk.Label(
    root, text="",
    font=("Arial", 14, "bold"),
    bg="#111"
)
result_label.pack(pady=20)

# ---------- RUN ----------
root.mainloop()
