# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gui.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QStatusBar, QTextBrowser,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(633, 565)
        font = QFont()
        font.setFamilies([u"Microsoft YaHei Light"])
        font.setPointSize(11)
        MainWindow.setFont(font)
        MainWindow.setCursor(QCursor(Qt.ArrowCursor))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.start_button = QPushButton(self.centralwidget)
        self.start_button.setObjectName(u"start_button")
        self.start_button.setGeometry(QRect(230, 410, 181, 61))
        font1 = QFont()
        font1.setFamilies([u"Microsoft YaHei Light"])
        font1.setPointSize(16)
        self.start_button.setFont(font1)
        self.start_button.setStyleSheet(u"border-radius:30px;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 149, 255);")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(200, 50, 251, 41))
        font2 = QFont()
        font2.setFamilies([u"Microsoft YaHei Light"])
        font2.setPointSize(14)
        self.label.setFont(font2)
        self.label.setAlignment(Qt.AlignCenter)
        self.textBrowser = QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(120, 120, 401, 131))
        font3 = QFont()
        font3.setFamilies([u"Microsoft YaHei Light"])
        font3.setPointSize(10)
        self.textBrowser.setFont(font3)
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(120, 320, 291, 31))
        self.lineEdit.setFont(font2)
        self.lineEdit.setReadOnly(True)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(120, 290, 251, 21))
        self.label_2.setFont(font3)
        self.browse_button = QPushButton(self.centralwidget)
        self.browse_button.setObjectName(u"browse_button")
        self.browse_button.setGeometry(QRect(420, 320, 101, 31))
        font4 = QFont()
        font4.setFamilies([u"Microsoft YaHei Light"])
        font4.setPointSize(9)
        font4.setBold(False)
        self.browse_button.setFont(font4)
        self.browse_button.setStyleSheet(u"border-radius:15px;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 149, 255);")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.start_button.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Google Contacts Program", None))
        self.textBrowser.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Microsoft YaHei Light','Microsoft YaHei Light'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Microsoft YaHei Light';\">Give this program a path to excel file(xlsx) that contains 3 columns:</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Microsoft YaHei Light'; font-weight:600;\">Full name</span><span style=\" font-family:'Microsoft YaHei Light';\">, </span><span style=\" font-family:'Microsoft YaHei Light'; font-weight:600;\">Phone number</"
                        "span><span style=\" font-family:'Microsoft YaHei Light';\"> and a </span><span style=\" font-family:'Microsoft YaHei Light'; font-weight:600;\">Current course</span><span style=\" font-family:'Microsoft YaHei Light';\">. </span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Microsoft YaHei Light';\">The excel file must be aligned from left to right.</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Microsoft YaHei Light';\">The program will add the contacts to Hamed's contacts list no matter if any of the users exists or not.</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Microsoft YaHei Light';\">Please note that this"
                        " program cooperates with Google Contacts under the user</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Microsoft YaHei Light';\">hilapniyot@gmail.com</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Microsoft YaHei Light';\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Microsoft YaHei Light';\">Do not Touch any file in the directory you are not familier with!</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Microsoft YaHei Light';\">For any problem, please contact the au"
                        "thor: Naor Or-Zion</span></p></body></html>", None))
        self.lineEdit.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Please Choose a contacts file path (xlsx)", None))
        self.browse_button.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
    # retranslateUi

