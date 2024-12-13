# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'program3_3.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QPushButton, QSizePolicy,
    QTextBrowser, QWidget)

class Ui_KMITL_Phone(object):
    def setupUi(self, KMITL_Phone):
        if not KMITL_Phone.objectName():
            KMITL_Phone.setObjectName(u"KMITL_Phone")
        KMITL_Phone.resize(648, 628)
        self.num = QTextBrowser(KMITL_Phone)
        self.num.setObjectName(u"num")
        self.num.setGeometry(QRect(10, 10, 631, 41))
        self.widget = QWidget(KMITL_Phone)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(-1, 60, 641, 561))
        self.one = QPushButton(self.widget)
        self.one.setObjectName(u"one")
        self.one.setGeometry(QRect(10, 0, 211, 111))
        font = QFont()
        font.setPointSize(50)
        self.one.setFont(font)
        self.two = QPushButton(self.widget)
        self.two.setObjectName(u"two")
        self.two.setGeometry(QRect(220, 0, 211, 111))
        self.two.setFont(font)
        self.three = QPushButton(self.widget)
        self.three.setObjectName(u"three")
        self.three.setGeometry(QRect(430, 0, 211, 111))
        self.three.setFont(font)
        self.four = QPushButton(self.widget)
        self.four.setObjectName(u"four")
        self.four.setGeometry(QRect(10, 110, 211, 111))
        self.four.setFont(font)
        self.six = QPushButton(self.widget)
        self.six.setObjectName(u"six")
        self.six.setGeometry(QRect(430, 110, 211, 111))
        self.six.setFont(font)
        self.five = QPushButton(self.widget)
        self.five.setObjectName(u"five")
        self.five.setGeometry(QRect(220, 110, 211, 111))
        self.five.setFont(font)
        self.seven = QPushButton(self.widget)
        self.seven.setObjectName(u"seven")
        self.seven.setGeometry(QRect(10, 220, 211, 111))
        self.seven.setFont(font)
        self.nine = QPushButton(self.widget)
        self.nine.setObjectName(u"nine")
        self.nine.setGeometry(QRect(430, 220, 211, 111))
        self.nine.setFont(font)
        self.eight = QPushButton(self.widget)
        self.eight.setObjectName(u"eight")
        self.eight.setGeometry(QRect(220, 220, 211, 111))
        self.eight.setFont(font)
        self.star = QPushButton(self.widget)
        self.star.setObjectName(u"star")
        self.star.setGeometry(QRect(10, 330, 211, 111))
        self.star.setFont(font)
        self.hash = QPushButton(self.widget)
        self.hash.setObjectName(u"hash")
        self.hash.setGeometry(QRect(430, 330, 211, 111))
        self.hash.setFont(font)
        self.zero = QPushButton(self.widget)
        self.zero.setObjectName(u"zero")
        self.zero.setGeometry(QRect(220, 330, 211, 111))
        self.zero.setFont(font)
        self.talk = QPushButton(self.widget)
        self.talk.setObjectName(u"talk")
        self.talk.setGeometry(QRect(10, 440, 311, 111))
        self.talk.setFont(font)
        self.delete_2 = QPushButton(self.widget)
        self.delete_2.setObjectName(u"delete_2")
        self.delete_2.setGeometry(QRect(320, 440, 321, 111))
        self.delete_2.setFont(font)

        self.retranslateUi(KMITL_Phone)

        QMetaObject.connectSlotsByName(KMITL_Phone)
    # setupUi

    def retranslateUi(self, KMITL_Phone):
        KMITL_Phone.setWindowTitle(QCoreApplication.translate("KMITL_Phone", u"Dialog", None))
        self.one.setText(QCoreApplication.translate("KMITL_Phone", u"1", None))
        self.two.setText(QCoreApplication.translate("KMITL_Phone", u"2", None))
        self.three.setText(QCoreApplication.translate("KMITL_Phone", u"3", None))
        self.four.setText(QCoreApplication.translate("KMITL_Phone", u"4", None))
        self.six.setText(QCoreApplication.translate("KMITL_Phone", u"6", None))
        self.five.setText(QCoreApplication.translate("KMITL_Phone", u"5", None))
        self.seven.setText(QCoreApplication.translate("KMITL_Phone", u"7", None))
        self.nine.setText(QCoreApplication.translate("KMITL_Phone", u"9", None))
        self.eight.setText(QCoreApplication.translate("KMITL_Phone", u"8", None))
        self.star.setText(QCoreApplication.translate("KMITL_Phone", u"*", None))
        self.hash.setText(QCoreApplication.translate("KMITL_Phone", u"#", None))
        self.zero.setText(QCoreApplication.translate("KMITL_Phone", u"0", None))
        self.talk.setText(QCoreApplication.translate("KMITL_Phone", u"Talk", None))
        self.delete_2.setText(QCoreApplication.translate("KMITL_Phone", u"<", None))
    # retranslateUi

