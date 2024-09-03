import sqlite3 as db

conn = db.connect("12lec_sql_lite/app.db")
cursor = conn.cursor()  # Creating a cursor before to execute a query
cursor.execute(
    """
      CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER primary key,
        nombre VARCHAR(50)
      );
    """
)
# It's necessary to commit the changes in order to execute them on the db
conn.commit()
conn.close()
