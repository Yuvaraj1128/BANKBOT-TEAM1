import sqlite3

DB_PATH = "bank.db"

conn = sqlite3.connect(DB_PATH)
c = conn.cursor()

# Create users table if not exists (Double check)
c.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    account_number TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    name TEXT NOT NULL,
    email TEXT,
    phone TEXT,
    balance INTEGER DEFAULT 0
)
""")

# Insert the 3 users
users = [
    ("221", "Yuvith@123", "Yuvith", "yuvith@gmail.com", "9922001101", 150000.45),
    ("222", "Kiran@123", "Kiran", "kiran@gmail.com", "9876543210", 342000.36),
    ("223", "Vivek@123", "Vivek", "vivek@gmail.com", "8123456790", 30003.90)
]

c.executemany("""
INSERT OR REPLACE INTO users 
(account_number, password, name, email, phone, balance)
VALUES (?, ?, ?, ?, ?, ?)
""", users)

conn.commit()
conn.close()

print("✅ Users Seeded Successfully: Yuvith, Kiran, Vivek")