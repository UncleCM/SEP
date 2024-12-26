import sys
from PySide6.QtWidgets import QApplication, QDialog, QListWidgetItem, QMessageBox, QLabel, QVBoxLayout, QWidget, QFrame
from PySide6.QtCore import Qt, QTimer, QRect, QUrl
from PySide6.QtGui import QPixmap, QPainter
from PySide6.QtMultimedia import QSoundEffect
from Q1 import Ui_Dialog

class AnimationArea(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.frame_no = 0
        self.images = []
        for i in range(9):
            path = f"images/frame-{i+1}.png"
            pixmap = QPixmap(path)
            if pixmap.isNull():
                print(f"Failed to load {path}")
            self.images.append(pixmap)
        
        self.setStyleSheet("background-color: white; border: 1px solid black;")
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_value)
        self.timer.start(75)
        
    def paintEvent(self, e):
        if not self.images:
            return
        p = QPainter()
        p.begin(self)
        p.drawPixmap(self.rect(), self.images[self.frame_no])
        p.end()
        
    def update_value(self):
        if not self.images:
            return
        self.frame_no = (self.frame_no + 1) % len(self.images)
        self.update()

class TodoList(QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init_ui()
        self.setup_connections()
        self.setup_animation()
        self.setup_sounds()
        
    def init_ui(self):
        self.setWindowTitle("Todo List")
        self.setMinimumSize(640, 1000)
        
        self.Add_btn.setStyleSheet("background-color: rgb(32, 255, 58)")
        self.MarkComplete_btn.setStyleSheet("background-color: rgb(34, 226, 255)")
        self.Delete_btn.setStyleSheet("background-color: rgb(255, 25, 29)")
        
    def setup_sounds(self):
        self.add_sound = QSoundEffect()
        self.add_sound.setSource(QUrl.fromLocalFile("sounds/Wah.wav"))
        
        self.delete_sound = QSoundEffect()
        self.delete_sound.setSource(QUrl.fromLocalFile("sounds/gunshot.wav"))
        
        self.clear_sound = QSoundEffect()
        self.clear_sound.setSource(QUrl.fromLocalFile("sounds/a-10.wav"))

        self.mark_complete_sound = QSoundEffect()
        self.mark_complete_sound.setSource(QUrl.fromLocalFile("sounds/EcoWah.wav"))
        
    def setup_animation(self):
        window_width = self.width()
        margin = 40
        frame_width = window_width - (margin * 2)
        frame_height = 322

        self.anim_frame = QFrame(self)
        self.anim_frame.setGeometry(margin, 620, frame_width, frame_height)
        self.anim_frame.setFrameStyle(QFrame.Box)
        
        self.anim_area = AnimationArea(self.anim_frame)
        self.anim_area.setFixedSize(frame_width - 2, frame_height - 2)
        self.anim_area.move(1, 1)

    def setup_connections(self):
        self.Add_btn.clicked.connect(self.add_task)
        self.MarkComplete_btn.clicked.connect(self.mark_complete)
        self.Delete_btn.clicked.connect(self.delete_task)
        self.Clear_btn.clicked.connect(self.clear_all)
        self.Input.returnPressed.connect(self.add_task)
        
    def add_task(self):
        task_text = self.Input.text().strip()
        if task_text:
            item = QListWidgetItem(task_text)
            item.setFlags(item.flags() | Qt.ItemIsUserCheckable)
            item.setCheckState(Qt.Unchecked)
            self.List_Output.addItem(item)
            self.Input.clear()
            self.add_sound.play()
            
    def mark_complete(self):
        current_item = self.List_Output.currentItem()
        if current_item:
            current_state = current_item.checkState()
            new_state = Qt.Checked if current_state == Qt.Unchecked else Qt.Unchecked
            current_item.setCheckState(new_state)
            font = current_item.font()
            font.setStrikeOut(new_state == Qt.Checked)
            current_item.setFont(font)
            self.mark_complete_sound.play()
            
    def delete_task(self):
        current_item = self.List_Output.currentItem()
        if current_item:
            self.List_Output.takeItem(self.List_Output.row(current_item))
            self.delete_sound.play()
            
    def clear_all(self):
        if self.List_Output.count() > 0:
            reply = QMessageBox.question(
                self, "Confirm Clear All",
                "Are you sure you want to clear all tasks?",
                QMessageBox.Yes | QMessageBox.No
            )
            if reply == QMessageBox.Yes:
                self.List_Output.clear()
                self.clear_sound.play()
                
    def count_tasks(self):
        return self.List_Output.count()
        
    def count_completed_tasks(self):
        completed = 0
        for i in range(self.List_Output.count()):
            if self.List_Output.item(i).checkState() == Qt.Checked:
                completed += 1
        return completed
        
    def closeEvent(self, event):
        reply = QMessageBox.question(
            self, "Confirm Exit",
            "Are you sure you want to exit?",
            QMessageBox.Yes | QMessageBox.No
        )
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

if __name__ == "__main__":
    QApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    app = QApplication(sys.argv)
    window = TodoList()
    window.show()
    sys.exit(app.exec())