import sys
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QMessageBox, QListWidget
from database_operations import register_user, login_user
from database import create_database, create_tables

class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Расписание занятий студента")
        self.setGeometry(100, 100, 400, 200)

        self.layout = QtWidgets.QVBoxLayout()

        self.btn_register = QtWidgets.QPushButton("Регистрация")
        self.btn_register.clicked.connect(self.open_register_window)

        self.btn_login = QtWidgets.QPushButton("Вход")
        self.btn_login.clicked.connect(self.open_login_window)

        self.layout.addWidget(self.btn_register)
        self.layout.addWidget(self.btn_login)

        self.setLayout(self.layout)

    def open_register_window(self):
        self.register_window = RegisterWindow()
        self.register_window.show()

    def open_login_window(self):
        self.login_window = LoginWindow()
        self.login_window.show()


class RegisterWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Регистрация")
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

        self.btn_register = QtWidgets.QPushButton("Зарегистрироваться")
        self.btn_register.clicked.connect(self.register)

        self.layout.addWidget(self.label_name)
        self.layout.addWidget(self.input_name)
        self.layout.addWidget(self.label_phone)
        self.layout.addWidget(self.input_phone)
        self.layout.addWidget(self.label_email)
        self.layout.addWidget(self.input_email)
        self.layout.addWidget(self.label_password)
        self.layout.addWidget(self.input_password)
        self.layout.addWidget(self.btn_register)

        self.setLayout(self.layout)

    def register(self):
        name = self.input_name.text()
        phone = self.input_phone.text()
        email = self.input_email.text()
        password = self.input_password.text()

        if register_user(name, phone, email, password):
            QMessageBox.information(self, "Информация", "Регистрация успешна!")
            self.close()  # Закрыть окно регистрации после успешной регистрации
        else:
            QMessageBox.warning(self, "Ошибка", "Ошибка при регистрации.")


class LoginWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Вход")
        self.setGeometry(100, 100, 400, 200)

        self.layout = QtWidgets.QVBoxLayout()

        self.label_email = QtWidgets.QLabel("Электронная почта:")
        self.input_email = QtWidgets.QLineEdit()
        self.label_password = QtWidgets.QLabel("Пароль:")
        self.input_password = QtWidgets.QLineEdit()
        self.input_password.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)

        self.btn_login = QtWidgets.QPushButton("Войти")
        self.btn_login.clicked.connect(self.login)

        self.layout.addWidget(self.label_email)
        self.layout.addWidget(self.input_email)
        self.layout.addWidget(self.label_password)
        self.layout.addWidget(self.input_password)
        self.layout.addWidget(self.btn_login)

        self.setLayout(self.layout)

    def login(self):
        email = self.input_email.text()
        password = self.input_password.text()

        result = login_user(email, password)

        if result:
            QMessageBox.information(self, "Информация", "Вход успешен!")
            self.open_schedule_window()
            self.close()  # Закрыть окно входа после успешного входа
        else:
            QMessageBox.warning(self, "Ошибка", "Неверный email или пароль.")

    def open_schedule_window(self):
        self.schedule_window = ScheduleWindow()
        self.schedule_window.show()


class ScheduleWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Расписание занятий")
        self.setGeometry(100, 100, 600, 400)

        self.layout = QtWidgets.QVBoxLayout()
        self.label_schedule = QtWidgets.QLabel("Расписание занятий:")
        self.layout.addWidget(self.label_schedule)

        self.schedule_list = QListWidget()
        self.layout.addWidget(self.schedule_list)

        self.load_schedule()

        self.setLayout(self.layout)

    def load_schedule(self):
        # Здесь можно добавить свои занятия
        lessons = [
            {"subject": "МДК.11.01", "teacher": "Типикина П.В.", "date_time": "05.12 8:20", "classroom": "614", "duration": 80},
            {"subject": "МДК.11.01", "teacher": "Типикина П.В.", "date_time": "05.12 9:50", "classroom": "627", "duration": 80},
            {"subject": "Иностранный язык", "teacher": "Маркелова В.Н.", "date_time": "05.12 11:20", "classroom": "610", "duration": 80},
        ]

        for lesson in lessons:
            self.schedule_list.addItem(
                f"{lesson['subject']} - {lesson['teacher']} | {lesson['date_time']} | Аудитория: {lesson['classroom']} | Продолжительность: {lesson['duration']} мин"
            )

if __name__ == "__main__":
    create_database()  # Создаем базу данных
    create_tables()    # Создаем таблицы
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
