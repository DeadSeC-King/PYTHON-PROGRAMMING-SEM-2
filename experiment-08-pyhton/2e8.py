#2.	Design a GUI based basic calculator for performing basic arithmetic operations.
import tkinter as tk
def add():
    num1=float(entry1.get())
    num2=float(entry2.get())
    result=num1+num2
    label_result.config(text="Result: "+str(result))
def subtract():
    num1=float(entry1.get())
    num2=float(entry2.get())
    result=num1-num2
    label_result.config(text="Result: "+str(result))
def multiply():
    num1=float(entry1.get())
    num2=float(entry2.get())
    result=num1*num2
    label_result.config(text="Result: "+str(result))
def divide():
    num1=float(entry1.get())
    num2=float(entry2.get())
    if num2!=0:
        result=num1/num2
        label_result.config(text="Result: "+str(result))
    else:
        label_result.config(text="Error: Division by zero")
root=tk.Tk()
root.title("Basic Calculator")
root.geometry("300x200")
entry1=tk.Entry(root)
entry1.pack()
entry2=tk.Entry(root)
entry2.pack()
button_add=tk.Button(root,text="Add",command=add)
button_add.pack()
button_subtract=tk.Button(root,text="Subtract",command=subtract)
button_subtract.pack()
button_multiply=tk.Button(root,text="Multiply",command=multiply)
button_multiply.pack()
button_divide=tk.Button(root,text="Divide",command=divide)
button_divide.pack()
label_result=tk.Label(root,text="Result: ")
label_result.pack()
root.mainloop()
