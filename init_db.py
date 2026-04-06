import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

# Drop table if exists (to reset cleanly)
cursor.execute("DROP TABLE IF EXISTS users")

# Create table
cursor.execute("""
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    password TEXT
)
""")

# Insert test user
cursor.execute("INSERT INTO users (username, password) VALUES ('admin', 'admin123')")

conn.commit()
conn.close()

print("✅ Database initialized successfully!")