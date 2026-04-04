#4.	Create a GUI based task manager where users can add, edit and remove tasks. Use Tkinter (buttons, listbox), SQLite/MySQL (task storage).
import tkinter as tk
import sqlite3
def add_task():
    task=entry_task.get()
    conn=sqlite3.connect('tasks.db')
    c=conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS tasks (task TEXT)''')
    c.execute("INSERT INTO tasks VALUES (?)", (task,))
    conn.commit()
    conn.close()
    entry_task.delete(0, tk.END)
    load_tasks()
def load_tasks():
    conn=sqlite3.connect('tasks.db')
    c=conn.cursor()
    c.execute("SELECT * FROM tasks")
    tasks=c.fetchall()
    conn.close()
    listbox_tasks.delete(0, tk.END)
    for task in tasks:
        listbox_tasks.insert(tk.END, task[0])
def delete_task():
    selected_task=listbox_tasks.curselection()
    if selected_task:
        task=listbox_tasks.get(selected_task)
        conn=sqlite3.connect('tasks.db')
        c=conn.cursor()
        c.execute("DELETE FROM tasks WHERE task=?", (task,))
        conn.commit()
        conn.close()
        load_tasks()
root=tk.Tk()
root.title("Task Manager")
root.geometry("300x400")
label_task=tk.Label(root,text="Task:")
label_task.pack()
entry_task=tk.Entry(root)
entry_task.pack()

button_add=tk.Button(root,text="Add Task",command=add_task)
button_add.pack()
listbox_tasks=tk.Listbox(root)
listbox_tasks.pack()
button_delete=tk.Button(root,text="Delete Task",command=delete_task)
button_delete.pack()
load_tasks()
root.mainloop()
