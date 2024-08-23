import mysql.connector

db = mysql.connector.connect(
    user='root',
    password='',
    host='127.0.0.1',
    database='wzctrl'
)

cursor = db.cursor()

if db.is_connected():
    print("Connection established")
else:
    print("Connection failed")