import sys
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QMessageBox
from database_operations import register_user, login_user
from database import create_database, create_tables

class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Расписание занятий студента")
        self.setGeometry(100, 100, 400, 300)

        self.layout = QtWidgets.QVBoxLayout()

        self.label_name = QtWidgets.QLabel("Имя:")
        self.input_name = QtWidgets.QLineEdit()
        self.label_phone = QtWidgets.QLabel("Телефон:")
        self.input_phone = QtWidgets.QLineEdit()
        self.label_email = QtWidgets.QLabel("Электронная почта:")
        self.input_email = QtWidgets.QLineEdit()
        self.label_password = QtWidgets.QLabel("Пароль:")
        self.input_password = QtWidgets.QLineEdit()
        self.input_password.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)

        self.btn_register = QtWidgets.QPushButton("Регистрация")
        self.btn_register.clicked.connect(self.register)

        self.btn_login = QtWidgets.QPushButton("Вход")
        self.btn_login.clicked.connect(self.login)

        self.layout.addWidget(self.label_name)
        self.layout.addWidget(self.input_name)
        self.layout.addWidget(self.label_phone)
        self.layout.addWidget(self.input_phone)
        self.layout.addWidget(self.label_email)
        self.layout.addWidget(self.input_email)
        self.layout.addWidget(self.label_password)
        self.layout.addWidget(self.input_password)
        self.layout.addWidget(self.btn_register)
        self.layout.addWidget(self.btn_login)

        self.setLayout(self.layout)

    def register(self):
        name = self.input_name.text()
        phone = self.input_phone.text()
        email = self.input_email.text()
        password = self.input_password.text()

        if register_user(name, phone, email, password):
            QMessageBox.information(self, "Информация", "Регистрация успешна!")
        else:
            QMessageBox.warning(self, "Ошибка", "Ошибка при регистрации.")

    def login(self):
        email = self.input_email.text()
        password = self.input_password.text()

        result = login_user(email, password)

        if result:
            QMessageBox.information(self, "Информация", "Вход успешен!")
            self.open_schedule_window()
        else:
            QMessageBox.warning(self, "Ошибка", "Неверный email или пароль.")

    def open_schedule_window(self):
        self.schedule_window = ScheduleWindow()
        self.schedule_window.show()
        self.close()


class ScheduleWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Расписание занятий")
        self.setGeometry(100, 100, 600, 400)

        self.layout = QtWidgets.QVBoxLayout()
        self.label_schedule = QtWidgets.QLabel("Расписание занятий:")
        self.layout.addWidget(self.label_schedule)

        self.schedule_list = QtWidgets.QListWidget()
        self.layout.addWidget(self.schedule_list)

        self.load_schedule()

        self.setLayout(self.layout)

    def load_schedule(self):
        # Здесь можно добавить свои занятия
        lessons = [
            {"subject": "Математика", "teacher": "Иванов И.И.", "date_time": "2023-10-01 10:00", "classroom": "101",
             "duration": 90},
            {"subject": "Физика", "teacher": "Петров П.П.", "date_time": "2023-10-01 12:00", "classroom": "102",
             "duration": 60},
            {"subject": "Химия", "teacher": "Сидоров С.С.", "date_time": "2023-10-02 10:00", "classroom": "103",
             "duration": 90},
        ]

        for lesson in lessons:
            self.schedule_list.addItem(
                f"{lesson['subject']} - {lesson['teacher']} | {lesson['date_time']} | Аудитория: {lesson['classroom']} | Продолжительность: {lesson['duration']} мин")


if __name__ == "__main__":
    create_database()  # Создаем базу данных
    create_tables()  # Создаем таблицы
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
    create_database()  # Создаем базу данных
    create_tables()  # Создаем таблицы
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

