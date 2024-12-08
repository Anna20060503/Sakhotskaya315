import mysql.connector


def create_database():
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Mamika27"
    )
    cursor = db.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS timetable8")
    db.close()


def create_tables():
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Mamika27",
        database="timetable8"
    )
    cursor = db.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS student (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name TEXT,
        phone TEXT,
        email TEXT,
        password TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS lesson (
        id INT AUTO_INCREMENT PRIMARY KEY,
        subject_id INT,
        teacher_id INT,
        date_time DATETIME,
        classroom TEXT,
        duration INT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS teacher (
        id INT AUTO_INCREMENT PRIMARY KEY,
        first_name TEXT,
        last_name TEXT,
        subject TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS student_lesson (
        student_id INT,
        lesson_id INT,
        PRIMARY KEY (student_id, lesson_id),
        FOREIGN KEY (student_id) REFERENCES student(id),
        FOREIGN KEY (lesson_id) REFERENCES lesson(id)
    )
    """)

    db.commit()
    db.close()


create_database()
create_tables()