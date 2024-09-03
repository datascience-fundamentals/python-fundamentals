import sqlite3 as db

# Using with, It's not necessary to close the connection and commit the changes,
# because it executes the magic method __exit__ which is in charge to do it
with db.connect("12lec_sql_lite/app.db") as conn:
    cursor = conn.cursor()
    cursor.execute(
        """
          CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER primary key,
            nombre VARCHAR(50)
          );
        """
    )
