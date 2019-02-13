import sys
from PyQt5 import QtWidgets, QtCore
from design import Ui_MainWindow
from calc import Ui_Form
import os
import sys
import re

class ExampleApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btnBrowse.clicked.connect(self.browse_folder)
        self.calc = CCalculator(self)
        self.calcButton.clicked.connect(self.calc.show)
    def browse_folder(self):
        self.listWidget.clear()
        directory = QtWidgets.QFileDialog.getExistingDirectory(self, "Выберите папку")
        if directory:
            for file_name in os.listdir(directory):
                self.listWidget.addItem(file_name)


class CCalculator(QtWidgets.QWidget, Ui_Form):
    def __init__(self, parent):
        super().__init__()
        self.result =''
        self.operators = ['+', '-', '*', '/', '^']
        self.setupUi(self)
        self.oneButton.clicked.connect(self.setOneButton)
        self.twoButton.clicked.connect(self.setTwoButton)
        self.threeButton.clicked.connect(self.setThreeButton)
        self.fourButton.clicked.connect(self.setFourButton)
        self.fiveButton.clicked.connect(self.setFiveButton)
        self.sixButton.clicked.connect(self.setSixButton)
        self.sevenButton.clicked.connect(self.setSevenButton)
        self.eightButton.clicked.connect(self.setEightButton)
        self.nineButton.clicked.connect(self.setNineButton)
        self.zeroButton.clicked.connect(self.setZeroButton)
        self.zzButton.clicked.connect(self.setZZButton)
        self.plusButton.clicked.connect(self.setPlusButton)
        self.minusButton.clicked.connect(self.setMinusButton)
        self.umnButton.clicked.connect(self.setUmnButton)
        self.delenButton.clicked.connect(self.setDelenButton)
        self.deleteButton.clicked.connect(self.setDeleteButton)
        self.procentButton.clicked.connect(self.setProcentButton)
        self.ravnoButton.clicked.connect(self.setRavnoButton)
        self.clearButton.clicked.connect(self.setClearButton)
    def setOneButton(self):
        self.result += '1'
        self.lineEdit.setText(self.result)
    def setTwoButton(self):
        self.result += '2'
        self.lineEdit.setText(self.result)
    def setThreeButton(self):
        self.result += '3'
        self.lineEdit.setText(self.result)
    def setFourButton(self):
        self.result += '4'
        self.lineEdit.setText(self.result)
    def setFiveButton(self):
        self.result += '5'
        self.lineEdit.setText(self.result)
    def setSixButton(self):
        self.result += '6'
        self.lineEdit.setText(self.result)
    def setSevenButton(self):
        self.result += '7'
        self.lineEdit.setText(self.result)
    def setEightButton(self):
        self.result += '8'
        self.lineEdit.setText(self.result)
    def setNineButton(self):
        self.result += '9'
        self.lineEdit.setText(self.result)
    def setZeroButton(self):
        self.result += '0'
        self.lineEdit.setText(self.result)
    def setZZButton(self):
        self.result += '00'
        self.lineEdit.setText(self.result)
    def setClearButton(self):
        self.lineEdit.clear(self)

    def setDotButton(self):
        self.result += '.'

    def setPlusButton(self):
        #а пусть оно так для всех знаков и работает, все равно нам потом вот разделять строку.
        #тут надо еще предусмотреть проверку на последний введенный символ строки, как в калькуляторах,
        #не может же быть у них там подряд два плюса. Последний знак, если он оператор, надо менять
        self.result += '+'
        self.lineEdit.setText(self.result)
    #доделай пока все это, потом надо подумать, а как сделать так, чтобы операции выполнялись по порядку :)
    #Например, умножение всегда впереди сложения.
        def setMinusButton(self):
        self.result += '-'
        self.lineEdit.setText(self.result)

    def setUmnButton(self):
        pass
    def setDelenButton(self):
        pass

    def setDeleteButton(self):
        pass

    def setProcentButton(self):
        pass

    def setRavnoButton(self):
        self.split_args()

    def split_args(self):
        #это работает примерно так
        #шаблоном разбивается наша строка, и мы получаем аргументы. Вторым шаблоном неплохо
        #получить еще наши все знаки, а дальше просто произвести получившиеся математические операции (тут можно
        #посмотреть в сторону NumPy) в статье написаны паттерны, как это сделать.
        splitted_string = self.result
        arguments = re.split(r'[+*/-]', splitted_string )
        print(arguments)



sys._excepthook = sys.excepthook
def my_exception_hook(exctype,value,traceback):
    print(exctype,value,traceback)
    sys._excepthook(exctype, value, traceback)
    sys.exit(1)
sys.excepthook = my_exception_hook

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = ExampleApp()
    window.show()
    try:
        sys.exit(app.exec_())
    except:
        print("exit")

if __name__ == '__main__':
    main()



