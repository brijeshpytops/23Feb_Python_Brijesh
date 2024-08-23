from .dbConnection import cursor

def create_database():
    try:
        database_name = input("Enter a database name :")
        Query = f"CREATE DATABASE IF NOT EXISTS {database_name}"
        cursor.execute(Query)
    except Exception as err:
        print(f"ERROR: {err}")