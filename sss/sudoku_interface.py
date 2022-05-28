"""In this module is code for interface and all it's functions"""
from tkinter import Entry, Tk, Label, Button, END
from scraping import sudoku, solved

root = Tk()
root.title("Sudoku")
root.iconbitmap("static\\sudoku_picture.ico")
root.resizable(False, False)

game_title = Label(root, text="Fill in the fields with right numbers.")
game_title.grid(row=0, column=1, columnspan=10, pady=5)


def validate(key_input):
    """Check if user input is a number with one digit"""
    out = (key_input.isdigit() or key_input == "") and len(
        key_input) < 2 and key_input != 0
    return out


rule = root.register(validate)
cells = {}


def draw9x9():
    """Function makes the game board with entry fields"""
    for i in range(9):
        for j in range(9):
            entry = Entry(root, width=5, bg="#D0ffff", justify="center", validate="key",
                          validatecommand=(rule, "%P"))
            entry.bind("<KeyRelease>", lambda event: check_input())
            entry.grid(row=i + 1, column=j + 1,
                       sticky="nsew", padx=1, pady=1, ipady=5)
            cells[(i, j)] = entry


def fill_the_fields(puzzle):
    """Function fills the board with the result of scraping"""
    for i in range(9):
        for j in range(9):
            if puzzle[i][j] != 0:
                cells[(i, j)].delete(0, END)
                cells[(i, j)].insert(0, puzzle[i][j])
                cells[(i, j)].configure(state="disabled")


draw9x9()
fill_the_fields(sudoku)

clear_button = Button(text="Clear", width=10,
                      command=lambda: write_number("del"))
clear_button.grid(row=15, column=1, columnspan=5, pady=20)


def write_automatic_solution():
    "Function writes the solution in the text file"
    with open("db\\automatic_result_time.txt", "w", encoding="utf-8") as file:
        for i in range(9):
            file.write(str(solved[i]) + "\n")


solve_button = Button(text="Solve", width=10, command=write_automatic_solution)
solve_button.grid(row=15, column=5, columnspan=5, pady=20)


def check_input():
    """Checks if input number is equal to the one in solved puzzle"""
    for i in range(9):
        for j in range(9):
            if cells[(i, j)] != 0:
                if '1' <= cells[(i, j)].get() <= '9':
                    sudoku[i][j] = int(cells[(i, j)].get())
                    if sudoku[i][j] != solved[i][j]:
                        cells[(i, j)].configure(bg="#FF7659")
                    else:
                        cells[(i, j)].configure(bg="#D0ffff")
    if endgame():
        print("endgame")


def write_number(argument):
    """Functions enables buttons to write numbers on the board"""
    try:
        focused_entry = root.focus_get()
        focused_entry.delete(0, END)
        if argument != "del":
            focused_entry.insert(0, argument)
        check_input()
        game_title.configure(text="Fill in the fields with right numbers.")
    except AttributeError:
        game_title.configure(text="Focus the field first")


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


def endgame():
    """Checks if all the fields are correctly filled"""
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] != solved[i][j]:
                return False

    return True


show_btns()

root.mainloop()
