import sqlite3

def init_db():
    conn = sqlite3.connect('blood_bank.db')
    c = conn.cursor()
    # Create tables
    c.execute('''CREATE TABLE IF NOT EXISTS donors (
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 name TEXT NOT NULL,
                 blood_group TEXT NOT NULL,
                 contact TEXT NOT NULL,
                 address TEXT)''')
    c.execute('''CREATE TABLE IF NOT EXISTS requests (
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 name TEXT NOT NULL,
                 blood_group TEXT NOT NULL,
                 contact TEXT NOT NULL,
                 status TEXT DEFAULT 'Pending')''')
    c.execute('''CREATE TABLE IF NOT EXISTS inventory (
                 blood_group TEXT PRIMARY KEY,
                 units INTEGER DEFAULT 0)''')
    # Initialize blood groups in inventory
    blood_groups = ['A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-']
    for bg in blood_groups:
        c.execute("INSERT OR IGNORE INTO inventory (blood_group, units) VALUES (?, 0)", (bg,))
    conn.commit()
    conn.close()

def add_donor(name, blood_group, contact, address):
    conn = sqlite3.connect('blood_bank.db')
    c = conn.cursor()
    c.execute("INSERT INTO donors (name, blood_group, contact, address) VALUES (?, ?, ?, ?)",
              (name, blood_group, contact, address))
    c.execute("UPDATE inventory SET units = units + 1 WHERE blood_group = ?", (blood_group,))
    conn.commit()
    conn.close()

def add_request(name, blood_group, contact):
    conn = sqlite3.connect('blood_bank.db')
    c = conn.cursor()
    c.execute("INSERT INTO requests (name, blood_group, contact) VALUES (?, ?, ?)",
              (name, blood_group, contact))
    conn.commit()
    conn.close()

def get_inventory():
    conn = sqlite3.connect('blood_bank.db')
    c = conn.cursor()
    c.execute("SELECT * FROM inventory")
    inventory = c.fetchall()
    conn.close()
    return inventory

def get_requests():
    conn = sqlite3.connect('blood_bank.db')
    c = conn.cursor()
    c.execute("SELECT * FROM requests")
    requests = c.fetchall()
    conn.close()
    return requests