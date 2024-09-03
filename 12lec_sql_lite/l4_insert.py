import sqlite3 as db

with db.connect("12lec_sql_lite/app.db") as conn:
    cursor = conn.cursor()
    cursor.execute(
        """
          INSERT INTO usuarios VALUES(?,?);
        """,
        (1, "Hola Mundo"),  # the parameter values are passed by tuple
    )
