#This program will create a simple GUI calculator
import random
import tkinter as tk
from tkinter import *

#Optional Create a versatile look to the GUI
#declare variables
expression = ""
button_colors = ['#00FFFF', '#98F5FF', '#FF6103', '#C1FFC1', '#808080',
               '#FF1493', '#FF3030', '#7CFC00', '#FFE1FF', ]

#create window
root = tk.Tk()
root.title("Calculator by Daniel")
root.geometry("175x300")


#functions


def clear():
    entry_result.delete(0, END)

def delete():

    current_task = entry_result.get()
    entry_result.delete(0, END)
    entry_result.insert(END,current_task[:-1])

def calculate():

    try:

        expression = entry_result.get()
        result = eval(expression)
        entry_result.delete(0, END)
        entry_result.insert(END, str(result))

    except Exception:
        entry_result.delete(0, END)
        entry_result.insert(END, "Error")


def exit():
    root.destroy()

#Create GUI with tkinter widgets
entry_result = tk.Entry(root, bg='gray', )
entry_result.grid(row=0, column=0, columnspan=4, padx=20, pady=5,)

#numberButtons
button_7 = tk.Button(root, width=4, height=2 ,text="7",
                     bg=random.choice(button_colors),
                     command=lambda : entry_result.insert(END,"7"))
button_7.grid(row=1, column=0)

button_8 = tk.Button(root, width=4, height=2 , text="8",
                     bg=random.choice(button_colors),
                     command=lambda :entry_result.insert(END,"8"))
button_8.grid(row=1, column=1)

button_9 = tk.Button(root, width=4, height=2 , text="9",
                     bg=random.choice(button_colors),
                     command=lambda : entry_result.insert(END,"9"))
button_9.grid(row=1, column=2)

button_plus = tk.Button(root, width=4, height=2 , text="+",
                        bg=random.choice(button_colors),
                        command=lambda : entry_result.insert(END,"+"))
button_plus.grid(row=1, column=3)

button_6 = tk.Button(root, width=4, height=2 , text="4",
                     bg=random.choice(button_colors),
                     command= lambda :entry_result.insert(END,"4"))
button_6.grid(row=2, column=0)

button_5 = tk.Button(root, width=4, height=2 , text="5",
                     bg=random.choice(button_colors),
                     command=lambda : entry_result.insert(END,"5"))
button_5.grid(row=2, column=1)

button_4 = tk.Button(root, width=4, height=2 , text="6",
                     bg=random.choice(button_colors),
                     command=lambda : entry_result.insert(END,"6"))
button_4.grid(row=2, column=2)

button_minus = tk.Button(root,width=4, height=2 , text="-",
                         bg=random.choice(button_colors)
                         ,command=lambda : entry_result.insert(END,"-"))
button_minus.grid(row=2, column=3)


button_1 = tk.Button(root,width=4, height=2 ,text="1",
                     bg=random.choice(button_colors),
                     command=lambda : entry_result.insert(END,"1"))
button_1.grid(row=3, column=0)

button_2 = tk.Button(root, width=4, height=2 , text="2",
                     bg=random.choice(button_colors),
                     command=lambda : entry_result.insert(END,"2"))
button_2.grid(row=3, column=1)

button_3 = tk.Button(root, width=4, height=2 , text="3",
                     bg=random.choice(button_colors),
                     command=lambda : entry_result.insert(END,"3"))
button_3.grid(row=3, column=2)

button_multiply = tk.Button(root, width=4, height=2 , text="*",
                            bg=random.choice(button_colors),
                            command=lambda : entry_result.insert(END,"*"))
button_multiply.grid(row=3, column=3)


button_0 = tk.Button(root, width=4, height=2 , text="0",
                     bg=random.choice(button_colors),
                     command=lambda : entry_result.insert(END,"0"))
button_0.grid(row=4, column=0)

button_clear = tk.Button(root, width=4, height=2 , text="C",
                         bg=random.choice(button_colors),
                         command= clear)
button_clear.grid(row=4, column=1)

button_delete = tk.Button(root, width=4, height=2 , text="De.",
                          bg=random.choice(button_colors),
                          command=lambda : delete())
button_delete.grid(row=4, column=2)

button_divide = tk.Button(root, width=4, height=2 , text="/",
                          bg=random.choice(button_colors),
                          command=lambda : entry_result.insert(END, "/"))
button_divide.grid(row=4, column=3)

button_exit = tk.Button(root, width=4, height=2 , text="Exit",
                        bg=random.choice(button_colors), command=exit)
button_exit.grid(row=5,column=1)

button_equals = tk.Button(root, width=4, height=2, text="=",
                          bg=random.choice(button_colors),
                          command=lambda : calculate())
button_equals.grid(row=5, column=2)

root.mainloop()