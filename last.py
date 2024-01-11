#必要なモジュールを全てインポート
import sqlite3
from bs4 import BeautifulSoup
import requests
import time

#DBファイルを保存するためのパスを作成
path = '/Users/yakabe/hasegawa/last12/ds-proguramming-last/'
#DBファイル名
db_name = 'sleepindex.sqlite'
con = sqlite3.connect(path + db_name)
con.close()

#テーブル作成
con = sqlite3.connect(path + db_name)

cur = con.cursor()

sql_create_table_weather = 'CREATE TABLE sleepindex(sleep_index text);'
cur.execute(sql_create_table_weather)

con.close()


#データをDBに挿入する(スクレイピング)
con = sqlite3.connect(path + db_name)

cur = con.cursor()

#スクレイピング先のurlを取得
url = 'https://tenki.jp/indexes/sleep/3/15/4510/12227/'
r = requests.get(url)

#HTMLソースをBeautifulSoupオブジェクトに変換する
html_soup = BeautifulSoup(r.text, "html.parser")

#睡眠指数のタグを取得
sleep_indexes= html_soup.find_all('p', class_='indexes-telop-0')

cur.executemany("INSERT INTO sleepindex (sleep_indexes) VALUES(?);")

#timeモジュールで負荷軽減
time.sleep(1)

#コミット処理（データ操作を反映させる）
con.commit()
con.close()
