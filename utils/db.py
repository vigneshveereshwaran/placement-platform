import sqlite3

def connect_db():
    return sqlite3.connect("database/database.db")

def get_all_users():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()

    conn.close()
    return users

def check_user(username, password):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM users WHERE username=? AND password=?",
        (username, password)
    )

    user = cursor.fetchone()
    conn.close()
    return user

def delete_user(user_id):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM users WHERE id=?", (user_id,))

    conn.commit()
    conn.close()
    
def add_user(username, password):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO users (username, password, role) VALUES (?, ?, ?)",
        (username, password, "user")
    )

    conn.commit()
    conn.close()