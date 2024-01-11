#必要なモジュールを全てインポート
import sqlite3
from bs4 import BeautifulSoup
import requeｓts
import time

#DBファイルを保存するためのパスを作成
path = '/Users/yakabe/hasegawa/last12/ds-proguramming-last/'
#DBファイル名
db_name = 'weather.sqlite'
con = sqlite3.connect(path + db_name)
con.close()


