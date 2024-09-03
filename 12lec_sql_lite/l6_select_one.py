import sqlite3 as db

with db.connect("12lec_sql_lite/app.db") as conn:
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuarios;")
    # fetchone allows you to get the first element of the result
    print(cursor.fetchone())
