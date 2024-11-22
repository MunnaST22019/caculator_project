import tkinter as tk

# Function to evaluate the expression
def evaluate_expression(expression):
    try:
        result = str(eval(expression))
        entry_var.set(result)
    except Exception as e:
        entry_var.set("Error")

# Function to update the current expression
def update_expression(value):
    current = entry_var.get()
    entry_var.set(current + value)

# Function to clear the expression
def clear_expression():
    entry_var.set("")

# Create the main window
root = tk.Tk()
root.title("Calculator")

# Variable to hold the expression
entry_var = tk.StringVar()

# Entry widget to display the expression/result
entry = tk.Entry(root, textvariable=entry_var, font=("Arial", 20), bd=10, relief="sunken", justify="right")
entry.grid(row=0, column=0, columnspan=4)

# Buttons for numbers and operations
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3)
]

# Create and place buttons on the grid
for (text, row, col) in buttons:
    if text == "=":
        # Equals button evaluates the expression
        button = tk.Button(root, text=text, font=("Arial", 20), width=5, height=2, command=lambda: evaluate_expression(entry_var.get()))
    else:
        # All other buttons just update the expression
        button = tk.Button(root, text=text, font=("Arial", 20), width=5, height=2, command=lambda value=text: update_expression(value))
    button.grid(row=row, column=col)

# Clear button
clear_button = tk.Button(root, text="C", font=("Arial", 20), width=5, height=2, command=clear_expression)
clear_button.grid(row=5, column=0)

# Start the GUI event loop
root.mainloop()
