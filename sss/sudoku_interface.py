"""In this module is code for interface and all it's functions"""
from tkinter import Entry, Tk, Label, Button

root = Tk()
root.title("Sudoku")
root.resizable(False, False)

game_title = Label(root, text="Fill in the fields with right numbers.")
game_title.grid(row=0, column=1, columnspan=10, pady=5)


def validate(key_input):
    """Check if user input is a number with one digit"""
    out = (key_input.isdigit() or key_input == "") and len(key_input) < 2
    return out


rule = root.register(validate)
cells = {}


def draw9x9():
    """Function makes the game board with entry fields"""
    for i in range(9):
        for j in range(9):
            entry = Entry(root, width=5, bg="#D0ffff", justify="center", validate="key",
                          validatecommand=(rule, "%P"))
            entry.grid(row=i + 1, column=j + 1,
                       sticky="nsew", padx=1, pady=1, ipady=5)
            cells[(i, j)] = entry


draw9x9()

clear_button = Button(text="Clear", width=10)
clear_button.grid(row=15, column=1, columnspan=5, pady=20)

solve_button = Button(text="Solve", width=10)
solve_button.grid(row=15, column=5, columnspan=5, pady=20)


def show_btns():
    """Function inserts buttons for number input"""
    for i in range(1, 10):
        num_button = Button(root, text=i)
        num_button.grid(row=20, column=i, sticky="nsew",
                        padx=1, pady=1, ipady=5)


show_btns()

root.mainloop()
