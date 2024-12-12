import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *

class Currency_Convertor(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.setWindowTitle('Currency Convertor')
        self.num = 0
        vbox = QVBoxLayout()
        self.label = QLabel(self)
        self.label.setText("Thai Baht to US Dollar")
        vbox.addWidget(self.label)
        self.THB_entry = QLineEdit(self)
        vbox.addWidget(self.THB_entry)
        self.convert_to_usd = QPushButton('Convert', self)
        self.convert_to_usd.clicked.connect(self.to_usd)
        vbox.addWidget(self.convert_to_usd) 
        self.label3 = QLabel(self)
        self.label3.setText("US Dollar to Thai Baht")
        vbox.addWidget(self.label3)
        self.label4 = QLabel(self)
        self.USD_entry = QLineEdit(self)
        vbox.addWidget(self.USD_entry)

        self.convert = QPushButton('Convert', self)
        self.convert.clicked.connect(self.to_thb)
        vbox.addWidget(self.convert)
        self.setLayout(vbox)
        self.show()

    def to_usd(self):
        dilog = QDialog(self)
        dilog.setWindowTitle("Result")
        layout = QVBoxLayout()
        label = QLabel(self)
        label.setText(str(float(self.THB_entry.text())/35))
        layout.addWidget(label)
        close_bth = QPushButton('Close', self)
        close_bth.clicked.connect(dilog.close)
        layout.addWidget(close_bth)
        dilog.setLayout(layout)
        dilog.show()

    def to_thb(self):
        dilog = QDialog(self)
        dilog.setWindowTitle("Result")
        layout = QVBoxLayout()
        label = QLabel(self)
        label.setText(str(float(self.USD_entry.text())*35))
        layout.addWidget(label)
        close_bth = QPushButton('Close', self)
        close_bth.clicked.connect(dilog.close)
        layout.addWidget(close_bth)
        dilog.setLayout(layout)
        dilog.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Currency_Convertor()
    sys.exit(app.exec())

