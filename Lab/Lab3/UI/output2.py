# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'program3_2.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QPushButton,
    QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(861, 600)
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(170, 230, 221, 101))
        font = QFont()
        font.setPointSize(50)
        self.label.setFont(font)
        self.widget = QWidget(Dialog)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(490, -1, 371, 601))
        self.inc_btn = QPushButton(self.widget)
        self.inc_btn.setObjectName(u"inc_btn")
        self.inc_btn.setGeometry(QRect(60, 20, 261, 171))
        self.inc_btn.setFont(font)
        self.dec_btn = QPushButton(self.widget)
        self.dec_btn.setObjectName(u"dec_btn")
        self.dec_btn.setGeometry(QRect(60, 210, 261, 171))
        self.dec_btn.setFont(font)
        self.reset = QPushButton(self.widget)
        self.reset.setObjectName(u"reset")
        self.reset.setGeometry(QRect(60, 410, 261, 171))
        self.reset.setFont(font)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"0", None))
        self.inc_btn.setText(QCoreApplication.translate("Dialog", u"+", None))
        self.dec_btn.setText(QCoreApplication.translate("Dialog", u"-", None))
        self.reset.setText(QCoreApplication.translate("Dialog", u"Reset", None))
    # retranslateUi

