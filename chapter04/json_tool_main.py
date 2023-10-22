import sys
import json

from PyQt6.QtWidgets import QApplication, QWidget, QMessageBox

from json_tool import Ui_TranslateJson


class MyTranslateJson(QWidget, Ui_TranslateJson):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_formate.clicked.connect(lambda: self.process_json(formatted=True))
        self.pushButton_unformate.clicked.connect(lambda: self.process_json(formatted=False))
        self.pushButton_paste.clicked.connect(self.json_paste)
        self.pushButton_clear.clicked.connect(self.json_clear)
        self.show()

    def _check_text_empty(self, text, message):
        if not text:
            QMessageBox.warning(self, '信息提示', message)
            return True
        return False

    def process_json(self, formatted=True):
        text = self.textEdit_json_text.toPlainText()
        if self._check_text_empty(text, '请输入json内容！'):
            return

        if formatted:
            text_result = json.dumps(json.loads(text), indent=4, ensure_ascii=False)
        else:
            text_result = json.dumps(json.loads(text), ensure_ascii=False)

        self.textEdit_json_text.setText(text_result)
        QMessageBox.information(self, '信息提示', '处理完成！')

    def json_paste(self):
        text = self.textEdit_json_text.toPlainText()
        if self._check_text_empty(text, 'json内容为空！'):
            return
        clipboard = QApplication.clipboard()
        clipboard.setText(text)
        QMessageBox.information(self, '信息提示', '复制成功！！')

    def json_clear(self):
        self.textEdit_json_text.clear()
        self.textEdit_json_text.clear()
        QMessageBox.information(self, '信息提示', '结果清空！！')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myTranslateJson = MyTranslateJson()
    sys.exit(app.exec())
