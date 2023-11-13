import tkinter as tk

def on_button_click(value):
    print(f"Button {value} clicked!")

# Initialize Tkinter window
root = tk.Tk()
root.title("Simple Calculator")

# Create Entry widget
entry = tk.Entry(root, width=20)
entry.grid(row=0, columnspan=4)

# Create buttons
buttons = [
    '7', '8', '9', '+',
    '4', '5', '6', '-',
    '1', '2', '3', '*',
    'C', '0', '=', '/'
]

row_val = 1
col_val = 0

for button in buttons:
    tk.Button(root, text=button, width=5, height=2, command=lambda b=button: on_button_click(b)).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Run the Tkinter event loop
root.mainloop()