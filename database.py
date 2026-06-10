import sqlite3

DB_NAME = "agri.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    c.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        password TEXT,
        role TEXT
    )
    ''')

    c.execute('''
    CREATE TABLE IF NOT EXISTS medicines (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        animal TEXT,
        dose TEXT,
        cost REAL,
        colour TEXT,
        purpose TEXT,
        manufacturer TEXT,
        side_effects TEXT,
        withdrawal_period TEXT
    )
    ''')

    conn.commit()
    conn.close()


def check_login(username, password):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    c.execute("SELECT role FROM users WHERE username=? AND password=?", (username, password))
    result = c.fetchone()

    conn.close()

    if result:
        return result[0]
    return None