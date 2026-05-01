import sqlite3

# Connect to database (creates file if not exists)
conn = sqlite3.connect("students.db")

# Create a cursor
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER
)
""")

# Insert data
cursor.execute("INSERT INTO students (name, age) VALUES (?, ?)", ("Ravi", 20))
cursor.execute("INSERT INTO students (name, age) VALUES (?, ?)", ("Anu", 19))

# Save changes
conn.commit()

# Fetch data
cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()

# Print data
for row in rows:
    print(row)

# Close connection
conn.close()