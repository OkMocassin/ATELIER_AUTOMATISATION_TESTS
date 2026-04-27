import sqlite3
import json

def init_db():
    conn = sqlite3.connect("data.db")
    conn.execute("CREATE TABLE IF NOT EXISTS runs (data TEXT)")
    conn.close()

def save_run(data):
    conn = sqlite3.connect("data.db")
    conn.execute("INSERT INTO runs VALUES (?)", (json.dumps(data),))
    conn.commit()
    conn.close()

def list_runs():
    conn = sqlite3.connect("data.db")
    rows = conn.execute("SELECT data FROM runs").fetchall()
    conn.close()
    return [json.loads(r[0]) for r in rows]
