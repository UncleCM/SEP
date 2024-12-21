import sys
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtMultimedia import QSoundEffect


class Animation_area(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.frame_no = 0
        self.images = [
            QPixmap("images/frame-" + str(i + 1) + ".png")
            for i in range(20)
        ]
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_value)
        self.timer.start(75)
        self.QSE = QSoundEffect()
        self.QSE.setSource(QUrl.fromLocalFile("sounds/rabbit_jump.wav"))

    def paintEvent(self, e):
        p = QPainter()
        p.begin(self)
        p.drawPixmap(QRect(0, 0, 320, 320), self.images[self.frame_no])
        p.end()

    def update_value(self):
        self.frame_no += 1
        if self.frame_no >= 20:
            self.frame_no = 0
            self.QSE.play()
        self.update()


class Simple_animation_window(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.anim_area = Animation_area()
        layout = QVBoxLayout()
        layout.addWidget(self.anim_area)
        self.pause_button = QPushButton("Pause")
        self.pause_button.clicked.connect(self.toggle_animation)
        layout.addWidget(self.pause_button)
        self.setLayout(layout)
        self.setMinimumSize(330, 400)

    def toggle_animation(self):
        if self.anim_area.timer.isActive():
            self.anim_area.timer.stop()
            self.pause_button.setText("Play")
        else:
            self.anim_area.timer.start()
            self.pause_button.setText("Pause")


def main():
    app = QApplication(sys.argv)
    w = Simple_animation_window()
    w.show()
    return app.exec()


if __name__ == "__main__":
    sys.exit(main())