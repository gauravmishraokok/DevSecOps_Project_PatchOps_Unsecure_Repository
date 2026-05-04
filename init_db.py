import sqlite3
import os

def setup():
    db_path = "users.db"
    if os.path.exists(db_path):
        os.remove(db_path)
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    cursor.execute("""
    CREATE TABLE users (
        id INTEGER PRIMARY KEY,
        username TEXT,
        email TEXT,
        password TEXT,
        role TEXT
    )
    """)
    
    cursor.execute("INSERT INTO users VALUES (1, 'admin', 'admin@example.com', 'supersecretpassword123', 'admin')")
    cursor.execute("INSERT INTO users VALUES (2, 'bob', 'bob@example.com', 'bob123', 'user')")
    
    cursor.execute("""
    CREATE TABLE reports (
        id INTEGER PRIMARY KEY,
        user_id INTEGER,
        title TEXT,
        content TEXT
    )
    """)
    
    cursor.execute("INSERT INTO reports VALUES (1, 1, 'Admin Report', 'Sensitive data')")
    cursor.execute("INSERT INTO reports VALUES (2, 2, 'Bob Report', 'Bob data')")
    
    conn.commit()
    conn.close()
    print("Database initialized.")

if __name__ == "__main__":
    setup()