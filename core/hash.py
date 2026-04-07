import hashlib

def make(p):
    return hashlib.sha256(p.encode()).hexdigest()

def check(p, hp):
    return make(p) == hp
