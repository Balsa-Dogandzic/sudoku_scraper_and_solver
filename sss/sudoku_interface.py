"""In this module is code for interface and all it's functions"""
from tkinter import Entry, Tk, Label, Button, END

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

clear_button = Button(text="Clear", width=10,
                      command=lambda: write_number("del"))
clear_button.grid(row=15, column=1, columnspan=5, pady=20)

solve_button = Button(text="Solve", width=10)
solve_button.grid(row=15, column=5, columnspan=5, pady=20)


def write_number(argument):
    """Functions enables buttons to write numbers on the board"""
    focused_entry = root.focus_get()
    focused_entry.delete(0, END)
    if argument != "del":
        focused_entry.insert(0, argument)


def show_btns():
    """Function inserts buttons for number input"""
    buttons = []
    for i in range(1, 10):
        num_button = Button(root, text=i)
        num_button.grid(row=20, column=i, sticky="nsew",
                        padx=1, pady=1, ipady=5)
        buttons.append(num_button)
    buttons[0].configure(command=lambda: write_number(1))
    buttons[1].configure(command=lambda: write_number(2))
    buttons[2].configure(command=lambda: write_number(3))
    buttons[3].configure(command=lambda: write_number(4))
    buttons[4].configure(command=lambda: write_number(5))
    buttons[5].configure(command=lambda: write_number(6))
    buttons[6].configure(command=lambda: write_number(7))
    buttons[7].configure(command=lambda: write_number(8))
    buttons[8].configure(command=lambda: write_number(9))


show_btns()

root.mainloop()
