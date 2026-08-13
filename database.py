import sqlite3

def create_table():

    conn = sqlite3.connect("school.db")

    cursor = conn.cursor()

    cursor.execute(
        """CREATE TABLE IF NOT EXISTS students(
        student_id TEXT PRIMARY KEY,
        name TEXT,
        semester INTEGER)
    """)
    conn.commit()
    conn.close()
    
def add_student(student_id, name, semester):

    conn = sqlite3.connect("school.db")

    cursor = conn.cursor()

    cursor.execute(
        """
    INSERT INTO students
    VALUES (?, ?, ?)
    """,
    (student_id, name, semester)
    )

    conn.commit()
    conn.close()

def get_all_students():

    conn = sqlite3.connect("school.db")

    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM students"
    )
    students = cursor.fetchall()

    conn.close()
    return students

def delete_student(student_id):

    conn = sqlite3.connect("school.db")

    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM students WHERE student_id = ?",
        (student_id,)
    )
    conn.commit()
    conn.close()

def update_student(student_id, name, semester):

    conn = sqlite3.connect("school.db")

    cursor = conn.cursor()

    cursor.execute(
        """
    UPDATE students
    SET name = ?, semester = ?
    WHERE student_id = ?
    """,
    (name, semester, student_id)
    )
    conn.commit()
    conn.close()

def search_student(student_id):

    conn = sqlite3.connect("school.db")

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT * FROM students
        WHERE student_id=?""",
        (student_id,)
    )

    student =  cursor.fetchone()
    conn.close()
    return student
