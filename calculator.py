import tkinter as tk
from tkinter import messagebox

mainWindow=tk.Tk()
mainWindow.title("Calculator")

first_label=tk.Label(mainWindow,text="First Number")
first_label.pack()

number1=tk.Entry(mainWindow)
number1.pack()

second_label=tk.Label(mainWindow,text="Second Number")
second_label.pack()

number2=tk.Entry(mainWindow)
number2.pack()

def addition():
    n1,n2=takeValueInput()
    result=n1+n2
    result_label.config(text="Operations result is: " +
                             str(result))

def substraction():
    n1,n2=takeValueInput()
    result=n1-n2
    result_label.config(text="Operations result is: " +
                             str(result))


def multiplication():
    n1,n2=takeValueInput()
    result=n1*n2
    result_label.config(text="Operations result is: " +
                             str(result))


def division():
    n1,n2=takeValueInput()
    if n2==0:
        messagebox.showerror("Error", "Cannot divide the value by 0.")
    else:
        result=n1/n2
        result_label.config(text="Operations result is: " +
                             str(result))

def takeValueInput():
    n1 = number1.get()
    n2 = number2.get()

    try:
        n1 = int(n1)
        n2 = int(n2)

        return n1, n2
    except ValueError:
        if ((len(number1.get()) == 0) or (len(number2.get()) == 0)):
            messagebox.showerror("Error", "Please enter a value")
        else:
            messagebox.showerror("Error", "Enter only integer value")
        quit(0)


button1=tk.Button(mainWindow,text="+",command=lambda:addition())
button1.pack()

button2=tk.Button(mainWindow,text="-",command=lambda:substraction())
button2.pack()

button3=tk.Button(mainWindow,text="*",command=lambda:multiplication())
button3.pack()

button4=tk.Button(mainWindow,text="/",command=lambda:division())
button4.pack()

result_label = tk.Label(mainWindow, text="Operations result is:")
result_label.pack()

mainWindow.mainloop()
