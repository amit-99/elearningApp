from PySide6 import QtWidgets

from ui.faculty.faculty_goToEvaluationCourse_window import Ui_FacultyGoToEvaluationCourseWindow

# from ui.faculty.faculty_addNewChapter_logic import FacultyAddNewChapterLogic
# from ui.faculty.faculty_modifyChapters_logic import FacultyModifyChaptersLogic

class FacultyGoToEvaluationCourseLogic(QtWidgets.QWidget):
    def __init__(self, args):
        super().__init__()
        self.ui = Ui_FacultyGoToEvaluationCourseWindow()
        self.ui.setupUi(self)
        self.previous_window = args[0]
        self.faculty_id = args[1]

        # handle input
        self.ui.lineEdit_3.setText("NCSUJegiCSC522F24")
        # course_id = self.ui.lineEdit_3.text()

        # handle button clicks
        # self.ui.pushButton_4.clicked.connect(self.add_new_chapter)
        # self.ui.pushButton_4.clicked.connect(self.modify_chapters)
        self.ui.pushButton_back.clicked.connect(self.handle_back)

    # def add_new_chapter(self):
    #     course_id = self.ui.lineEdit_3.text()

    #     self.faculty_addNewChapter_logic = FacultyAddNewChapterLogic([self, self.faculty_id])
    #     self.faculty_addNewChapter_logic.show()
    #     self.close()

    # def modify_chapters(self):
    #     course_id = self.ui.lineEdit_3.text()

    #     self.faculty_modifyChapters_logic = FacultyModifyChaptersLogic([self, self.faculty_id])
    #     self.faculty_modifyChapters_logic.show()
    #     self.close()

    def handle_back(self):
        self.previous_window.show()
        self.close()