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

sql_create_table_sleep = 'CREATE TABLE sleepindex(sleep_index TEXT);'
cur.execute(sql_create_table_sleep)

con.close()