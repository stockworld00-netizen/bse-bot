import sqlite3

def is_duplicate(unique_id):
    conn = sqlite3.connect("bse.db")
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS posts (id TEXT)")
    c.execute("SELECT * FROM posts WHERE id=?", (unique_id,))
    exists = c.fetchone()
    if exists:
        conn.close()
        return True
    c.execute("INSERT INTO posts VALUES (?)", (unique_id,))
    conn.commit()
    conn.close()
    return False
