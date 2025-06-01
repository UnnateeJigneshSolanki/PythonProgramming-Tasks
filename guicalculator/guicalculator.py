import tkinter as tk
import math
from tkinter import messagebox
def calculate():
    exp = entry.get()
    if '+' in exp:
        num1,num2 = exp.split('+')
        ans = float(num1) + float(num2)
    elif '-' in exp:
        num1,num2 = exp.split('-')
        ans = float(num1) - float(num2)
    elif '*' in exp:
        num1,num2 = exp.split('*')
        ans = float(num1) * float(num2)
    elif '/' in exp:
        num1,num2 = exp.split('/')
        if float(num2) == 0:
            messagebox.showerror("Division by zero not possible")
            return
        ans = float(num1) / float(num2)
    elif '%' in exp:
        num1,num2 = exp.split('%')
        ans = float(num1) % float(num2)
    else:
        messagebox.showerror("Not a valid expression!")
        return
    messagebox.showinfo("Result", ans)
def click(btext):
    entry.insert(tk.END,btext)
def clear():
    entry.delete(0,tk.END)
def backspace():
    x = entry.get()
    entry.delete(0,tk.END)
    entry.insert(0, x[:-1])
root = tk.Tk()
root.title('GUI CALCULATOR')
root.configure(bg="black")
entry = tk.Entry(root, width=15,font=("Arial",19), justify="right",bd=3)
entry.grid(padx=12,pady=12,columnspan=4)
buttons=['1','2','3','4','5','6','7','8','9','0','+','-','*','/','%','<--','=','C',]
row = 1
col = 0
for b in buttons:
    if b == '=':
        btn = tk.Button(root,text=b,command=calculate,width=4,height=2,background='blue',fg='white')
    elif b == 'C':
        btn = tk.Button(root,text=b,command=clear,width=4,height=2,background='blue',fg='white')
    elif b == '<--':
        btn = tk.Button(root,text=b,command=backspace,width=4,height=2,background='blue',fg='white')
    else:
        btn = tk.Button(root,text=b,command=lambda b=b :click(b))
    btn.grid(row=row,column=col,padx=10,pady=10)
    col += 1
    if col > 2:
        col = 0
        row += 1
root.mainloop()