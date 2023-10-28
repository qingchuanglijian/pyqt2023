# Form implementation generated from reading ui file 'category_file.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_FileCategory(object):
    def setupUi(self, FileCategory):
        FileCategory.setObjectName("FileCategory")
        FileCategory.resize(402, 240)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("文件.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        FileCategory.setWindowIcon(icon)
        FileCategory.setStyleSheet(".QPushButton {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #f6f7f8, stop: 1 #dadbdc);\n"
"    border-radius: 5px;\n"
"    border: 1px solid #dadbdc;\n"
"    box-shadow: 2px 2px 2px rgba(0, 0, 0, 0.1);\n"
"    color: #333;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #e6e7e8, stop: 1 #c8c9ca);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #dadbdc, stop: 1 #b0b1b3);\n"
"}\n"
"\n"
".QLabel{\n"
"     font-weight: bold;\n"
"}\n"
"")
        self.verticalLayout = QtWidgets.QVBoxLayout(FileCategory)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit = QtWidgets.QLineEdit(parent=FileCategory)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.pushButton_chose_filepath = QtWidgets.QPushButton(parent=FileCategory)
        self.pushButton_chose_filepath.setObjectName("pushButton_chose_filepath")
        self.horizontalLayout.addWidget(self.pushButton_chose_filepath)
        self.pushButton_category_file = QtWidgets.QPushButton(parent=FileCategory)
        self.pushButton_category_file.setObjectName("pushButton_category_file")
        self.horizontalLayout.addWidget(self.pushButton_category_file)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.plainTextEdit_result = QtWidgets.QPlainTextEdit(parent=FileCategory)
        self.plainTextEdit_result.setObjectName("plainTextEdit_result")
        self.verticalLayout.addWidget(self.plainTextEdit_result)

        self.retranslateUi(FileCategory)
        QtCore.QMetaObject.connectSlotsByName(FileCategory)

    def retranslateUi(self, FileCategory):
        _translate = QtCore.QCoreApplication.translate
        FileCategory.setWindowTitle(_translate("FileCategory", "文件分类工具"))
        self.pushButton_chose_filepath.setText(_translate("FileCategory", "选择文件夹"))
        self.pushButton_category_file.setText(_translate("FileCategory", "整理文件夹"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FileCategory = QtWidgets.QDialog()
    ui = Ui_FileCategory()
    ui.setupUi(FileCategory)
    FileCategory.show()
    sys.exit(app.exec())
