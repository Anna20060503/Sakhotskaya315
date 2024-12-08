import mysql.connector
from mysql.connector import Error

def connect_to_database():
    """Создает соединение с базой данных."""
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Mamika27",
            database="timetable8"
        )
        return connection
    except Error as e:
        print(f"Ошибка подключения: {e}")
        return None

def register_user(name, phone, email, password):
    """Регистрация пользователя в базе данных."""
    connection = connect_to_database()
    if connection:
        cursor = connection.cursor()
        try:
            cursor.execute("INSERT INTO student (name, phone, email, password) VALUES (%s, %s, %s, %s)",
                           (name, phone, email, password))
            connection.commit()
            return True
        except Error as err:
            print(f"Ошибка: {err}")
            return False
        finally:
            cursor.close()
            connection.close()
    return False

def login_user(email, password):
    """Проверка пользователя в базе данных."""
    connection = connect_to_database()
    if connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM student WHERE email = %s AND password = %s", (email, password))
        result = cursor.fetchone()
        cursor.close()
        connection.close()
        return result
    return None