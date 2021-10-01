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
#cursor.execute("INSERT INTO customers (name, email,age) VALUES ('rohan', 'rohan@google.com',30)")
#cursor.execute("INSERT INTO customers (name, email,age) VALUES ('rinki', 'rinki@google.com',35)")
#cursor.execute("INSERT INTO customers (name, email,age) VALUES ('raju', 'raju@google.com',40)")
#cursor.execute("INSERT INTO customers (name, email,age) VALUES ('pinky', 'kf@umich.edu',55)")

#cursor.execute("DELETE FROM customers WHERE email='rohan@google.com' ")

#cursor.execute("UPDATE customers SET name= 'Rocket' WHERE email='raju@google.com' ")
#cursor.execute("UPDATE customers SET email= 'rock@rocket.com' WHERE name='Rocket' ")

#cursor.execute("SELECT * FROM customers")
#cursor.execute("SELECT * FROM customers ORDER BY email")

cursor.execute("SELECT * FROM customers ORDER BY name DESC")    #Records will be sorted in descending order
items = cursor.fetchall()                                       #Creates a list of tuples
#print(type(items))
#print(dir(cursor))

print(len(items))

for item in items:
    print(item)             #Print all tuples in the database

print()
for item in items:
    print(item[0] + " " + item[1])          #Print only specific tuples

print()
for item in items:
    print(item[0] + " " + item[1] + " = " + str(item[2]))


dbase.commit()              #This is imporatnt to write changes to database

#dbase.close()

print("==============================================")

#Creating a new table in the same database

'''
cursor.execute("""CREATE TABLE Users(
                  name text,
                  hobbies text
                )""")
'''
#Fetching the data that is being input from sqlite browser

cursor.execute("SELECT * FROM Users")
items = cursor.fetchall()

for item in items:
    print(item)

dbase.close()        #CLosing the database here after opertaions with both tables