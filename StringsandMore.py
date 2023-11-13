import tkinter as tk


def perform_operations():
    user_input = entry.get()
    concatenated = "Prefix " + user_input
    words = user_input.split(" ")
    joined = "_".join(words)
    upper_case = user_input.upper()
    lower_case = user_input.lower()
    length = len(user_input)

    result_label.config(
        text=f"Concatenated: {concatenated}\nWords: {words}\nJoined: {joined}\nUpper Case: {upper_case}\nLower Case: {lower_case}\nLength: {length}")


# Initialize Tkinter window
root = tk.Tk()
root.title("String Operations")
root.geometry("300x300")

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Perform Operations", command=perform_operations)
button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()