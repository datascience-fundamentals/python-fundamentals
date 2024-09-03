import sqlite3 as db

with db.connect("12lec_sql_lite/app.db") as conn:
    cursor = conn.cursor()
    usuarios = [
        (2, "Chanchito feliz"),
        (3, "Chanchito triste"),
    ]
    cursor.executemany(
        """
          INSERT INTO usuarios VALUES (?, ?);
        """,
        usuarios,  # executemany allows you to pass a list of tuples which contains the values
    )
