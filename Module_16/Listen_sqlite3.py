import sqlite3 as sl

con = sl.connect('students.db')

with con:
    con.execute("""
        CREATE TABLE students (
            id PRIMARY KEY,
            name STRING,
            age INTEGER); """)
