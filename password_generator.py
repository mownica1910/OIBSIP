import tkinter as tk
import random
import string

def generate_password():
    try:
        length = int(entry_length.get())

        characters = ""

        if var_letters.get():
            characters += string.ascii_letters
        if var_numbers.get():
            characters += string.digits
        if var_symbols.get():
            characters += string.punctuation

        if length <= 0:
            result_label.config(text="Enter valid length!")
            return

        if characters == "":
            result_label.config(text="Select at least one option!")
            return

        password = ""
        for i in range(length):
            password += random.choice(characters)

        result_label.config(text=password)

    except:
        result_label.config(text="Invalid input!")
root = tk.Tk()
root.title("Password Generator")
root.geometry("350x300")
tk.Label(root, text="Random Password Generator", font=("Arial", 12, "bold")).pack(pady=10)
tk.Label(root, text="Password Length").pack()
entry_length = tk.Entry(root)
entry_length.pack()
var_letters = tk.IntVar()
var_numbers = tk.IntVar()
var_symbols = tk.IntVar()
tk.Checkbutton(root, text="Include Letters", variable=var_letters).pack()
tk.Checkbutton(root, text="Include Numbers", variable=var_numbers).pack()
tk.Checkbutton(root, text="Include Symbols", variable=var_symbols).pack()
tk.Button(root, text="Generate Password", command=generate_password).pack(pady=10)
result_label = tk.Label(root, text="", fg="blue", wraplength=300)
result_label.pack(pady=10)
root.mainloop()