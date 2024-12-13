import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from UI.output3 import Ui_KMITL_Phone

class Phone(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_KMITL_Phone()
        self.ui.setupUi(self)

        self.num = ""

        self.ui.one.clicked.connect(self.one)
        self.ui.two.clicked.connect(self.two)
        self.ui.three.clicked.connect(self.three)
        self.ui.four.clicked.connect(self.four)
        self.ui.five.clicked.connect(self.five)
        self.ui.six.clicked.connect(self.six)
        self.ui.seven.clicked.connect(self.seven)
        self.ui.eight.clicked.connect(self.eight)
        self.ui.nine.clicked.connect(self.nine)
        self.ui.star.clicked.connect(self.star)
        self.ui.hash.clicked.connect(self.hash)
        self.ui.zero.clicked.connect(self.zero)
        self.ui.talk.clicked.connect(self.talk)
        self.ui.delete_2.clicked.connect(self.delete_2)
        
        
    def one(self):
        self.num += "1"
        self.ui.num.setText(self.num)
    
    def two(self):
        self.num += "2"
        self.ui.num.setText(self.num)

    def three(self):
        self.num += "3"
        self.ui.num.setText(self.num)

    def four(self):
        self.num += "4"
        self.ui.num.setText(self.num)

    def five(self):
        self.num += "5"
        self.ui.num.setText(self.num) 
    
    def six(self):
        self.num += "6"
        self.ui.num.setText(self.num)

    def seven(self):
        self.num += "7"
        self.ui.num.setText(self.num)

    def eight(self):
        self.num += "8"
        self.ui.num.setText(self.num)

    def nine(self):
        self.num += "9"
        self.ui.num.setText(self.num)

    def star(self):
        self.num += "*"
        self.ui.num.setText(self.num)
    
    def hash(self):
        self.num += "#"
        self.ui.num.setText(self.num)

    def zero(self):
        self.num += "0"
        self.ui.num.setText(self.num)


    def delete_2(self):
        self.num = self.num[:-1]
        self.ui.num.setText(self.num)

    def talk(self):
        self.ui.num.setText("Dialling: " + self.num)



if __name__ == "__main__":
    w = QApplication(sys.argv)
    window = Phone()
    window.show()
    sys.exit(w.exec_())