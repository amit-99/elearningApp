# Form implementation generated from reading ui file 'faculty_add_new_chapter_window.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PySide6 import QtCore, QtGui, QtWidgets


class Ui_FacultyAddNewChapterWindow(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(720, 480)
        self.label = QtWidgets.QLabel(parent=Form)
        self.label.setGeometry(QtCore.QRect(215, 57, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(21)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.widget = QtWidgets.QWidget(parent=Form)
        self.widget.setGeometry(QtCore.QRect(130, 150, 349, 231))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_8 = QtWidgets.QLabel(parent=self.widget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.verticalLayout.addWidget(self.label_8)
        self.lineEdit_7 = QtWidgets.QLineEdit(parent=self.widget)
        self.lineEdit_7.setStyleSheet("QLineEdit {\n"
"        background-color: #2b2b2b;  /* Dark background */\n"
"        color: #fcba03;  /* Text color */\n"
"        border: 2px solid #3d3d3d;  /* Border color */\n"
"        border-radius: 8px;  /* Rounded corners */\n"
"        padding: 8px;  /* Padding inside the input field */\n"
"        font-size: 16px;  /* Font size */\n"
"        font-weight: bold;  /* Bold font */\n"
"    }\n"
"\n"
"    QLineEdit:hover {\n"
"        background-color: #3d3d3d;  /* Background when hovered */\n"
"        border: 2px solid #fcba03;  /* Border color when hovered */\n"
"    }\n"
"\n"
"    QLineEdit:focus {\n"
"        background-color: #1a1a1a;  /* Background when focused */\n"
"        border: 2px solid #fcba03;  /* Border color when focused */\n"
"        color: #ffffff;  /* Text color when focused */\n"
"    }")
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.verticalLayout.addWidget(self.lineEdit_7)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_6 = QtWidgets.QLabel(parent=self.widget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_4.addWidget(self.label_6)
        self.lineEdit_5 = QtWidgets.QLineEdit(parent=self.widget)
        self.lineEdit_5.setStyleSheet("QLineEdit {\n"
"        background-color: #2b2b2b;  /* Dark background */\n"
"        color: #fcba03;  /* Text color */\n"
"        border: 2px solid #3d3d3d;  /* Border color */\n"
"        border-radius: 8px;  /* Rounded corners */\n"
"        padding: 8px;  /* Padding inside the input field */\n"
"        font-size: 16px;  /* Font size */\n"
"        font-weight: bold;  /* Bold font */\n"
"    }\n"
"\n"
"    QLineEdit:hover {\n"
"        background-color: #3d3d3d;  /* Background when hovered */\n"
"        border: 2px solid #fcba03;  /* Border color when hovered */\n"
"    }\n"
"\n"
"    QLineEdit:focus {\n"
"        background-color: #1a1a1a;  /* Background when focused */\n"
"        border: 2px solid #fcba03;  /* Border color when focused */\n"
"        color: #ffffff;  /* Text color when focused */\n"
"    }")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.horizontalLayout_4.addWidget(self.lineEdit_5)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_7 = QtWidgets.QLabel(parent=self.widget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_5.addWidget(self.label_7)
        self.lineEdit_6 = QtWidgets.QLineEdit(parent=self.widget)
        self.lineEdit_6.setStyleSheet("QLineEdit {\n"
"        background-color: #2b2b2b;  /* Dark background */\n"
"        color: #fcba03;  /* Text color */\n"
"        border: 2px solid #3d3d3d;  /* Border color */\n"
"        border-radius: 8px;  /* Rounded corners */\n"
"        padding: 8px;  /* Padding inside the input field */\n"
"        font-size: 16px;  /* Font size */\n"
"        font-weight: bold;  /* Bold font */\n"
"    }\n"
"\n"
"    QLineEdit:hover {\n"
"        background-color: #3d3d3d;  /* Background when hovered */\n"
"        border: 2px solid #fcba03;  /* Border color when hovered */\n"
"    }\n"
"\n"
"    QLineEdit:focus {\n"
"        background-color: #1a1a1a;  /* Background when focused */\n"
"        border: 2px solid #fcba03;  /* Border color when focused */\n"
"        color: #ffffff;  /* Text color when focused */\n"
"    }")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.horizontalLayout_5.addWidget(self.lineEdit_6)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.pushButton_back_2 = QtWidgets.QPushButton(parent=self.widget)
        self.pushButton_back_2.setStyleSheet("QPushButton {\n"
"        background-color: #2b2b2b;  \n"
"        color: #fcba03;              \n"
"        border: 2px solid #3d3d3d;      \n"
"        border-radius: 8px;          \n"
"        padding: 8px 16px;            \n"
"        font-size: 16px;            \n"
"        font-weight: bold;\n"
"    \n"
"    }\n"
"\n"
"    QPushButton:hover {\n"
"        background-color: #fcba03;\n"
"         color: #000000;\n"
"        border: 2px solid #5a5a5a;    \n"
"    }\n"
"\n"
"    QPushButton:pressed {\n"
"        background-color: #1a1a1a;      \n"
"        border: 2px solid #2b2b2b;      \n"
"    }")
        self.pushButton_back_2.setObjectName("pushButton_back_2")
        self.horizontalLayout_6.addWidget(self.pushButton_back_2)
        self.pushButton_4 = QtWidgets.QPushButton(parent=self.widget)
        self.pushButton_4.setStyleSheet("QPushButton {\n"
"        background-color: #2b2b2b;  \n"
"        color: #fcba03;              \n"
"        border: 2px solid #3d3d3d;      \n"
"        border-radius: 8px;          \n"
"        padding: 8px 16px;            \n"
"        font-size: 16px;            \n"
"        font-weight: bold;\n"
"    \n"
"    }\n"
"\n"
"    QPushButton:hover {\n"
"        background-color: #fcba03;\n"
"         color: #000000;\n"
"        border: 2px solid #5a5a5a;    \n"
"    }\n"
"\n"
"    QPushButton:pressed {\n"
"        background-color: #1a1a1a;      \n"
"        border: 2px solid #2b2b2b;      \n"
"    }")
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_6.addWidget(self.pushButton_4)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.verticalLayout.addLayout(self.verticalLayout_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Add New Chapter"))
        self.label_8.setText(_translate("Form", "Course ID:"))
        self.label_6.setText(_translate("Form", "Unique Chapter ID:"))
        self.label_7.setText(_translate("Form", "Chapter Title:"))
        self.pushButton_back_2.setText(_translate("Form", "Back"))
        self.pushButton_4.setText(_translate("Form", "Add New Section"))
