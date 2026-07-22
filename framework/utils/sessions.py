import sqlite3

def init_db():
    conn = sqlite3.connect('ids.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS targets
                 (id INTEGER PRIMARY KEY, ip_address TEXT, port INTEGER, status TEXT)''')
    c.execute('''CREATE TABLE IF NOT EXISTS sessions
                 (id INTEGER PRIMARY KEY, target_id INTEGER, payload TEXT, status TEXT, start_time DATETIME, end_time DATETIME, note TEXT,
                  FOREIGN KEY(target_id) REFERENCES targets(id))''')
    c.execute('''CREATE TABLE IF NOT EXISTS notes
                 (id INTEGER PRIMARY KEY, target_id INTEGER, note TEXT,
                  FOREIGN KEY(target_id) REFERENCES targets(id))''')
    conn.commit()
    conn.close()

def add_target(ip_address, port):
    conn = sqlite3.connect('ids.db')
    c = conn.cursor()
    c.execute("INSERT INTO targets (ip_address, port, status) VALUES (?, ?, 'active')", (ip_address, port))
    conn.commit()
    conn.close()

def get_active_targets():
    conn = sqlite3.connect('ids.db')
    c = conn.cursor()
    c.execute("SELECT * FROM targets WHERE status = 'active'")
    rows = c.fetchall()
    conn.close()
    return rows

def get_target_ips():
    conn = sqlite3.connect('ids.db')
    c = conn.cursor()
    c.execute("SELECT ip_address FROM targets")
    rows = c.fetchall()
    conn.close()
    return rows

def add_note(target_id, note):
    conn = sqlite3.connect('ids.db')
    c = conn.cursor()
    c.execute("INSERT INTO notes (target_id, note) VALUES (?, ?)", (target_id, note))
    conn.commit()
    conn.close()
    return "Note added"

def add_session(target_id, payload):
    conn = sqlite3.connect('ids.db')
    c = conn.cursor()
    c.execute("INSERT INTO sessions (target_id, payload, status, start_time) VALUES (?, ?, 'active', CURRENT_TIMESTAMP)", (target_id, payload))
    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()
    add_target("127.0.0.1", 4444)
    print(get_active_targets())
    print(get_target_ips())
