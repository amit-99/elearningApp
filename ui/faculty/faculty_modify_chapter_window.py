# Form implementation generated from reading ui file 'faculty_modify_chapter_window.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PySide6 import QtCore, QtGui, QtWidgets


class Ui_FacultyModifyChapterWindow(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(720, 480)
        self.label = QtWidgets.QLabel(parent=Form)
        self.label.setGeometry(QtCore.QRect(230, 30, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(21)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.layoutWidget = QtWidgets.QWidget(parent=Form)
        self.layoutWidget.setGeometry(QtCore.QRect(160, 170, 349, 291))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_4 = QtWidgets.QLabel(parent=self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.lineEdit_3 = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.lineEdit_3.setStyleSheet("QLineEdit {\n"
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
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalLayout.addWidget(self.lineEdit_3)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton = QtWidgets.QPushButton(parent=self.layoutWidget)
        self.pushButton.setStyleSheet("QPushButton {\n"
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
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_3.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.layoutWidget)
        self.pushButton_2.setStyleSheet("QPushButton {\n"
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
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(parent=self.layoutWidget)
        self.pushButton_3.setStyleSheet("QPushButton {\n"
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
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)
        self.delete_chapter = QtWidgets.QPushButton(parent=self.layoutWidget)
        self.delete_chapter.setStyleSheet("QPushButton {\n"
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
        self.delete_chapter.setObjectName("delete_chapter")
        self.verticalLayout.addWidget(self.delete_chapter)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.pushButton_back = QtWidgets.QPushButton(parent=self.layoutWidget)
        self.pushButton_back.setStyleSheet("QPushButton {\n"
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
        self.pushButton_back.setObjectName("pushButton_back")
        self.verticalLayout_2.addWidget(self.pushButton_back)
        self.lineEdit_4 = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit_4.setGeometry(QtCore.QRect(330, 120, 177, 43))
        self.lineEdit_4.setStyleSheet("QLineEdit {\n"
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
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_5 = QtWidgets.QLabel(parent=Form)
        self.label_5.setGeometry(QtCore.QRect(160, 120, 160, 43))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Modify Chapter"))
        self.label_4.setText(_translate("Form", "Unique Chapter ID:"))
        self.pushButton.setText(_translate("Form", "Add New Section"))
        self.pushButton_2.setText(_translate("Form", "Modify Section"))
        self.pushButton_3.setText(_translate("Form", "Hide Chapter"))
        self.delete_chapter.setText(_translate("Form", "Delete Chapter"))
        self.pushButton_back.setText(_translate("Form", "Back"))
        self.label_5.setText(_translate("Form", "Textbook ID:"))
