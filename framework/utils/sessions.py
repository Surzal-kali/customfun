import sqlite3


class Database_Manager():
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
        return conn, c

    def add_target(ip_address, port):
        conn = sqlite3.connect('ids.db')
        c = conn.cursor()
        c.execute("INSERT INTO targets (ip_address, port, status) VALUES (?, ?, 'active')", (ip_address, port))
        conn.commit()
        return conn, c

    def get_active_targets():
        conn = sqlite3.connect('ids.db')
        c = conn.cursor()
        c.execute("SELECT * FROM targets WHERE status = 'active'")
        rows = c.fetchall()
        return rows, conn, c
    
    def get_target_by_ip(ip_address):
        conn = sqlite3.connect('ids.db')
        c = conn.cursor()
        c.execute("SELECT * FROM targets WHERE ip_address ={ip_address}".format(ip_address=ip_address))
        rows = c.fetchall()
        return rows, conn, c

    def get_target_ips():
        conn = sqlite3.connect('ids.db')
        c = conn.cursor()
        c.execute("SELECT ip_address FROM targets")
        rows = c.fetchall()
        return rows, conn, c

    def add_note(target_id, note):
        conn = sqlite3.connect('ids.db')
        c = conn.cursor()
        c.execute("INSERT INTO notes (target_id, note) VALUES (?, ?)", (target_id, note))
        conn.commit()
        return "Note added", conn, c


    def add_session(target_id, payload):
        conn = sqlite3.connect('ids.db')
        c = conn.cursor()
        c.execute("INSERT INTO sessions (target_id, payload, status, start_time) VALUES (?, ?, 'active', CURRENT_TIMESTAMP)", (target_id, payload))
        conn.commit()
        return conn, c

    def close_db():
        conn = sqlite3.connect('ids.db')
        c = conn.cursor()
        conn.close()
        return "Database closed"

