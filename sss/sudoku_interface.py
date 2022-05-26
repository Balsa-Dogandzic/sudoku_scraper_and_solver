"""In this module is code for interface and all it's functions"""
from tkinter import Entry, Tk, Label

root = Tk()
root.title("Sudoku")
root.resizable(False, False)

game_title = Label(root, text="Fill in the fields with right numbers.")
game_title.grid(row=0, column=1, columnspan=10)


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

root.mainloop()
