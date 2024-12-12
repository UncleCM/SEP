import sys
import time
from PySide6.QtWidgets import *
from PySide6.QtCore import *


class digital_clock(QWidget):
    def __init__(self):
        super().__init__()
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.showTime)
        self.timer.start(1000)

        self.label = QLabel(self)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        self.setLayout(layout)
        self.showTime()

    def showTime(self):
        current_time = time.strftime("%H:%M:%S")
        self.label.setText(current_time)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    clock = digital_clock()
    clock.show()
    sys.exit(app.exec())