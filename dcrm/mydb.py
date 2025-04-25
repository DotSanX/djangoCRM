import mysql.connector

data = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'password123',


)

cursorObject = data.cursor()

#create datbase

cursorObject.execute("CREATE DATABASE elderco")

print("ALL done")