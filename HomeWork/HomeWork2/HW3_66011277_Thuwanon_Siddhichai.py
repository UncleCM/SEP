import sys
from PySide6.QtWidgets import QApplication, QDialog, QListWidgetItem, QMessageBox
from PySide6.QtCore import Qt
from Q1 import Ui_Dialog

class TodoList(QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init_ui()
        self.setup_connections()
        
    def init_ui(self):
        self.setWindowTitle("Todo List")
        self.setMinimumSize(640, 615)
        
        self.current_task = ""
        
        self.Add_btn.setStyleSheet("background-color: rgb(32, 255, 58)")
        self.MarkComplete_btn.setStyleSheet("background-color: rgb(34, 226, 255)")
        self.Delete_btn.setStyleSheet("background-color: rgb(255, 25, 29)")
        
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
            
    def mark_complete(self):
        current_item = self.List_Output.currentItem()
        
        if current_item:
            current_state = current_item.checkState()
            new_state = Qt.Checked if current_state == Qt.Unchecked else Qt.Unchecked
            current_item.setCheckState(new_state)
            
            font = current_item.font()
            font.setStrikeOut(new_state == Qt.Checked)
            current_item.setFont(font)
            
    def delete_task(self):
        current_item = self.List_Output.currentItem()
        
        if current_item:
            self.List_Output.takeItem(self.List_Output.row(current_item))
            
    def clear_all(self):
        if self.List_Output.count() > 0:
            reply = QMessageBox.question(
                self,
                "Confirm Clear All",
                "Are you sure you want to clear all tasks?",
                QMessageBox.Yes | QMessageBox.No
            )
            
            if reply == QMessageBox.Yes:
                self.List_Output.clear()
        
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
            self,
            "Confirm Exit",
            "Are you sure you want to exit?",
            QMessageBox.Yes | QMessageBox.No
        )
        
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TodoList()
    window.show()
    sys.exit(app.exec())