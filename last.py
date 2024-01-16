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

for sleep_index in sleep_indexes:
  cur.execute("INSERT INTO sleepindex (sleep_index) VALUES(?);", (sleep_index.text.strip(),))
  #timeモジュールで負荷軽減
  time.sleep(1)

#コミット処理（データ操作を反映させる）
con.commit()
con.close()


#テーブルのデータ参照用
con = sqlite3.connect(path + db_name)

cur = con.cursor()

sql_select = 'SELECT * FROM sleepindex;'

cur.execute(sql_select)
for r in cur:
  print(r)

con.close()



#ローカルデータの読み込み（データの整理）
import pandas as pd

df = pd.read_csv('/Users/yakabe/hasegawa/last12/ds-proguramming-last/sleep_index.csv', encoding='shift_jis')

# %　を除去
df['睡眠効率'] = df['睡眠効率'].str.replace('%', '')


#データセットのカラムを取捨選択
df = df.drop(columns=['就床時刻', '入眠時刻', '鳴動時刻', '起床時刻', '就床時刻', '入眠潜時'])

#不必要な行を削除
df = df.drop(index=range(5, 11))

#実行確認
print(df)


#必要なモジュールを全てインポート
import sqlite3
from bs4 import BeautifulSoup
import requests
import time

#DBファイルを保存するためのパスを作成
path = '/Users/yakabe/hasegawa/last12/ds-proguramming-last/'
#DBファイル名
db_name = 'SleepScore.sqlite'
con = sqlite3.connect(path + db_name)
con.close()

#ローカルデータ用のテーブル作成
con = sqlite3.connect(path + db_name)

cur = con.cursor()

sql_create_table_sleep_score = 'CREATE TABLE sleepscore(date TEXT, bedtime TEXT, time_of_sleep TEXT, awaking_time TEXT, mid_awaking REAL, snooze REAL, sleep_efficiency REAL, good_sleep_score REAL);'
cur.execute(sql_create_table_sleep_score)

con.close()

#データをDBに挿入する(スクレイピング)
con = sqlite3.connect(path + db_name)

cur = con.cursor()

#データを整理したデータフレームを直接データベースに挿入
df.to_sql('sleepscore', con, index=False, if_exists='replace')


#コミット処理（データ操作を反映させる）
con.commit()
con.close()


#テーブルのデータ参照用
con = sqlite3.connect(path + db_name)

cur = con.cursor()

sql_select = 'SELECT * FROM sleepscore;'

cur.execute(sql_select)
for r in cur:
  print(r)

con.close()
