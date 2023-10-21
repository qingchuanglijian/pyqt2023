from PyQt6.QtWidgets import QApplication,QWidget,QMessageBox
import sys

from chapter03.num_calculate import Ui_CalculateNum


class MyCalculateNum(QWidget,Ui_CalculateNum):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.currentInput = ""
        self.previousInput = ""
        self.currentOperator = ""
        self.digitButtons = [self.pushButton_0,self.pushButton_1,self.pushButton_2,self.pushButton_3,self.pushButton_4/
                               self.pushButton_5,self.pushButton_6,self.pushButton_7,self.pushButton_8,self.pushButton_9/
                               self.pushButton_00]
        self.operatorButtons = [self.pushButton_add,self.pushButton_sub,self.pushButton_mul,self.pushButton_divide]
        for btn in self.digitButtons:
            btn.clicked.connect(self.digitClicked)
        self.show()

    def digitClicked(self):
        button = self.sender()
        if button:
            digit = button.text
            self.currentInput += button.text
            self.lineEdit_result.setText(self.currentInput)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myCalculateNum=MyCalculateNum()
    sys.exit(app.exec())