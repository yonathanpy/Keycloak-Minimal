import sqlite3

conn = sqlite3.connect("id.db", check_same_thread=False)
cur = conn.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS users(u TEXT PRIMARY KEY, p TEXT)")
cur.execute("CREATE TABLE IF NOT EXISTS logs(e TEXT)")
conn.commit()
