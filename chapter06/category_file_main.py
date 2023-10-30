import os
import shutil

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
            choose_path = self.lineEdit.text()
            for dirpath,dirnames,filenames in os.walk(choose_path):
                for filename in filenames:
                    filepath = os.path.join(dirpath,filename)
                    name,extension = os.path.splitext(filename)
                    if extension:
                        extension = extension[1:]
                        dest_dir = os.path.join(choose_path,extension)
                        if not os.path.exists(dest_dir):
                            os.makedirs(dest_dir)
                        dest_file = os.path.join(dest_dir,filename)
                        shutil.move(filepath,dest_file)
            QMessageBox.information(self,'信息提示','文件目录整理完成！')
        else:
            QMessageBox.warning(self,'信息警告','请选择文件路径')
            return
if __name__ == '__main__':
    app = QApplication(sys.argv)
    myFileCategory = MyFileCategory()
    sys.exit(app.exec())