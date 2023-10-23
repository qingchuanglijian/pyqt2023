import os
import sys
import random
import string

from PyQt6.QtWidgets import (
    QApplication, QDialog, QMessageBox
)

from chapter02.password_generate import Ui_PasswordGenerate


class MyPasswordGenerate(QDialog, Ui_PasswordGenerate):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton_generate_pwd.clicked.connect(
            self.generate_pwd
        )
        self.pushButton_save_pwd.clicked.connect(
            self.write_to_file
        )
        self.pwd = ''
        self.show()

    def generate_pwd(self):
        if not self.lineEdit_website.text():
            QMessageBox.warning(self, '错误提醒', '请输入网址！')
            return
        if not (self.checkBox_upper.isChecked() | self.checkBox_lower.isChecked() | self.checkBox_digit.isChecked() | self.checkBox_marks.isChecked()):
            QMessageBox.warning(self, '错误提醒', '请选择密码组合类型！')
            return
        characters = ''
        if self.checkBox_upper.isChecked():
            characters += string.ascii_uppercase
        if self.checkBox_lower.isChecked():
            characters += string.ascii_lowercase
        if self.checkBox_digit.isChecked():
            characters += string.digits
        if self.checkBox_marks.isChecked():
            characters += string.punctuation

        # 确保每种选择的类型至少出现一次
        password = []
        if self.checkBox_upper.isChecked():
            password.append(random.choice(string.ascii_uppercase))
        if self.checkBox_lower.isChecked():
            password.append(random.choice(string.ascii_lowercase))
        if self.checkBox_digit.isChecked():
            password.append(random.choice(string.digits))
        if self.checkBox_marks.isChecked():
            password.append(random.choice(string.punctuation))

        # 根据指定的长度生成密码

        pwd_length = self.lineEdit_pwd_length.text()
        if not pwd_length or not pwd_length.isdigit():
            QMessageBox.warning(self, '错误提醒', '请输入正确密码长度！')
            return
        for i in range(int(pwd_length) - len(password)):
            password.append(random.choice(characters))
        # 打乱密码字符顺序
        random.shuffle(password)
        self.pwd = ''.join(password)
        self.lineEdit_pwd.setText(self.pwd)

    def write_to_file(self):
        if not self.pwd:
            QMessageBox.warning(self, '错误提醒', '请先生成密码！')
            return
        lines = []

        # 检查文件是否存在，如果存在则读取内容
        if os.path.exists('web_pwd.txt'):
            with open('web_pwd.txt', 'r') as file:
                lines = file.readlines()

        # 分割输入内容的第一部分
        content_first_part = self.lineEdit_website.text()

        # 检查内容的第一部分是否已经存在于文件中
        content_found = False
        for index, line in enumerate(lines):
            line_first_part = line.strip().split()[0]
            if content_first_part == line_first_part:
                content_found = True
                lines[index] = f"{content_first_part}\t{self.pwd}\n"  # 覆盖此条数据
                break

        # 如果内容不存在，追加到列表末尾
        if not content_found:
            lines.append(f"{content_first_part}\t{self.pwd}\n")

        # 写回文件
        with open("web_pwd.txt", 'w') as file:
            file.writelines(lines)

        QMessageBox.information(self, '信息提示', '密码保存成功！')


if __name__ == '__main__':
    app = QApplication(sys.argv)

    myPasswordGenerate = MyPasswordGenerate()

    sys.exit(app.exec())
