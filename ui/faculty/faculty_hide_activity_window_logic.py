from PySide6 import QtWidgets
from dao.user_dao import UserDAO
from db.db_connection import get_db_connection
from ui.admin.admin_modifyChapter_window import Ui_AdminModifyChapterWindow
from ui.admin.admin_addNewSection_logic import AdminAddNewSectionLogic
from ui.admin.admin_modifySection_logic import AdminModifySectionLogic
from ui.faculty.faculty_hide_activity_window import Ui_FacultyHideActivityWindow
from ui.faculty.faculty_hide_content_block_window import Ui_FacultyHideContentBlockWindow
from ui.faculty.faculty_hide_section_window import Ui_FacultyHideSectionWindow
from ui.faculty.faculty_modify_chapter_window import Ui_FacultyModifyChapterWindow

class FacultyHideActivityLogic(QtWidgets.QWidget):
    def __init__(self, args):
        super().__init__()
        self.ui = Ui_FacultyHideActivityWindow()
        self.ui.setupUi(self)
        self.previous_window = args[0]
        self.textbook_id=args[1]
        self.chapter_id=args[2]
        self.section_id=args[3]
        self.block_id=args[4]
        
        self.db_connection = get_db_connection()    
        self.user_dao = UserDAO(self.db_connection)

        self.ui.pushButton_6.clicked.connect(self.handle_hide_activity)
        
        self.ui.pushButton_7.clicked.connect(self.handle_back)
        
    def handle_back(self):    
        self.previous_window.show()
        self.close()

    def handle_hide_activity(self):
        activity_id=self.ui.lineEdit.text()
        response,error=self.user_dao.hide_activity(self.textbook_id,self.chapter_id,self.section_id,self.block_id,activity_id)
        if response:
           QtWidgets.QMessageBox.information(self,'Information','Activity hidden status updated successfully!!') 
        else:
            QtWidgets.QMessageBox.warning(self, "Warning", str(error))    

        