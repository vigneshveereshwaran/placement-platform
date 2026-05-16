import sqlite3

conn = sqlite3.connect("database/database.db")
cursor = conn.cursor()

# Create table only if not exists
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    password TEXT,
    role TEXT
)
""")

# Insert admin ONLY if not already exists
cursor.execute("""
SELECT * FROM users WHERE username='admin'
""")

if not cursor.fetchone():
    cursor.execute("""
    INSERT INTO users (username, password, role)
    VALUES ('admin', '123', 'admin')
    """)

conn.commit()
conn.close()

print("Database ready!")