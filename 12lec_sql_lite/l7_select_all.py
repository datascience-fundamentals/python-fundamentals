import sqlite3 as db

with db.connect("12lec_sql_lite/app.db") as conn:
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuarios")
    print(cursor.fetchall())  # fetchall allows you to select all elements
