
import sqlite3
import pandas as pd

def connect_db():
    return sqlite3.connect("students.db")

def create_table():
    conn = connect_db()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS students(
            roll_no INTEGER PRIMARY KEY,
            name TEXT,
            course TEXT,
            marks REAL
        )
    """)
    conn.commit()
    conn.close()

def add_student(roll, name, course, marks):
    conn = connect_db()
    conn.execute(
        "INSERT INTO students VALUES(?,?,?,?)",
        (roll, name, course, marks)
    )
    conn.commit()
    conn.close()

def view_students():
    conn = connect_db()
    df = pd.read_sql_query("SELECT * FROM students", conn)
    conn.close()
    return df

def update_student(roll, name, course, marks):
    conn = connect_db()
    conn.execute("""
        UPDATE students
        SET name=?, course=?, marks=?
        WHERE roll_no=?
    """, (name, course, marks, roll))
    conn.commit()
    conn.close()

def delete_student(roll):
    conn = connect_db()
    conn.execute(
        "DELETE FROM students WHERE roll_no=?",
        (roll,)
    )
    conn.commit()
    conn.close()

create_table()
