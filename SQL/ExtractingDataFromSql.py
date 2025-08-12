import mysql.connector

connection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "12345612",
    database = "ecommerce"
)

cursor = connection.cursor()

query1 = "desc customers"

cursor.execute(query1)

table = cursor.fetchall()

print('\n Table Description : ')
for attr in table:
    print(attr)


query2 = "select * from customers"


cursor.execute(query2)

table = cursor.fetchall()

print('\n Table Data:')
for row in table:
    print(row[0], end=" ")
    print(row[1], end=" ")
    print(row[2], end="\n")


cursor.close()

connection.close()