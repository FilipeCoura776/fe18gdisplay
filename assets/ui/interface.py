# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interface.ui'
##
## Created by: Qt User Interface Compiler version 6.11.2
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QLabel,
    QMainWindow, QSizePolicy, QWidget)
import portraits_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(551, 644)
        MainWindow.setStyleSheet(u"background-color: rgb(18, 36, 40);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 10, 531, 621))
        self.widget.setStyleSheet(u"background-color: rgb(12, 32, 33);\n"
"\n"
"border: 1px solid #3498db;\n"
"border-radius: 0px;\n"
"border-color: rgb(42, 60, 61);")
        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(10, 220, 511, 261))
        self.widget_2.setStyleSheet(u"background-color: rgb(3, 22, 26);")
        self.label_3 = QLabel(self.widget_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 0, 131, 31))
        font = QFont()
        font.setFamilies([u"Times New Roman"])
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"border:0px;\n"
"background-color: rgba(255, 255, 255, 0);\n"
"color:rgb(199, 194, 174);\n"
"")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.line = QFrame(self.widget_2)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(5, 20, 501, 24))
        self.line.setStyleSheet(u"background-color: rgb(138, 136, 121); /* Cor da linha (ex: dourado Fire Emblem) */\n"
"max-height: 4px;           /* Define a espessura da linha (ex: 2 pixels) */\n"
"border: none;              /* Remove qualquer borda padr\u00e3o */\n"
"margin: 10px 0px;")
        self.line.setFrameShadow(QFrame.Shadow.Raised)
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.label_4 = QLabel(self.widget_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 80, 51, 41))
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(u"border:0px;\n"
"background-color: rgba(255, 255, 255, 0);\n"
"color:rgb(199, 194, 174);\n"
"")
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.line_2 = QFrame(self.widget_2)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(20, 112, 101, 21))
        self.line_2.setStyleSheet(u"background-color: rgb(138, 136, 121);\n"
"max-height: 1px;       \n"
"border: none;          \n"
"margin: 10px 0px;")
        self.line_2.setFrameShadow(QFrame.Shadow.Raised)
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.lblStrGr = QLabel(self.widget_2)
        self.lblStrGr.setObjectName(u"lblStrGr")
        self.lblStrGr.setGeometry(QRect(82, 82, 41, 41))
        font1 = QFont()
        font1.setFamilies([u"SimSun-ExtG"])
        font1.setPointSize(20)
        font1.setBold(True)
        self.lblStrGr.setFont(font1)
        self.lblStrGr.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.lblStrGr.setStyleSheet(u"border:0px;\n"
"background-color: rgba(255, 255, 255, 0);\n"
"")
        self.lblStrGr.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.line_3 = QFrame(self.widget_2)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setGeometry(QRect(20, 152, 101, 21))
        self.line_3.setStyleSheet(u"background-color: rgb(138, 136, 121);\n"
"max-height: 1px;       \n"
"border: none;          \n"
"margin: 10px 0px;")
        self.line_3.setFrameShadow(QFrame.Shadow.Raised)
        self.line_3.setFrameShape(QFrame.Shape.HLine)
        self.lblMagGr = QLabel(self.widget_2)
        self.lblMagGr.setObjectName(u"lblMagGr")
        self.lblMagGr.setGeometry(QRect(82, 122, 41, 41))
        self.lblMagGr.setFont(font1)
        self.lblMagGr.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.lblMagGr.setStyleSheet(u"border:0px;\n"
"background-color: rgba(255, 255, 255, 0);\n"
"")
        self.lblMagGr.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.label_7 = QLabel(self.widget_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(20, 120, 51, 41))
        self.label_7.setFont(font)
        self.label_7.setStyleSheet(u"border:0px;\n"
"background-color: rgba(255, 255, 255, 0);\n"
"color:rgb(199, 194, 174);\n"
"")
        self.label_7.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.line_4 = QFrame(self.widget_2)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setGeometry(QRect(20, 192, 101, 21))
        self.line_4.setStyleSheet(u"background-color: rgb(138, 136, 121);\n"
"max-height: 1px;       \n"
"border: none;          \n"
"margin: 10px 0px;")
        self.line_4.setFrameShadow(QFrame.Shadow.Raised)
        self.line_4.setFrameShape(QFrame.Shape.HLine)
        self.lblSpdGr = QLabel(self.widget_2)
        self.lblSpdGr.setObjectName(u"lblSpdGr")
        self.lblSpdGr.setGeometry(QRect(82, 162, 41, 41))
        self.lblSpdGr.setFont(font1)
        self.lblSpdGr.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.lblSpdGr.setStyleSheet(u"border:0px;\n"
"background-color: rgba(255, 255, 255, 0);\n"
"")
        self.lblSpdGr.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.label_9 = QLabel(self.widget_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(20, 160, 51, 41))
        self.label_9.setFont(font)
        self.label_9.setStyleSheet(u"border:0px;\n"
"background-color: rgba(255, 255, 255, 0);\n"
"color:rgb(199, 194, 174);\n"
"")
        self.label_9.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.line_5 = QFrame(self.widget_2)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setGeometry(QRect(20, 230, 101, 21))
        self.line_5.setStyleSheet(u"background-color: rgb(138, 136, 121);\n"
"max-height: 1px;       \n"
"border: none;          \n"
"margin: 10px 0px;")
        self.line_5.setFrameShadow(QFrame.Shadow.Raised)
        self.line_5.setFrameShape(QFrame.Shape.HLine)
        self.label_10 = QLabel(self.widget_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(20, 200, 51, 41))
        self.label_10.setFont(font)
        self.label_10.setStyleSheet(u"border:0px;\n"
"background-color: rgba(255, 255, 255, 0);\n"
"color:rgb(199, 194, 174);\n"
"")
        self.label_10.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.lblDexGr = QLabel(self.widget_2)
        self.lblDexGr.setObjectName(u"lblDexGr")
        self.lblDexGr.setGeometry(QRect(82, 202, 41, 41))
        self.lblDexGr.setFont(font1)
        self.lblDexGr.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.lblDexGr.setStyleSheet(u"border:0px;\n"
"background-color: rgba(255, 255, 255, 0);\n"
"")
        self.lblDexGr.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.lblChaGr = QLabel(self.widget_2)
        self.lblChaGr.setObjectName(u"lblChaGr")
        self.lblChaGr.setGeometry(QRect(222, 202, 41, 41))
        self.lblChaGr.setFont(font1)
        self.lblChaGr.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.lblChaGr.setStyleSheet(u"border:0px;\n"
"background-color: rgba(255, 255, 255, 0);\n"
"")
        self.lblChaGr.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.line_6 = QFrame(self.widget_2)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setGeometry(QRect(160, 194, 101, 21))
        self.line_6.setStyleSheet(u"background-color: rgb(138, 136, 121);\n"
"max-height: 1px;       \n"
"border: none;          \n"
"margin: 10px 0px;")
        self.line_6.setFrameShadow(QFrame.Shadow.Raised)
        self.line_6.setFrameShape(QFrame.Shape.HLine)
        self.line_7 = QFrame(self.widget_2)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setGeometry(QRect(160, 152, 101, 21))
        self.line_7.setStyleSheet(u"background-color: rgb(138, 136, 121);\n"
"max-height: 1px;       \n"
"border: none;          \n"
"margin: 10px 0px;")
        self.line_7.setFrameShadow(QFrame.Shadow.Raised)
        self.line_7.setFrameShape(QFrame.Shape.HLine)
        self.label_13 = QLabel(self.widget_2)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(160, 120, 51, 41))
        self.label_13.setFont(font)
        self.label_13.setStyleSheet(u"border:0px;\n"
"background-color: rgba(255, 255, 255, 0);\n"
"color:rgb(199, 194, 174);\n"
"")
        self.label_13.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.label_14 = QLabel(self.widget_2)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(160, 160, 51, 41))
        self.label_14.setFont(font)
        self.label_14.setStyleSheet(u"border:0px;\n"
"background-color: rgba(255, 255, 255, 0);\n"
"color:rgb(199, 194, 174);\n"
"")
        self.label_14.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.lblLckGr = QLabel(self.widget_2)
        self.lblLckGr.setObjectName(u"lblLckGr")
        self.lblLckGr.setGeometry(QRect(222, 162, 41, 41))
        font2 = QFont()
        font2.setFamilies([u"SimSun-ExtG"])
        font2.setPointSize(20)
        font2.setBold(True)
        font2.setItalic(False)
        font2.setUnderline(False)
        font2.setStrikeOut(False)
        font2.setStyleStrategy(QFont.PreferDefault)
        self.lblLckGr.setFont(font2)
        self.lblLckGr.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.lblLckGr.setStyleSheet(u"border:0px;\n"
"background-color: rgba(255, 255, 255, 0);\n"
"")
        self.lblLckGr.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.line_8 = QFrame(self.widget_2)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setGeometry(QRect(160, 112, 101, 21))
        self.line_8.setStyleSheet(u"background-color: rgb(138, 136, 121);\n"
"max-height: 1px;       \n"
"border: none;          \n"
"margin: 10px 0px;")
        self.line_8.setFrameShadow(QFrame.Shadow.Raised)
        self.line_8.setFrameShape(QFrame.Shape.HLine)
        self.line_9 = QFrame(self.widget_2)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setGeometry(QRect(160, 230, 101, 21))
        self.line_9.setStyleSheet(u"background-color: rgb(138, 136, 121);\n"
"max-height: 1px;       \n"
"border: none;          \n"
"margin: 10px 0px;")
        self.line_9.setFrameShadow(QFrame.Shadow.Raised)
        self.line_9.setFrameShape(QFrame.Shape.HLine)
        self.lblResGr = QLabel(self.widget_2)
        self.lblResGr.setObjectName(u"lblResGr")
        self.lblResGr.setGeometry(QRect(222, 122, 41, 41))
        self.lblResGr.setFont(font1)
        self.lblResGr.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.lblResGr.setStyleSheet(u"border:0px;\n"
"background-color: rgba(255, 255, 255, 0);\n"
"")
        self.lblResGr.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.lblDefGr = QLabel(self.widget_2)
        self.lblDefGr.setObjectName(u"lblDefGr")
        self.lblDefGr.setGeometry(QRect(222, 84, 41, 41))
        self.lblDefGr.setFont(font1)
        self.lblDefGr.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.lblDefGr.setStyleSheet(u"border:0px;\n"
"background-color: rgba(255, 255, 255, 0);\n"
"")
        self.lblDefGr.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.label_18 = QLabel(self.widget_2)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(160, 200, 51, 41))
        self.label_18.setFont(font)
        self.label_18.setStyleSheet(u"border:0px;\n"
"background-color: rgba(255, 255, 255, 0);\n"
"color:rgb(199, 194, 174);\n"
"")
        self.label_18.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.label_19 = QLabel(self.widget_2)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(160, 82, 51, 41))
        self.label_19.setFont(font)
        self.label_19.setStyleSheet(u"border:0px;\n"
"background-color: rgba(255, 255, 255, 0);\n"
"color:rgb(199, 194, 174);\n"
"")
        self.label_19.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.line_10 = QFrame(self.widget_2)
        self.line_10.setObjectName(u"line_10")
        self.line_10.setGeometry(QRect(20, 72, 101, 21))
        self.line_10.setStyleSheet(u"background-color: rgb(138, 136, 121);\n"
"max-height: 1px;       \n"
"border: none;          \n"
"margin: 10px 0px;")
        self.line_10.setFrameShadow(QFrame.Shadow.Raised)
        self.line_10.setFrameShape(QFrame.Shape.HLine)
        self.lblHpGr = QLabel(self.widget_2)
        self.lblHpGr.setObjectName(u"lblHpGr")
        self.lblHpGr.setGeometry(QRect(82, 42, 41, 41))
        self.lblHpGr.setFont(font1)
        self.lblHpGr.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.lblHpGr.setStyleSheet(u"border:0px;\n"
"background-color: rgba(255, 255, 255, 0);\n"
"")
        self.lblHpGr.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.label_5 = QLabel(self.widget_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(20, 40, 51, 41))
        self.label_5.setFont(font)
        self.label_5.setStyleSheet(u"border:0px;\n"
"background-color: rgba(255, 255, 255, 0);\n"
"color:rgb(199, 194, 174);\n"
"")
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.label_6 = QLabel(self.widget_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(350, 0, 131, 31))
        self.label_6.setFont(font)
        self.label_6.setStyleSheet(u"border:0px;\n"
"background-color: rgba(255, 255, 255, 0);\n"
"color:rgb(199, 194, 174);\n"
"")
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lblTotalGr = QLabel(self.widget_2)
        self.lblTotalGr.setObjectName(u"lblTotalGr")
        self.lblTotalGr.setGeometry(QRect(450, 0, 51, 31))
        self.lblTotalGr.setFont(font1)
        self.lblTotalGr.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.lblTotalGr.setStyleSheet(u"border:0px;\n"
"background-color: rgba(255, 255, 255, 0);\n"
"")
        self.lblTotalGr.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.radar_teste = QWidget(self.widget_2)
        self.radar_teste.setObjectName(u"radar_teste")
        self.radar_teste.setGeometry(QRect(300, 50, 201, 201))
        font3 = QFont()
        font3.setPointSize(9)
        self.radar_teste.setFont(font3)
        self.radar_teste.setStyleSheet(u"border: 0px;\n"
"background-color: rgb(4, 26, 31);")
        self.widget_3 = QWidget(self.widget)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setGeometry(QRect(10, 10, 511, 201))
        self.widget_3.setStyleSheet(u"background-color: rgb(21, 40, 46);")
        self.wdgPortrait = QWidget(self.widget_3)
        self.wdgPortrait.setObjectName(u"wdgPortrait")
        self.wdgPortrait.setGeometry(QRect(310, -10, 211, 211))
        self.wdgPortrait.setStyleSheet(u"image: url(:/portraits/Cai.png);\n"
"border:0px;")
        self.widget_4 = QWidget(self.widget_3)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setGeometry(QRect(230, 0, 271, 201))
        self.widget_4.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0.142, y1:1, x2:0.594, y2:1, stop:0.331579 rgba(21, 40, 46, 255), stop:0.836842 rgba(255, 255, 255, 0));\n"
"border:0px;")
        self.widget_5 = QWidget(self.widget_3)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setGeometry(QRect(-1, 4, 281, 181))
        self.widget_5.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);\n"
"\n"
"border:0px;\n"
"\n"
"")
        self.lblName = QLabel(self.widget_5)
        self.lblName.setObjectName(u"lblName")
        self.lblName.setGeometry(QRect(10, 0, 261, 31))
        font4 = QFont()
        font4.setFamilies([u"Times New Roman"])
        font4.setPointSize(18)
        self.lblName.setFont(font4)
        self.lblName.setStyleSheet(u"border:0px;\n"
"background-color: rgba(255, 255, 255, 0);\n"
"")
        self.lblName.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lblTitle = QLabel(self.widget_5)
        self.lblTitle.setObjectName(u"lblTitle")
        self.lblTitle.setGeometry(QRect(10, 25, 261, 31))
        self.lblTitle.setFont(font)
        self.lblTitle.setStyleSheet(u"border:0px;\n"
"background-color: rgba(255, 255, 255, 0);\n"
"\n"
"color: rgb(193, 193, 193);\n"
"")
        self.lblTitle.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lblClass = QLabel(self.widget_5)
        self.lblClass.setObjectName(u"lblClass")
        self.lblClass.setGeometry(QRect(10, 65, 261, 31))
        self.lblClass.setFont(font4)
        self.lblClass.setStyleSheet(u"border:0px;\n"
"background-color: rgba(255, 255, 255, 0);\n"
"")
        self.lblClass.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lblTier = QLabel(self.widget_5)
        self.lblTier.setObjectName(u"lblTier")
        self.lblTier.setGeometry(QRect(10, 90, 261, 31))
        self.lblTier.setFont(font)
        self.lblTier.setStyleSheet(u"border:0px;\n"
"background-color: rgba(255, 255, 255, 0);\n"
"\n"
"color: rgb(110, 110, 110);\n"
"")
        self.lblTier.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.line_11 = QFrame(self.widget_5)
        self.line_11.setObjectName(u"line_11")
        self.line_11.setGeometry(QRect(10, 50, 261, 21))
        self.line_11.setStyleSheet(u"background-color: rgb(138, 136, 121);\n"
"max-height: 1px;       \n"
"border: none;          \n"
"margin: 10px 0px;")
        self.line_11.setFrameShadow(QFrame.Shadow.Raised)
        self.line_11.setFrameShape(QFrame.Shape.HLine)
        self.widget_7 = QWidget(self.widget_5)
        self.widget_7.setObjectName(u"widget_7")
        self.widget_7.setGeometry(QRect(20, 140, 181, 31))
        self.widget_7.setStyleSheet(u"background-color: rgb(21, 40, 46);")
        self.icon1 = QWidget(self.widget_7)
        self.icon1.setObjectName(u"icon1")
        self.icon1.setGeometry(QRect(0, 0, 20, 20))
        self.icon1.setStyleSheet(u"background-color: rgb(55, 252, 255);\n"
"\n"
"image: url(:/icons/Sword.png);")
        self.icon2 = QWidget(self.widget_7)
        self.icon2.setObjectName(u"icon2")
        self.icon2.setGeometry(QRect(22, 0, 20, 20))
        self.icon2.setStyleSheet(u"background-color: rgb(55, 252, 255);\n"
"image: url(:/icons/Spear.png);")
        self.icon3 = QWidget(self.widget_7)
        self.icon3.setObjectName(u"icon3")
        self.icon3.setGeometry(QRect(44, 0, 20, 20))
        self.icon3.setStyleSheet(u"background-color: rgb(55, 252, 255);")
        self.icon4 = QWidget(self.widget_7)
        self.icon4.setObjectName(u"icon4")
        self.icon4.setGeometry(QRect(66, 0, 20, 20))
        self.icon4.setStyleSheet(u"background-color: rgb(55, 252, 255);")
        self.icon5 = QWidget(self.widget_7)
        self.icon5.setObjectName(u"icon5")
        self.icon5.setGeometry(QRect(88, 0, 20, 20))
        self.icon5.setStyleSheet(u"background-color: rgb(55, 252, 255);")
        self.icon8 = QWidget(self.widget_7)
        self.icon8.setObjectName(u"icon8")
        self.icon8.setGeometry(QRect(154, 0, 20, 20))
        self.icon8.setStyleSheet(u"background-color: rgb(55, 252, 255);")
        self.icon6 = QWidget(self.widget_7)
        self.icon6.setObjectName(u"icon6")
        self.icon6.setGeometry(QRect(110, 0, 20, 20))
        self.icon6.setStyleSheet(u"background-color: rgb(55, 252, 255);")
        self.icon7 = QWidget(self.widget_7)
        self.icon7.setObjectName(u"icon7")
        self.icon7.setGeometry(QRect(132, 0, 20, 20))
        self.icon7.setStyleSheet(u"background-color: rgb(55, 252, 255);")
        self.line_12 = QFrame(self.widget_5)
        self.line_12.setObjectName(u"line_12")
        self.line_12.setGeometry(QRect(10, 160, 261, 21))
        self.line_12.setStyleSheet(u"background-color: rgb(138, 136, 121);\n"
"max-height: 1px;       \n"
"border: none;          \n"
"margin: 10px 0px;")
        self.line_12.setFrameShadow(QFrame.Shadow.Raised)
        self.line_12.setFrameShape(QFrame.Shape.HLine)
        self.lblName.raise_()
        self.lblTitle.raise_()
        self.lblTier.raise_()
        self.lblClass.raise_()
        self.line_11.raise_()
        self.widget_7.raise_()
        self.line_12.raise_()
        self.lblName_2 = QLabel(self.widget)
        self.lblName_2.setObjectName(u"lblName_2")
        self.lblName_2.setGeometry(QRect(10, 490, 261, 31))
        self.lblName_2.setFont(font4)
        self.lblName_2.setStyleSheet(u"border:0px;\n"
"background-color: rgba(255, 255, 255, 0);\n"
"")
        self.lblName_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.cbbChar = QComboBox(self.widget)
        self.cbbChar.setObjectName(u"cbbChar")
        self.cbbChar.setGeometry(QRect(50, 530, 181, 31))
        self.cbbChar.setFont(font)
        self.cbbChar.setStyleSheet(u"background-color: rgb(0, 0, 127);")
        self.cbbClass = QComboBox(self.widget)
        self.cbbClass.setObjectName(u"cbbClass")
        self.cbbClass.setGeometry(QRect(280, 530, 181, 31))
        self.cbbClass.setFont(font)
        self.cbbClass.setStyleSheet(u"background-color: rgb(0, 0, 127);")
        self.lblName_4 = QLabel(self.widget)
        self.lblName_4.setObjectName(u"lblName_4")
        self.lblName_4.setGeometry(QRect(240, 490, 261, 31))
        self.lblName_4.setFont(font4)
        self.lblName_4.setStyleSheet(u"border:0px;\n"
"background-color: rgba(255, 255, 255, 0);\n"
"")
        self.lblName_4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.widget_6 = QWidget(self.centralwidget)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setGeometry(QRect(20, 20, 511, 201))
        self.widget_6.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);\n"
"\n"
"border: 1px solid rgb(199, 194, 174);;")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Growth Rates", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Str", None))
        self.lblStrGr.setText(QCoreApplication.translate("MainWindow", u"20", None))
        self.lblMagGr.setText(QCoreApplication.translate("MainWindow", u"20", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Mag", None))
        self.lblSpdGr.setText(QCoreApplication.translate("MainWindow", u"20", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Spd", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Dex", None))
        self.lblDexGr.setText(QCoreApplication.translate("MainWindow", u"20", None))
        self.lblChaGr.setText(QCoreApplication.translate("MainWindow", u"20", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Res", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Lck", None))
        self.lblLckGr.setText(QCoreApplication.translate("MainWindow", u"20", None))
        self.lblResGr.setText(QCoreApplication.translate("MainWindow", u"20", None))
        self.lblDefGr.setText(QCoreApplication.translate("MainWindow", u"20", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Cha", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Def", None))
        self.lblHpGr.setText(QCoreApplication.translate("MainWindow", u"20", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"HP", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Total", None))
        self.lblTotalGr.setText(QCoreApplication.translate("MainWindow", u"220", None))
        self.lblName.setText(QCoreApplication.translate("MainWindow", u"Nome", None))
        self.lblTitle.setText(QCoreApplication.translate("MainWindow", u"T\u00edtulo", None))
        self.lblClass.setText(QCoreApplication.translate("MainWindow", u"Classe", None))
        self.lblTier.setText(QCoreApplication.translate("MainWindow", u"Tier", None))
        self.lblName_2.setText(QCoreApplication.translate("MainWindow", u"Select Character", None))
        self.lblName_4.setText(QCoreApplication.translate("MainWindow", u"Select Class", None))
    # retranslateUi

