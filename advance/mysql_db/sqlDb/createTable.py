from .dbConnection import cursor

def create_table():
    table_name =  input("enter a table_name: ")
    field_config = input("Enter a fields with their config: ")
    query = f"create table {table_name} (" + field_config + ");"
    print(query)
    cursor.execute(query)