from fastapi import FastAPI
from db import cur, conn
from hash import make, check
from token import issue
from audit import log

app = FastAPI()

@app.post("/register")
def register(u: str, p: str):
    cur.execute("INSERT INTO users VALUES(?,?)", (u, make(p)))
    conn.commit()
    log(f"register:{u}")
    return {"ok": True}

@app.post("/login")
def login(u: str, p: str):
    cur.execute("SELECT p FROM users WHERE u=?", (u,))
    r = cur.fetchone()
    if r and check(p, r[0]):
        t = issue(u)
        log(f"login:{u}")
        return {"token": t}
    return {"error": "invalid"}
