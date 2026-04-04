import tkinter as tk
from tkinter import messagebox
import sqlite3
import hashlib

# ================= DATABASE SETUP =================
conn = sqlite3.connect('users.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
)
''')
conn.commit()

# ================= SECURITY =================
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# ================= FUNCTIONS =================
def signup():
    username = entry_user.get()
    password = entry_pass.get()

    if not username or not password:
        messagebox.showerror("Error", "All fields required")
        return

    hashed = hash_password(password)

    try:
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed))
        conn.commit()
        messagebox.showinfo("Success", "Account created successfully")
    except sqlite3.IntegrityError:
        messagebox.showerror("Error", "Username already exists")


def login():
    username = entry_user.get()
    password = entry_pass.get()

    hashed = hash_password(password)

    cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, hashed))
    result = cursor.fetchone()

    if result:
        messagebox.showinfo("Success", f"Welcome {username}!")
    else:
        messagebox.showerror("Error", "Invalid credentials")

# ================= UI =================
root = tk.Tk()
root.title("Login System")
root.geometry("300x250")

label_title = tk.Label(root, text="Login / Signup", font=("Arial", 14))
label_title.pack(pady=10)

label_user = tk.Label(root, text="Username")
label_user.pack()
entry_user = tk.Entry(root)
entry_user.pack()

label_pass = tk.Label(root, text="Password")
label_pass.pack()
entry_pass = tk.Entry(root, show="*")
entry_pass.pack()

btn_login = tk.Button(root, text="Login", width=10, command=login)
btn_login.pack(pady=5)

btn_signup = tk.Button(root, text="Signup", width=10, command=signup)
btn_signup.pack(pady=5)

root.mainloop()

# ================= NOTES =================
# Run this file directly.
# A database file 'users.db' will be created automatically.
# Passwords are stored securely using SHA-256 hashing.
