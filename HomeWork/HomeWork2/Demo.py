from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                              QHBoxLayout, QLineEdit, QPushButton, QListWidget,
                              QListWidgetItem, QMessageBox, QCheckBox, QLabel)
from PySide6.QtCore import Qt, QSize
import json
import sys
from datetime import datetime

class TodoListApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Todo List")
        self.setMinimumSize(QSize(500, 600))
        
        # Create central widget and main layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)
        
        # Create title
        title_label = QLabel("Todo List")
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet("""
            font-size: 24px;
            font-weight: bold;
            margin: 10px;
            color: #2c3e50;
        """)
        main_layout.addWidget(title_label)
        
        # Create input area
        input_layout = QHBoxLayout()
        
        # Task input
        self.task_input = QLineEdit()
        self.task_input.setPlaceholderText("Enter a new task...")
        self.task_input.returnPressed.connect(self.add_task)
        input_layout.addWidget(self.task_input)
        
        # Add button
        add_button = QPushButton("Add Task")
        add_button.clicked.connect(self.add_task)
        add_button.setStyleSheet("""
            QPushButton {
                background-color: #2ecc71;
                color: white;
                border: none;
                padding: 5px 15px;
                border-radius: 3px;
            }
            QPushButton:hover {
                background-color: #27ae60;
            }
        """)
        input_layout.addWidget(add_button)
        
        main_layout.addLayout(input_layout)
        
        # Create list widget
        self.task_list = QListWidget()
        self.task_list.setStyleSheet("""
            QListWidget {
                border: 1px solid #bdc3c7;
                border-radius: 3px;
            }
            QListWidget::item {
                padding: 5px;
                border-bottom: 1px solid #ecf0f1;
            }
            QListWidget::item:selected {
                background-color: #e8f0fe;
                color: black;
            }
        """)
        main_layout.addWidget(self.task_list)
        
        # Create buttons layout
        button_layout = QHBoxLayout()
        
        # Complete button
        complete_button = QPushButton("Mark Complete")
        complete_button.clicked.connect(self.toggle_task)
        complete_button.setStyleSheet("""
            QPushButton {
                background-color: #3498db;
                color: white;
                border: none;
                padding: 5px 15px;
                border-radius: 3px;
            }
            QPushButton:hover {
                background-color: #2980b9;
            }
        """)
        button_layout.addWidget(complete_button)
        
        # Delete button
        delete_button = QPushButton("Delete Task")
        delete_button.clicked.connect(self.delete_task)
        delete_button.setStyleSheet("""
            QPushButton {
                background-color: #e74c3c;
                color: white;
                border: none;
                padding: 5px 15px;
                border-radius: 3px;
            }
            QPushButton:hover {
                background-color: #c0392b;
            }
        """)
        button_layout.addWidget(delete_button)
        
        # Clear all button
        clear_button = QPushButton("Clear All")
        clear_button.clicked.connect(self.clear_all)
        clear_button.setStyleSheet("""
            QPushButton {
                background-color: #95a5a6;
                color: white;
                border: none;
                padding: 5px 15px;
                border-radius: 3px;
            }
            QPushButton:hover {
                background-color: #7f8c8d;
            }
        """)
        button_layout.addWidget(clear_button)
        
        main_layout.addLayout(button_layout)
        
        # Create status label
        self.status_label = QLabel("")
        self.status_label.setAlignment(Qt.AlignCenter)
        self.status_label.setStyleSheet("color: #27ae60; margin: 5px;")
        main_layout.addWidget(self.status_label)
        
        # Load saved tasks
        self.load_tasks()
        
    def add_task(self):
        task_text = self.task_input.text().strip()
        if task_text:
            # Create item with timestamp
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
            item = QListWidgetItem(f"{task_text} (Added: {timestamp})")
            item.setFlags(item.flags() | Qt.ItemIsUserCheckable)
            item.setCheckState(Qt.Unchecked)
            
            self.task_list.addItem(item)
            self.task_input.clear()
            self.save_tasks()
            self.status_label.setText("Task added successfully!")
        else:
            self.status_label.setText("Please enter a task!")
            
    def toggle_task(self):
        current_item = self.task_list.currentItem()
        if current_item:
            current_state = current_item.checkState()
            new_state = Qt.Checked if current_state == Qt.Unchecked else Qt.Unchecked
            current_item.setCheckState(new_state)
            
            # Update item appearance
            font = current_item.font()
            font.setStrikeOut(new_state == Qt.Checked)
            current_item.setFont(font)
            
            self.save_tasks()
            status = "completed" if new_state == Qt.Checked else "uncompleted"
            self.status_label.setText(f"Task marked as {status}!")
        else:
            self.status_label.setText("Please select a task!")
            
    def delete_task(self):
        current_item = self.task_list.currentItem()
        if current_item:
            reply = QMessageBox.question(
                self, "Delete Task",
                "Are you sure you want to delete this task?",
                QMessageBox.Yes | QMessageBox.No
            )
            if reply == QMessageBox.Yes:
                self.task_list.takeItem(self.task_list.row(current_item))
                self.save_tasks()
                self.status_label.setText("Task deleted!")
        else:
            self.status_label.setText("Please select a task!")
            
    def clear_all(self):
        if self.task_list.count() > 0:
            reply = QMessageBox.question(
                self, "Clear All",
                "Are you sure you want to delete all tasks?",
                QMessageBox.Yes | QMessageBox.No
            )
            if reply == QMessageBox.Yes:
                self.task_list.clear()
                self.save_tasks()
                self.status_label.setText("All tasks cleared!")
        else:
            self.status_label.setText("No tasks to clear!")
            
    def save_tasks(self):
        tasks = []
        for i in range(self.task_list.count()):
            item = self.task_list.item(i)
            tasks.append({
                'text': item.text(),
                'completed': item.checkState() == Qt.Checked
            })
            
        try:
            with open('tasks.json', 'w') as f:
                json.dump(tasks, f)
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Could not save tasks: {str(e)}")
            
    def load_tasks(self):
        try:
            with open('tasks.json', 'r') as f:
                tasks = json.load(f)
                
            for task in tasks:
                item = QListWidgetItem(task['text'])
                item.setFlags(item.flags() | Qt.ItemIsUserCheckable)
                item.setCheckState(Qt.Checked if task['completed'] else Qt.Unchecked)
                
                # Set strikethrough for completed tasks
                if task['completed']:
                    font = item.font()
                    font.setStrikeOut(True)
                    item.setFont(font)
                    
                self.task_list.addItem(item)
                
        except FileNotFoundError:
            pass  # Ignore if no saved tasks
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Could not load tasks: {str(e)}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # Apply fusion style for a modern look
    app.setStyle("Fusion")
    
    window = TodoListApp()
    window.show()
    
    sys.exit(app.exec())