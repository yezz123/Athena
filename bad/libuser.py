import sqlite3


def login(username, password):

    conn = sqlite3.connect("db_users.sqlite")
    conn.set_trace_callback(print)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()

    user = c.execute(
        f"SELECT * FROM users WHERE username = '{username}' and password = '{password}'"
    ).fetchone()

    if user:
        return user["username"]
    else:
        return False


def create(username, password):

    conn = sqlite3.connect("db_users.sqlite")
    c = conn.cursor()

    c.execute(
        "INSERT INTO users (username, password, failures, mfa_enabled, mfa_secret) VALUES ('%s', '%s', '%d', '%d', '%s')"
        % (username, password, 0, 0, "")
    )

    conn.commit()
    conn.close()


def userlist():

    conn = sqlite3.connect("db_users.sqlite")
    conn.set_trace_callback(print)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()

    users = c.execute("SELECT * FROM users").fetchall()

    if not users:
        return []
    else:
        return [user["username"] for user in users]


def password_change(username, password):

    conn = sqlite3.connect("db_users.sqlite")
    conn.set_trace_callback(print)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()

    c.execute(
        f"UPDATE users SET password = '{password}' WHERE username = '{username}'"
    )
    conn.commit()

    return True


def password_complexity(password):
    return True
