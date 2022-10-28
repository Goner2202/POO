
import tkinter as tk
import tkinter.messagebox
from tkinter.constants import SUNKEN
from tkinter import *
import math
import tkinter.font as font 

window = tk.Tk()
window.title('Calculator GONE.dust')
frame = tk.Frame(master=window, bg="grey69", padx=20)
myFont = font.Font(size=22, family="Roboto")
frame.pack()
entry = tk.Entry(master=frame, relief=SUNKEN, borderwidth=3, width=22, font=(myFont))
entry.grid(row=0, column=0, columnspan=4, ipady=10, pady=10, padx=10)

def myclick(number):
    entry.insert(tk.END, number)
 
def equal():
    try:
        y = str(eval(entry.get()))
        entry.delete(0, tk.END)
        entry.insert(0, y)
    except:
        tkinter.messagebox.showinfo("Error", "Syntax Error")
  
def allclear():
    entry.delete(0, tk.END)

def clear():
    entry.txt=entry.get()[:-1]
    entry.delete(0,END)
    entry.insert(0,entry.txt)

def decimal_2_bin(*args):
    try:
        y = int(entry.get())
        entry.delete(0, tk.END)
        if y < 0:
            y = bin(y)[3:]
            y = -abs(y)
            entry.insert(0, y)
        else:
            y = bin(y)[2:]
            entry.insert(0, y)
    except:
        tkinter.messagebox.showinfo("Error", "Syntax Error")
def decimal_2_oct():
    try:
        y = int(entry.get())
        entry.delete(0, tk.END)
        if y < 0:
            y = oct(y)[3:]
            y = -abs(y)
            entry.insert(0, y)
        else:
            y = oct(y)[2:]
            entry.insert(0, y)
    except:
        tkinter.messagebox.showinfo("Error", "Syntax Error")

def decimal_2_hex():
    try:
        y = int(entry.get())
        entry.delete(0, tk.END)
        if y < 0:
            y = hex(y)[3:]
            y = -abs(y)
            entry.insert(0, y)
        else:
            y = hex(y)[2:]
            entry.insert(0, y)
    except:
        tkinter.messagebox.showinfo("Error", "Syntax Error")

def sqrt():
    try:
        y = int(entry.get())
        entry.delete(0, tk.END)
        y = math.sqrt(y)
        entry.insert(0, y)
    except:
        tkinter.messagebox.showinfo("Error", "Syntax Error")

class Number:
    zero = '0'
    one = '1'
    two = '2'
    three = '3'
    four = '4'
    five = '5'
    six = '6'
    seven = '7'
    eight = '8'
    nine = '9'
    
button_1 = tk.Button(master=frame, text='1', padx=15, font=myFont, bg="lightgrey", fg="black",
                     pady=5, width=2, command=lambda: myclick(Number.one))
button_1.grid(row=1, column=0, pady=10, padx=10)

button_2 = tk.Button(master=frame, text='2', padx=15, font=myFont, bg="lightgrey", fg="black",
                     pady=5, width=2, command=lambda: myclick(Number.two))
button_2.grid(row=1, column=1, pady=10, padx=10)

button_3 = tk.Button(master=frame, text='3', padx=15, font=myFont, bg="lightgrey", fg="black",
                     pady=5, width=2, command=lambda: myclick(Number.three))
button_3.grid(row=1, column=2, pady=10, padx=10)

button_add = tk.Button(master=frame, text="+", padx=15, font=myFont, bg="lightgrey", fg="black",
                       pady=5, width=2, command=lambda: myclick('+'))
button_add.grid(row=1, column=3, pady=10, padx=10)

button_4 = tk.Button(master=frame, text='4', padx=15, font=myFont, bg="lightgrey", fg="black",
                     pady=5, width=2, command=lambda: myclick(Number.four))
button_4.grid(row=2, column=0, pady=10, padx=10)

button_5 = tk.Button(master=frame, text='5', padx=15, font=myFont, bg="lightgrey", fg="black",
                     pady=5, width=2, command=lambda: myclick(Number.five))
button_5.grid(row=2, column=1, pady=10, padx=10)

button_6 = tk.Button(master=frame, text='6', padx=15, font=myFont, bg="lightgrey", fg="black",
                     pady=5, width=2, command=lambda: myclick(Number.six))
button_6.grid(row=2, column=2, pady=10, padx=10)

button_subtract = tk.Button( master=frame, text="-", padx=15, font=myFont, bg="lightgrey", fg="black",
                     pady=5, width=2, command=lambda: myclick('-'))
button_subtract.grid(row=2, column=3, pady=10, padx=10)

button_7 = tk.Button(master=frame, text='7', padx=15, font=myFont, bg="lightgrey", fg="black",
                     pady=5, width=2, command=lambda: myclick(Number.seven))
button_7.grid(row=3, column=0, pady=10, padx=10)

button_8 = tk.Button(master=frame, text='8', padx=15, font=myFont, bg="lightgrey", fg="black",
                     pady=5, width=2, command=lambda: myclick(Number.eight))
button_8.grid(row=3, column=1, pady=10, padx=10)

button_9 = tk.Button(master=frame, text='9', padx=15, font=myFont, bg="lightgrey", fg="black",
                     pady=5, width=2, command=lambda: myclick(Number.nine))
button_9.grid(row=3, column=2, pady=10, padx=10)

button_multiply = tk.Button(master=frame, text="*", padx=15, font=myFont, bg="lightgrey", fg="black",
                     pady=5, width=2, command=lambda: myclick('*'))
button_multiply.grid(row=3, column=3, pady=10, padx=10)

button_leftbracket = tk.Button(master=frame, text="(", padx=15, font=myFont, bg="lightgrey", fg="black",
                     pady=5, width=2, command=lambda: myclick('('))
button_leftbracket.grid(row=4, column=0, pady=10, padx=10)
 
button_0 = tk.Button(master=frame, text='0', padx=15, font=myFont, bg="lightgrey", fg="black",
                     pady=5, width=2, command=lambda: myclick(Number.zero))
button_0.grid(row=4, column=1, pady=10, padx=10)

button_rightbracket = tk.Button(master=frame, text=")", padx=15, font=myFont, bg="lightgrey", fg="black",
                     pady=5, width=2, command=lambda: myclick(')'))
button_rightbracket.grid(row=4, column=2, pady=10, padx=10)

button_div = tk.Button(master=frame, text="/", padx=15, font=myFont, bg="lightgrey", fg="black",
                     pady=5, width=2, command=lambda: myclick('/'))
button_div.grid(row=4, column=3, pady=10, padx=10)

button_dot = tk.Button(master=frame, text=".", padx=15, font=myFont, bg="lightgrey", fg="black",
                     pady=5, width=2, command=lambda: myclick('.'))
button_dot.grid(row=5, column=0, pady=10, padx=10)

button_div0 = tk.Button(master=frame, text="div", padx=15, font=myFont, bg="lightgrey", fg="black",
                     pady=5, width=2, command=lambda: myclick('//'))
button_div0.grid(row=5, column=1, pady=10, padx=10)

button_mod = tk.Button(master=frame, text="mod", padx=15, font=myFont, bg="lightgrey", fg="black",
                     pady=5, width=2, command=lambda: myclick('%'))
button_mod.grid(row=5, column=2, pady=10, padx=10)

button_exp = tk.Button(master=frame, text="^", padx=15, font=myFont, bg="lightgrey", fg="black",
                     pady=5, width=2, command=lambda: myclick('**'))
button_exp.grid(row=5, column=3, pady=10, padx=10)

button_bin = tk.Button(master=frame, text="bin", padx=15, font=myFont, bg="lightgrey", fg="black",
                     pady=5, width=2, command=decimal_2_bin)
button_bin.grid(row=6, column=0, pady=10, padx=10)

button_oct = tk.Button(master=frame, text="oct", padx=15, font=myFont, bg="lightgrey", fg="black",
                     pady=5, width=2, command=decimal_2_bin)
button_oct.grid(row=6, column=1, pady=10, padx=10)

button_hex = tk.Button(master=frame, text="hex", padx=15, font=myFont, bg="lightgrey", fg="black",
                     pady=5, width=2, command=decimal_2_bin)
button_hex.grid(row=6, column=2, pady=10, padx=10)

button_sqrt = tk.Button(master=frame, text="sqrt", padx=15, font=myFont, bg="lightgrey", fg="black",
                     pady=5, width=2, command=sqrt)
button_sqrt.grid(row=6, column=3, pady=10, padx=10)

button_bin = tk.Button(master=frame, text="bin", padx=15, font=myFont, bg="lightgrey", fg="black",
                     pady=5, width=2, command=decimal_2_bin)
button_bin.grid(row=6, column=0, pady=10, padx=10)

button_oct = tk.Button(master=frame, text="oct", padx=15, font=myFont, bg="lightgrey", fg="black",
                     pady=5, width=2, command=decimal_2_bin)
button_oct.grid(row=6, column=1, pady=10, padx=10)

button_hex = tk.Button(master=frame, text="hex", padx=15, font=myFont, bg="lightgrey", fg="black",
                     pady=5, width=2, command=decimal_2_bin)
button_hex.grid(row=6, column=2, pady=10, padx=10)

button_sqrt = tk.Button(master=frame, text="sqrt", padx=15, font=myFont, bg="lightgrey", fg="black",
                     pady=5, width=2, command=sqrt)
button_sqrt.grid(row=6, column=3, pady=10, padx=10)

button_allclear = tk.Button(master=frame, text="AC", padx=15, font=myFont, bg="lightgrey", fg="black",
                     pady=5, width=2, command=allclear)
button_allclear.grid(row=7, column=0, pady=10, padx=10)

button_clear = tk.Button(master=frame, text="C", padx=15, font=myFont, bg="lightgrey", fg="black",
                     pady=5, width=2, command=clear)
button_clear.grid(row=7, column=1, pady=10, padx=10)

button_equal = tk.Button(master=frame, text="=", padx=15, font=myFont, bg="lightgrey", fg="black",
                     pady=5, width=8, command=decimal_2_bin)
button_equal.grid(row=7, column=2, columnspan=2, pady=10, padx=10)
 
window.mainloop()