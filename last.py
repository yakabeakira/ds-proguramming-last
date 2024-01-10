import sqlite3
path = '/Users/yakabe/hasegawa/last12/ds-proguramming-last/'
db_name = 'wheatherindex.sqlite'
con = sqlite3.connect(path + db_name)
con.close()