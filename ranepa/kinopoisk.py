import urllib.parse

import response as response
from bs4 import BeautifulSoup
import requests
import pandas as pd

with open('token.txt') as token_file:
    token = token_file.read()

req = requests.get("https://www.kinopoisk.ru/lists/movies/top250/?page=2/token/{}".format(
    token
), params={} )
film_info = req.json()
print(film_info)

