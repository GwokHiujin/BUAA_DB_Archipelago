import sqlite3

connection = sqlite3.connect('db.sqlite3')
cur = connection.cursor()
with open('db.sql', 'r') as sql_file:
    sql_script = sql_file.read()
connection.executescript(sql_script)
connection.commit()
connection.close()