import tkinter as tk

root = tk.Tk()
root.title("Calculator")
root.geometry("470x600+420+570")
root.resizable(False, False)
root.configure(bg="#262626")

# Labels
label_text = tk.Label(root, width=100, height=1, bg="#D0CED0", text="Basic Calculator", font=("Times New Roman", 20, "bold"), justify="left")
label_result = tk.Label(root, width=80, height=2, text="", bg="#D0CED0", font=("Times New Roman", 40), anchor="e")
label_text.pack()
label_result.pack()

# Global Equation Variable
equation = ""

# Functions
def show(value):
    global equation
    equation += value
    label_result.config(text=equation)

def clear():
    global equation
    equation = ""
    label_result.config(text=equation)

def calculate():
    global equation
    try:
        result = eval(equation)  # Unsafe in general; ensure the input is trusted.
        label_result.config(text=result)
        equation = str(result)
    except:
        label_result.config(text="error")
        equation = ""

def backspace():
    global equation
    equation = equation[:-1]
    label_result.config(text=equation)

# Button Parameters
button_config = {
    "width": 5,
    "height": 1,
    "font": ("Times New Roman", 20, "bold"),
    "fg": "#FFFFFF",
    "bg": "#333333"
}

# Button Layout
buttons = [
    ["%", "**2", "C", "Back"],
    ["1/x", "(", ")", "/"],
    ["7", "8", "9", "*"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    [" ", "0", ".", "="]
]

commands = {
    "%": lambda: show("%"),
    "**2": lambda: show("**2"),
    "C": clear,
    "Back": backspace,
    "1/x": lambda: show("1/"),
    "(": lambda: show("("),
    ")": lambda: show(")"),
    "/": lambda: show("/"),
    "*": lambda: show("*"),
    "-": lambda: show("-"),
    "+": lambda: show("+"),
    "=": calculate,
    ".": lambda: show("."),
    "0": lambda: show("0"),
    " ": None
}

# Create Buttons Dynamically
for i, row in enumerate(buttons):
    for j, text in enumerate(row):
        command = commands.get(text, lambda t=text: show(t))
        btn = tk.Button(root, text=text, command=command, **button_config)
        btn.place(x=20 + j * 110, y=180 + i * 70)

root.mainloop()