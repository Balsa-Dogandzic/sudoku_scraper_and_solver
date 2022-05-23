from bs4 import BeautifulSoup
import requests

url = "http://nine.websudoku.com/?"

result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")

print(doc)
