import sys
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QLabel

def say_hello():
    print('Hello World!')

if __name__ == "__main__":
    app = QApplication(sys.argv)

    w = QWidget()
    w.setWindowTitle('Simple')
    btn = QPushButton('Button', w)
    btn.clicked.connect(say_hello)
    w.show()

    sys.exit(app.exec())