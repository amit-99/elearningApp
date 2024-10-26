from PySide6 import QtWidgets
from dao.user_dao import UserDAO
from db.db_connection import get_db_connection
from ui.ta.ta_login_window import Ui_TaLoginWindow

class TALoginLogic(QtWidgets.QWidget):
    def __init__(self, previous_window):
        super().__init__()
        self.ui = Ui_TaLoginWindow()
        self.ui.setupUi(self)
        self.previous_window = previous_window

        self.db_connection = get_db_connection()
        self.user_dao = UserDAO(self.db_connection)

        self.ui.pushButton_6.clicked.connect(self.handle_login)
        self.ui.pushButton_5.clicked.connect(self.handle_back)

    def handle_login(self):
        username = self.ui.lineEdit.text()
        password = self.ui.lineEdit_2.text()
        role = "TA"

        if self.user_dao.validate_credentials(role, username, password):
            QtWidgets.QMessageBox.information(self, "Login Successful", "Welcome, TA!")
            self.close()
        else:
            QtWidgets.QMessageBox.warning(self, "Login Failed", "Invalid User ID or password.")

    def handle_back(self):
        self.previous_window.show()
        self.close()
