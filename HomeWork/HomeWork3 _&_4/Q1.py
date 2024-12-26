# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Q1.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QLineEdit,
    QListWidget, QListWidgetItem, QPushButton, QSizePolicy,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(640, 615)
        self.Todolist = QLabel(Dialog)
        self.Todolist.setObjectName(u"Todolist")
        self.Todolist.setGeometry(QRect(260, 20, 111, 41))
        font = QFont()
        font.setPointSize(15)
        self.Todolist.setFont(font)
        self.Add_btn = QPushButton(Dialog)
        self.Add_btn.setObjectName(u"Add_btn")
        self.Add_btn.setGeometry(QRect(500, 70, 93, 29))
        self.Add_btn.setStyleSheet(u"background-color: rgb(32, 255, 58)")
        self.MarkComplete_btn = QPushButton(Dialog)
        self.MarkComplete_btn.setObjectName(u"MarkComplete_btn")
        self.MarkComplete_btn.setGeometry(QRect(40, 510, 171, 41))
        self.MarkComplete_btn.setStyleSheet(u"Background-color:rgb(34, 226, 255)")
        self.List_Output = QListWidget(Dialog)
        self.List_Output.setObjectName(u"List_Output")
        self.List_Output.setGeometry(QRect(40, 130, 551, 351))
        self.Clear_btn = QPushButton(Dialog)
        self.Clear_btn.setObjectName(u"Clear_btn")
        self.Clear_btn.setGeometry(QRect(420, 510, 171, 41))
        self.Delete_btn = QPushButton(Dialog)
        self.Delete_btn.setObjectName(u"Delete_btn")
        self.Delete_btn.setGeometry(QRect(230, 510, 171, 41))
        self.Delete_btn.setStyleSheet(u"background-color:rgb(255, 25, 29)")
        self.Input = QLineEdit(Dialog)
        self.Input.setObjectName(u"Input")
        self.Input.setGeometry(QRect(50, 70, 421, 31))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.Todolist.setText(QCoreApplication.translate("Dialog", u"To do list", None))
        self.Add_btn.setText(QCoreApplication.translate("Dialog", u"Add Task", None))
        self.MarkComplete_btn.setText(QCoreApplication.translate("Dialog", u"MarkComplete", None))
        self.Clear_btn.setText(QCoreApplication.translate("Dialog", u"Clear All", None))
        self.Delete_btn.setText(QCoreApplication.translate("Dialog", u"Delete Task", None))
    # retranslateUi

