import sqlite3

#Connect to a databse
dbase = sqlite3.connect("dbtest.db")

#Get the cursor/pointer to the database
cursor = dbase.cursor()

#Create a table

'''
cursor.execute("""CREATE TABLE customers(
                  name text,
                  email text,
                  age integer
                )""")

'''
#cursor.execute("INSERT INTO customers VALUES('Raj','raj@google.com',20)")
#cursor.execute("INSERT INTO customers VALUES('Rohit','rohit@google.com',30)")
#cursor.execute("INSERT INTO customers (name, email,age) VALUES ('Chuck', 'csev@umich.edu',30)")
#cursor.execute("INSERT INTO customers (name, email,age) VALUES ('Colleen', 'cvl@umich.edu',35)")
#cursor.execute("INSERT INTO customers (name, email,age) VALUES ('Ted', 'ted@umich.edu',40)")
#cursor.execute("INSERT INTO customers (name, email,age) VALUES ('Sally', 'a1@umich.edu',45)")
#cursor.execute("INSERT INTO customers (name, email,age) VALUES ('Ted', 'ted@umich.edu',50)")
#cursor.execute("INSERT INTO customers (name, email,age) VALUES ('Kristen', 'kf@umich.edu',55)")

#cursor.execute("DELETE FROM customers WHERE email='ted@umich.edu' ")

#cursor.execute("UPDATE customers SET name= 'Charles' WHERE email='csev@umich.edu' ")

#cursor.execute("SELECT * FROM customers")
#cursor.execute("SELECT * FROM customers ORDER BY email")

cursor.execute("SELECT * FROM customers ORDER BY name DESC")
items = cursor.fetchall()

for item in items:
    print(item)

print()
for item in items:
    print(item[0] + " " + item[1])

print()
for item in items:
    print(item[0] + " " + item[1] + " = " + str(item[2]))


dbase.commit()

dbase.close()