import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from UI.output import Ui_Dialog

def say_hello():
    print("Hello World")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialog = QDialog()
    ui = Ui_Dialog()
    ui.setupUi(dialog)
    ui.hello_btn.clicked.connect(say_hello)
    dialog.show()
    sys.exit(app.exec())