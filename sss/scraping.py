"""Module for scraping of the puzzle and solving the scraped puzzle"""
from copy import deepcopy
from bs4 import BeautifulSoup
import requests


def scrape():
    """Function scrapes the sudoku and returns in like a matrix"""
    url = "http://nine.websudoku.com/?"

    result = requests.get(url)
    doc = BeautifulSoup(result.text, "html.parser")

    input_fields = doc.findAll("input")

    puzzle = []
    index = 0

    for i in range(9):
        puzzle.append([])
        for _ in range(9):
            if input_fields[index].attrs.get('value') is not None:
                puzzle[i].append(int(input_fields[index].attrs['value']))
            else:
                puzzle[i].append(0)
            index += 1

    return puzzle


def find_next_empty(puzzle):
    """Function finds the next 0 in the puzzle"""
    for i in range(9):
        for j in range(9):
            if puzzle[i][j] == 0:
                return i, j

    return None, None


def is_valid(puzzle, guess, row, col):
    """Function checks if a number can be inserted in that position"""
    row_vals = puzzle[row]
    if guess in row_vals:
        return False

    col_vals = [puzzle[i][col] for i in range(9)]
    if guess in col_vals:
        return False

    row_start = (row // 3) * 3
    col_start = (col // 3) * 3

    for i in range(row_start, row_start + 3):
        for j in range(col_start, col_start + 3):
            if puzzle[i][j] == guess:
                return False

    return True


def solve_sudoku(puzzle):
    """Function solves the puzzle and returns it"""
    row, col = find_next_empty(puzzle)

    if row is None:
        return puzzle

    for guess in range(1, 10):
        if is_valid(puzzle, guess, row, col):
            puzzle[row][col] = guess
            if solve_sudoku(puzzle):
                return puzzle

        puzzle[row][col] = 0

    return False


sudoku = scrape()
temp = deepcopy(sudoku)
solved = solve_sudoku(temp)

print(solved)
