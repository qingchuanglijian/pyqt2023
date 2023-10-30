import os
import shutil
import sys

from PyQt6.QtWidgets import QApplication, QDialog, QFileDialog, QMessageBox
from category_file import Ui_FileCategory


class MyFileCategory(QDialog, Ui_FileCategory):
    INFO_MESSAGE = '文件目录整理完成！'
    WARNING_MESSAGE = '请选择文件路径'

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_chose_filepath.clicked.connect(self.chose_filepath)
        self.pushButton_category_file.clicked.connect(self.category_file)
        self.show()

    def chose_filepath(self):
        directory = QFileDialog.getExistingDirectory(self, '选择文件夹', os.getcwd())
        if directory:
            self.lineEdit.setText(directory)

    def category_file(self):
        choose_path = self.lineEdit.text()
        if choose_path:
            self.organize_files(choose_path)
            QMessageBox.information(self, '信息提示', self.INFO_MESSAGE)
        else:
            QMessageBox.warning(self, '信息警告', self.WARNING_MESSAGE)

    def organize_files(self, path):
        for dirpath, _, filenames in os.walk(path):
            for filename in filenames:
                filepath = os.path.join(dirpath, filename)
                _, extension = os.path.splitext(filename)
                if extension:
                    extension = extension[1:]
                    dest_dir = os.path.join(path, extension)
                    if not os.path.exists(dest_dir):
                        os.makedirs(dest_dir)
                    dest_file = os.path.join(dest_dir, filename)
                    try:
                        shutil.move(filepath, dest_file)
                    except Exception as e:
                        print(f"Error moving file {filepath}: {e}")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myFileCategory = MyFileCategory()
    sys.exit(app.exec())
