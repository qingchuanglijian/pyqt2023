import os

from PyQt6.QtWidgets import QApplication,QDialog,QFileDialog,QMessageBox
import sys
from category_file import  Ui_FileCategory
class MyFileCategory(QDialog,Ui_FileCategory):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_chose_filepath.clicked.connect(
            self.chose_filepath
        )
        self.pushButton_category_file.clicked.connect(
            self.category_file
        )
        self.show()

    def chose_filepath(self):
        directory = QFileDialog.getExistingDirectory(self,'选择文件夹',os.getcwd())
        if directory:
            self.lineEdit.setText(directory)

    def category_file(self):
        if self.lineEdit.text():
            pass
if __name__ == '__main__':
    app = QApplication(sys.argv)
    myFileCategory = MyFileCategory()
    sys.exit(app.exec())