import sqlite3
from bs4 import BeautifulSoup
import requeｓts
path = '/Users/yakabe/hasegawa/last12/ds-proguramming-last/'

#DBファイルを保存するためのファイルパス
db_name = 'wheatherindex.sqlite'
con = sqlite3.connect(path + db_name)
con.close()

#テーブルを作成
con = sqlite3.connect(path + db_name)
cur = con.cursor()
#テーブルにカラムを作成
sql_create_table_wheatherindex = 'CREATE TABLE wheather_index(cityday TEXT, wheatherindex TEXT, good_sleep_score FLOAT);'
cur.execute(sql_create_table_wheatherindex)
con.close()

