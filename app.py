import sqlite3

db = sqlite3.connect("assesment.db")
cursor = db.cursor()
sql = "SELECT * from shoes;"
cursor.execute(sql)
results = cursor.fetchall()
print(results)
db.close()