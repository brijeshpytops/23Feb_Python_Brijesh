from sqlDb.createDatabase import create_database
from sqlDb.createTable import create_table
from sqlDb.insertData import insert_data
from sqlDb.readData import read_data

# create_database()
# create_table()
# insert_data()
for user in read_data():
    print(user)