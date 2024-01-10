from bs4 import BeautifulSoup
import requests
url = 'https://tenki.jp/indexes/sleep/3/15/4510/12227/#google_vignette'
r = requests.get(url)
import time
html_soup = BeautifulSoup(r.text, "html.parser")