#必要なモジュールを全てインポート
import sqlite3
from bs4 import BeautifulSoup
import requeｓts
import time
path = '/Users/yakabe/hasegawa/last12/ds-proguramming-last/'


#urlを取得する
url = 'https://tenki.jp/indexes/sleep/3/15/4510/12227/'
r = requests.get(url)
html_soup = BeautifulSoup(r.text, "html.parser")

#タグからデータを抽出（スクレイピング）
city_day = html_soup.find_all('td', class_ = 'cityday')
#timeモジュールで負荷軽減
for i in range(len(city_day)):
    time.sleep(2)
wheather_index1 = html_soup.find_all('span', class_='indexes-telop-0')
#timeモジュールで負荷軽減
for i in range(len(wheather_index1)):
    time.sleep(2)
wheather_index2 = html_soup.find_all('p', class_ = 'indexes-telop-0')
#timeモジュールで負荷軽減
for i in range(len(wheather_index2)):
    time.sleep(2)

