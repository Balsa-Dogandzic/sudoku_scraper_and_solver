"""Module for scraping of the puzzle and solving the scraped puzzle"""
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
        for j in range(9):
            if input_fields[index].attrs.get('value') is not None:
                puzzle[i].append(int(input_fields[index].attrs['value']))
            else:
                puzzle[i].append(0)
            index += 1

    return puzzle


print(scrape())
