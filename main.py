import sys
from PyQt5 import QtWidgets
from design import Ui_MainWindow
from calc import Ui_Form
import os
import sys

class ExampleApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btnBrowse.clicked.connect(self.browse_folder)
        self.calcButton.clicked.connect()
    def browse_folder(self):
        self.listWidget.clear()
        directory = QtWidgets.QFileDialog.getExistingDirectory(self, "Выберите папку")
        if directory:
            for file_name in os.listdir(directory):
                self.listWidget.addItem(file_name)

class CCalculator(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)



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



