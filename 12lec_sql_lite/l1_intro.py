import sqlite3 as db

# creating a connection to sql lite db
con = db.connect("12lec_sql_lite/app.db")
con.close()
