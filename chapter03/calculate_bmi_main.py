from PyQt6.QtWidgets import QApplication, QWidget, QMessageBox
import sys
from chapter03.calculate_bmi import Ui_CalculateBmi


class MyCalculateBmi(QWidget, Ui_CalculateBmi):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_calculate.clicked.connect(self.calculate_bmi)
        self.show()

    def validate_input(self, line_edit, message):
        if not line_edit.text():
            QMessageBox.warning(self, '信息提醒', message)
            return False
        try:
            float(line_edit.text())
        except ValueError:
            QMessageBox.warning(self, '信息提醒', message)
            return False
        return True

    def calculate_bmi(self):
        if not self.validate_input(self.lineEdit_height, '请输入正确身高！'):
            return
        if not self.validate_input(self.lineEdit_weight, '请输入正确体重！'):
            return

        height = float(self.lineEdit_height.text()) / 100
        weight = float(self.lineEdit_weight.text())
        bmi = round(weight / (height ** 2), 1)

        if bmi <= 18.4:
            calculate_result = '消瘦'
        elif 18.5 < bmi <= 23.9:
            calculate_result = '正常'
        elif 24 <= bmi <= 27.9:
            calculate_result = '超重'
        else:
            calculate_result = '肥胖'

        ideal_weight = round((height ** 2) * 22, 1)
        self.label_title.setText(f'您的计算结果：{bmi}')
        self.label_result.setText(f'BMI:{bmi}属于{calculate_result},您的理想体重为：{ideal_weight}KG')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myCalculateBmi = MyCalculateBmi()
    sys.exit(app.exec())
