import os
import sys
import random
import string
from PyQt6.QtWidgets import QApplication, QDialog, QMessageBox
from chapter02.password_generate import Ui_PasswordGenerate


class MyPasswordGenerate(QDialog, Ui_PasswordGenerate):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.load_websites()
        self.comboBox.lineEdit().textChanged.connect(self.on_website_text_changed)
        self.comboBox.setCurrentText('')  # 确保comboBox_website的内容为空
        self.comboBox.currentIndexChanged.connect(self.display_password)
        self.pushButton_generate_pwd.clicked.connect(self.generate_pwd)
        self.pushButton_save_pwd.clicked.connect(self.write_to_file)
        self.pwd = ''
        self.show()

    def generate_pwd(self):
        if not self.comboBox.currentText():
            QMessageBox.warning(self, '错误提醒', '请输入网址！')
            return

        checks = [
            (self.checkBox_upper, string.ascii_uppercase),
            (self.checkBox_lower, string.ascii_lowercase),
            (self.checkBox_digit, string.digits),
            (self.checkBox_marks, string.punctuation)
        ]

        characters = ''.join([chars for check, chars in checks if check.isChecked()])

        if not characters:
            QMessageBox.warning(self, '错误提醒', '请选择密码组合类型！')
            return

        password = [random.choice(chars) for check, chars in checks if check.isChecked()]

        pwd_length = self.lineEdit_pwd_length.text()
        if not pwd_length or not pwd_length.isdigit():
            QMessageBox.warning(self, '错误提醒', '请输入正确密码长度！')
            return

        password.extend(random.choices(characters, k=int(pwd_length) - len(password)))
        random.shuffle(password)
        self.pwd = ''.join(password)
        self.lineEdit_pwd.setText(self.pwd)

    def write_to_file(self):
        if not self.pwd:
            QMessageBox.warning(self, '错误提醒', '请先生成密码！')
            return

        filename = 'web_pwd.txt'
        lines = []
        if os.path.exists(filename):
            with open(filename, 'r') as file:
                lines = file.readlines()

        content_first_part = self.comboBox.currentText()
        new_line = f"{content_first_part}\t{self.pwd}\n"
        lines = [line if line.split()[0] != content_first_part else new_line for line in lines]
        if new_line not in lines:
            lines.append(new_line)

        with open(filename, 'w') as file:
            file.writelines(lines)

        # 更新comboBox_website的下拉列表
        if self.comboBox.findText(content_first_part) == -1:
            self.comboBox.addItem(content_first_part)

        QMessageBox.information(self, '信息提示', '密码保存成功！')

        # 重置控件内容
        self.comboBox.setCurrentText('')  # 清除comboBox_website的当前文本
        self.checkBox_upper.setChecked(False)  # 取消选中复选框
        self.checkBox_lower.setChecked(False)
        self.checkBox_digit.setChecked(False)
        self.checkBox_marks.setChecked(False)
        self.lineEdit_pwd_length.clear()  # 清除lineEdit_pwd_length的内容
        self.lineEdit_pwd.clear()  # 清除lineEdit_pwd的内容

    def load_websites(self):
        filename = 'web_pwd.txt'
        if os.path.exists(filename):
            with open(filename, 'r') as file:
                lines = file.readlines()
            for line in lines:
                website, _ = line.strip().split('\t')
                self.comboBox.addItem(website)

    def display_password(self, index):
        if index == -1:  # 没有选择任何项
            return
        filename = 'web_pwd.txt'
        if os.path.exists(filename):
            with open(filename, 'r') as file:
                lines = file.readlines()
            _, password = lines[index].strip().split('\t')
            self.lineEdit_pwd.setText(password)
            self.lineEdit_pwd_length.setText(str(len(password)))
    def on_website_text_changed(self, text):
        if not text:  # 如果文本为空
            self.lineEdit_pwd_length.clear()  # 清空密码长度
            self.lineEdit_pwd.clear()  # 清空密码


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myPasswordGenerate = MyPasswordGenerate()
    sys.exit(app.exec())
