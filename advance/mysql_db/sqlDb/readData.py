from .dbConnection import cursor

def read_data():
    # Read data from the database
    # cursor.execute("SELECT * FROM users")
    # cursor.execute("SELECT * FROM users where user_id < 6")
    # cursor.execute("SELECT * FROM users limit 6")
    # cursor.execute("SELECT * FROM users order by username DESC")
    cursor.execute("SELECT * FROM users order by username")
    data = cursor.fetchall()
    return data