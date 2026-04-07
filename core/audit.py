from db import cur, conn

def log(e):
    cur.execute("INSERT INTO logs VALUES(?)", (e,))
    conn.commit()
