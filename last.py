from bs4 import BeautifulSoup
import requests
import time

url = 'https://tenki.jp/indexes/sleep/3/15/4510/12227/#google_vignette'
r = requests.get(url)

html_soup = BeautifulSoup(r.text, "html.parser")
city_day = html_soup.find_all('td', class_ = 'cityday').text.strip()
for i in range(len(city_day)):
    time.sleep(2)
    city_day_data = city_day[i].tezt.strip()

wheather_index1 = html_soup.find_all('span', class_='indexes-telop-0')
for i in range(len(wheather_index1)):
    time.sleep(2)
    wheather_index1_data = wheather_index1[i].tezt.strip()

wheather_index2 = html_soup.find_all('p', class_ = 'indexes-telop-0')
for i in range(len(wheather_index2)):
    time.sleep(2)
    wheather_index2_data = wheather_index2[i].tezt.strip()