from .dbConnection import db, cursor

def insert_data():
    # Insert data into the table
    query = """
    INSERT INTO users (username, email, password)
    VALUES
    ('kavsikyo', 'kavsikyo.walker@mail.com', 'kavsikyo@2024!');
    """
    cursor.execute(query)
    db.commit()