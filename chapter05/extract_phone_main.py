import sys
from PyQt6.QtWidgets import QApplication, QWidget, QMessageBox
from extract_phone import Ui_ExtractPhoneNum
from re_file import re_compile

class MyExtractPhoneNum(QWidget, Ui_ExtractPhoneNum):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_extract.clicked.connect(lambda :self.extract_information(flag='phone'))
        self.pushButton_sfz.clicked.connect(lambda: self.extract_information(flag='sfz'))
        self.pushButton_banknum.clicked.connect(lambda: self.extract_information(flag='bank'))
        self.pushButton_email.clicked.connect(lambda: self.extract_information(flag='email'))
        self.pushButton_carnum.clicked.connect(lambda: self.extract_information(flag='car'))
        self.pushButton_ipdir.clicked.connect(lambda: self.extract_information(flag='ip'))
        self.pushButton_paste.clicked.connect(self.paste_phone)
        self.pushButton_clear.clicked.connect(self.phone_clear)
        self.show()

    def _check_text_empty(self, text: str, message: str) -> bool:
        if not text:
            self._show_message('信息提示', message)
            return True
        return False

    def _show_message(self, title: str, message: str):
        QMessageBox.information(self, title, message)

    def extract_information(self, flag):
        text = self.plainTextEdit_input.toPlainText()

        if self._check_text_empty(text, '请输入数据！'):
            return

        # 使用字典来映射flag到其对应的描述
        flag_descriptions = {
            'phone': '手机号',
            'sfz': '身份证号码',
            'email': '电子邮箱',
            'car': '车牌号码',
            'ip': 'IP地址',
            'bank': '银行卡号'
        }

        if flag in flag_descriptions:
            extracted_data = re_compile(flag).findall(text)
            extracted_data = '\n'.join(extracted_data)
            self.plainTextEdit_result.setPlainText(extracted_data)
            if not extracted_data:
                self._show_message('信息提示', f'无{flag_descriptions[flag]}信息！')
                return
            self._show_message('信息提示', f'{flag_descriptions[flag]}提取成功！')
    def paste_phone(self):
        text = self.plainTextEdit_result.toPlainText()
        if self._check_text_empty(text, '结果为空！'):
            return
        clipboard = QApplication.clipboard()
        clipboard.setText(text)
        self._show_message('信息提示', '复制成功！')
    def phone_clear(self):
        self.plainTextEdit_input.clear()
        self.plainTextEdit_result.clear()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myExtractPhoneNum = MyExtractPhoneNum()
    sys.exit(app.exec())
