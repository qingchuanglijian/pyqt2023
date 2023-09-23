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
        try:
            float(line_edit.text())
            return True
        except ValueError:
            QMessageBox.warning(self, '信息提醒', message)
            return False


    def calculate_bmi(self):
        if not all([self.validate_input(self.lineEdit_height, '请输入正确身高！'),
                    self.validate_input(self.lineEdit_weight, '请输入正确体重！')]):
            return

        height = float(self.lineEdit_height.text()) / 100
        weight = float(self.lineEdit_weight.text())
        bmi = round(weight / (height ** 2), 1)

        bmi_categories = {
            (0, 18.4): '消瘦',
            (18.5, 23.9): '正常',
            (24, 27.9): '超重'
        }
        calculate_result = next((category for (start, end), category in bmi_categories.items() if start < bmi <= end), '肥胖')

        ideal_weight = round((height ** 2) * 22, 1)
        self.label_title.setText(f'您的计算结果：{bmi}')
        self.label_result.setText(f'BMI:{bmi}属于{calculate_result},您的理想体重为：{ideal_weight}KG')

        self.lineEdit_height.setText('')
        self.lineEdit_weight.setText('')




if __name__ == '__main__':
    app = QApplication(sys.argv)
    myCalculateBmi = MyCalculateBmi()
    sys.exit(app.exec())
