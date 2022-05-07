import sqlite3


def get_posts(username):

    conn = sqlite3.connect("db_posts.sqlite")
    conn.set_trace_callback(print)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()

    rows = c.execute(
        "SELECT * FROM posts WHERE username = ? ORDER BY date DESC", (username,)
    ).fetchall()

    return [dict(zip(row.keys(), row)) for row in rows]


def post(username, text):

    conn = sqlite3.connect("db_posts.sqlite")
    conn.set_trace_callback(print)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()

    rows = c.execute(
        "INSERT INTO posts (username, text, date) VALUES (?, ?, DateTime('now'))",
        (username, text),
    )
    conn.commit()

    return True
