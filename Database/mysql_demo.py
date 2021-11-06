import mysql.connector


db = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='tan',
    database='team'
)


print(db.is_connected())
my_cursor = db.cursor()

#my_cursor.execute("CREATE DATABASE team")

#my_cursor.execute("CREATE TABLE player(name VARCHAR(50))")
my_cursor.execute("DESCRIBE player")


for x in my_cursor:
    print(x)