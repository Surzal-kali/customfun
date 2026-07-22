import sqlite3
#I'll add more later, but for now

def init_db():
    conn = sqlite3.connect('sessions.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS sessions (id INTEGER PRIMARY KEY, session_name TEXT, session_data TEXT)''')
    conn.commit()
    conn.close()