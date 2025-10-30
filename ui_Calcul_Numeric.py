# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Calcul_Numeric.ui'
##
## Created by: Qt User Interface Compiler version 6.7.1
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGraphicsView, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QPlainTextEdit, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QTextEdit, QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(939, 618)
        MainWindow.setStyleSheet(u"background-color: #132877;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.SecondTable = QWidget(self.centralwidget)
        self.SecondTable.setObjectName(u"SecondTable")
        self.SecondTable.setEnabled(True)
        self.SecondTable.setStyleSheet(u"QWidget{\n"
"    background-color: #132877;\n"
"    color: white;\n"
"    border-top-right-radius: 10px;\n"
"    border-bottom-right-radius: 10px;\n"
"}\n"
"\n"
"QPushButton {\n"
"    color:white;\n"
"    text-align:left;\n"
"    height:30px;\n"
"    border:none;\n"
"    padding-left:10px;\n"
"    border-top-right-radius:10px;\n"
"    border-bottom-right-radius:10px;\n"
"}\n"
"QPushButton:checked{\n"
"    background-color: #89cff0;\n"
"    color: #1F95EF;\n"
"    font-weight:bold;\n"
"}\n"
"")
        self.verticalLayout_4 = QVBoxLayout(self.SecondTable)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, -1, 10, -1)
        self.label_2 = QLabel(self.SecondTable)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(40, 40))
        self.label_2.setMaximumSize(QSize(40, 40))
        self.label_2.setPixmap(QPixmap(u":/icons/ovidius_icon.png"))
        self.label_2.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.label_2)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(15)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 15, -1, -1)
        self.Home_Button2 = QPushButton(self.SecondTable)
        self.Home_Button2.setObjectName(u"Home_Button2")
        self.Home_Button2.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u":/icons/home icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Home_Button2.setIcon(icon)
        self.Home_Button2.setIconSize(QSize(25, 25))
        self.Home_Button2.setCheckable(True)
        self.Home_Button2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.Home_Button2)

        self.Bezier_Button2 = QPushButton(self.SecondTable)
        self.Bezier_Button2.setObjectName(u"Bezier_Button2")
        self.Bezier_Button2.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icona linie calculator.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Bezier_Button2.setIcon(icon1)
        self.Bezier_Button2.setIconSize(QSize(25, 25))
        self.Bezier_Button2.setCheckable(True)
        self.Bezier_Button2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.Bezier_Button2)

        self.Bspline_Button2 = QPushButton(self.SecondTable)
        self.Bspline_Button2.setObjectName(u"Bspline_Button2")
        self.Bspline_Button2.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.Bspline_Button2.setIcon(icon1)
        self.Bspline_Button2.setIconSize(QSize(25, 25))
        self.Bspline_Button2.setCheckable(True)
        self.Bspline_Button2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.Bspline_Button2)


        self.verticalLayout_4.addLayout(self.verticalLayout_2)

        self.verticalSpacer_2 = QSpacerItem(20, 334, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.SignOut_Button2 = QPushButton(self.SecondTable)
        self.SignOut_Button2.setObjectName(u"SignOut_Button2")
        self.SignOut_Button2.setStyleSheet(u"QWidget{\n"
"	background-color: #132877;\n"
"	color:white;\n"
"	border-radius:10px\n"
"}\n"
"")
        icon2 = QIcon()
        icon2.addFile(u":/icons/sign out iconita windows11 white 100%.png", QSize(), QIcon.Normal, QIcon.Off)
        self.SignOut_Button2.setIcon(icon2)
        self.SignOut_Button2.setIconSize(QSize(25, 25))
        self.SignOut_Button2.setCheckable(True)

        self.verticalLayout_4.addWidget(self.SignOut_Button2)


        self.gridLayout.addWidget(self.SecondTable, 0, 1, 1, 1)

        self.FirstTable = QWidget(self.centralwidget)
        self.FirstTable.setObjectName(u"FirstTable")
        self.FirstTable.setStyleSheet(u"QWidget{\n"
"	background-color: #132877;\n"
"	border-top-right-radius:10px;\n"
"	border-bottom-right-radius:10px;\n"
"	height: 100%;\n"
"}\n"
"QPushButton {\n"
"	color:white;\n"
"	text-align:left;\n"
"	height:30px;\n"
"	border:none;\n"
"	padding-left:10px;\n"
"	border-radius:10px;\n"
"}\n"
"QPushButton:checked{\n"
"	background-color: #89cff0;\n"
"	color: #1F95EF;\n"
"	font-weight:bold;\n"
"}\n"
"")
        self.verticalLayout_3 = QVBoxLayout(self.FirstTable)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.FirstTable)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(40, 40))
        self.label.setMaximumSize(QSize(40, 40))
        self.label.setPixmap(QPixmap(u"icons/ovidius_icon.png"))
        self.label.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.label)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 15, -1, -1)
        self.Home_Button1 = QPushButton(self.FirstTable)
        self.Home_Button1.setObjectName(u"Home_Button1")
        self.Home_Button1.setIcon(icon)
        self.Home_Button1.setIconSize(QSize(25, 25))
        self.Home_Button1.setCheckable(True)
        self.Home_Button1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.Home_Button1)

        self.Bezier_Button1 = QPushButton(self.FirstTable)
        self.Bezier_Button1.setObjectName(u"Bezier_Button1")
        self.Bezier_Button1.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.Bezier_Button1.setIcon(icon1)
        self.Bezier_Button1.setIconSize(QSize(25, 25))
        self.Bezier_Button1.setCheckable(True)
        self.Bezier_Button1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.Bezier_Button1)

        self.Bspline_Button1 = QPushButton(self.FirstTable)
        self.Bspline_Button1.setObjectName(u"Bspline_Button1")
        self.Bspline_Button1.setLayoutDirection(Qt.LeftToRight)
        self.Bspline_Button1.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.Bspline_Button1.setIcon(icon1)
        self.Bspline_Button1.setIconSize(QSize(25, 25))
        self.Bspline_Button1.setCheckable(True)
        self.Bspline_Button1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.Bspline_Button1)


        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.verticalSpacer = QSpacerItem(20, 334, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.SignOut_Button1 = QPushButton(self.FirstTable)
        self.SignOut_Button1.setObjectName(u"SignOut_Button1")
        self.SignOut_Button1.setStyleSheet(u"QWidget{\n"
"	background-color: #132877;\n"
"	color:white;\n"
"	border-radius:10px\n"
"}\n"
"")
        self.SignOut_Button1.setIcon(icon2)
        self.SignOut_Button1.setIconSize(QSize(25, 25))
        self.SignOut_Button1.setCheckable(True)

        self.verticalLayout_3.addWidget(self.SignOut_Button1)


        self.gridLayout.addWidget(self.FirstTable, 0, 0, 1, 1)

        self.main_menu = QWidget(self.centralwidget)
        self.main_menu.setObjectName(u"main_menu")
        self.main_menu.setStyleSheet(u"background-color: #132877;")
        self.verticalLayout_5 = QVBoxLayout(self.main_menu)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.stackedWidget = QStackedWidget(self.main_menu)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"")
        self.Home_Page = QWidget()
        self.Home_Page.setObjectName(u"Home_Page")
        self.Menu_Button1 = QPushButton(self.Home_Page)
        self.Menu_Button1.setObjectName(u"Menu_Button1")
        self.Menu_Button1.setGeometry(QRect(0, 0, 40, 30))
        self.Menu_Button1.setMaximumSize(QSize(16777215, 16777208))
        self.Menu_Button1.setStyleSheet(u"QWidget{\n"
"	background-color: #132877;\n"
"	color:white;\n"
"	border-radius:10px;\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/icons/menu white 100% icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Menu_Button1.setIcon(icon3)
        self.Menu_Button1.setIconSize(QSize(25, 25))
        self.Menu_Button1.setCheckable(True)
        self.Menu_Button1.setAutoExclusive(False)
        self.Cei3BarbatiPuternici = QPlainTextEdit(self.Home_Page)
        self.Cei3BarbatiPuternici.setObjectName(u"Cei3BarbatiPuternici")
        self.Cei3BarbatiPuternici.setGeometry(QRect(10, 530, 350, 60))
        self.Cei3BarbatiPuternici.setStyleSheet(u"border-radius:10px;\n"
"border: 2px solid black;\n"
"background-color: #89cff0;\n"
"")
        self.Cei3BarbatiPuternici.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.Cei3BarbatiPuternici.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.Cei3BarbatiPuternici.setReadOnly(True)
        self.textEdit = QTextEdit(self.Home_Page)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(150, 110, 421, 51))
        self.textEdit.setStyleSheet(u"border-radius:10px;\n"
"border: 2px solid black;\n"
"background-color: #89cff0;\n"
"")
        self.textEdit.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.stackedWidget.addWidget(self.Home_Page)
        self.Bezier_Page = QWidget()
        self.Bezier_Page.setObjectName(u"Bezier_Page")
        self.Menu_Button2 = QPushButton(self.Bezier_Page)
        self.Menu_Button2.setObjectName(u"Menu_Button2")
        self.Menu_Button2.setGeometry(QRect(0, 0, 40, 30))
        self.Menu_Button2.setStyleSheet(u"QWidget{\n"
"	background-color: #132877;\n"
"	color:white;\n"
"	border-radius:10px;\n"
"}")
        self.Menu_Button2.setIcon(icon3)
        self.Menu_Button2.setIconSize(QSize(25, 25))
        self.Menu_Button2.setCheckable(True)
        self.Menu_Button2.setAutoExclusive(False)
        self.GraphicView2 = QGraphicsView(self.Bezier_Page)
        self.GraphicView2.setObjectName(u"GraphicView2")
        self.GraphicView2.setGeometry(QRect(10, 190, 600, 400))
        self.GraphicView2.setStyleSheet(u"border-radius:10px;\n"
"border: 2px solid black;\n"
"background-color: #89cff0;\n"
"")
        self.Draw_Button2 = QPushButton(self.Bezier_Page)
        self.Draw_Button2.setObjectName(u"Draw_Button2")
        self.Draw_Button2.setGeometry(QRect(260, 130, 100, 25))
        self.Draw_Button2.setStyleSheet(u"QWidget{\n"
"    background-color: #132877;\n"
"    color: white; \n"
"	border-radius:10px;\n"
"	border: 2px solid black;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #89cff0; \n"
"    color: #1F95EF; \n"
"}\n"
"")
        icon4 = QIcon()
        icon4.addFile(u":/icons/Draw icon black.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Draw_Button2.setIcon(icon4)
        self.Draw_Button2.setIconSize(QSize(20, 20))
        self.Draw_Button2.setCheckable(True)
        self.Draw_Button2.setAutoExclusive(True)
        self.Reset_Button2 = QPushButton(self.Bezier_Page)
        self.Reset_Button2.setObjectName(u"Reset_Button2")
        self.Reset_Button2.setGeometry(QRect(260, 160, 100, 25))
        self.Reset_Button2.setStyleSheet(u"QWidget{\n"
"    background-color: #132877;\n"
"    color: white; \n"
"	border-radius:10px;\n"
"	border: 2px solid black;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #89cff0; \n"
"    color: #1F95EF; \n"
"}\n"
"")
        icon5 = QIcon()
        icon5.addFile(u":/icons/Reset icon black.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Reset_Button2.setIcon(icon5)
        self.Reset_Button2.setIconSize(QSize(20, 20))
        self.Reset_Button2.setCheckable(True)
        self.Reset_Button2.setAutoExclusive(True)
        self.Reset_Button2.setAutoDefault(False)
        self.Import_Button2 = QPushButton(self.Bezier_Page)
        self.Import_Button2.setObjectName(u"Import_Button2")
        self.Import_Button2.setGeometry(QRect(260, 100, 100, 25))
        self.Import_Button2.setStyleSheet(u"QWidget{\n"
"    background-color: #132877;\n"
"    color: white; \n"
"	border-radius:10px;\n"
"	border: 2px solid black;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #89cff0; \n"
"    color: #1F95EF; \n"
"}\n"
"")
        icon6 = QIcon()
        icon6.addFile(u":/icons/import icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Import_Button2.setIcon(icon6)
        self.Import_Button2.setIconSize(QSize(25, 25))
        self.Import_Button2.setCheckable(True)
        self.Import_Button2.setAutoExclusive(True)
        self.Import_Button2.setAutoDefault(False)
        self.Coordonate2 = QLabel(self.Bezier_Page)
        self.Coordonate2.setObjectName(u"Coordonate2")
        self.Coordonate2.setGeometry(QRect(620, 190, 100, 400))
        self.Coordonate2.setStyleSheet(u"border-radius:10px;\n"
"border: 2px solid black;\n"
"background-color: #89cff0;\n"
"")
        self.ComboBox = QComboBox(self.Bezier_Page)
        self.ComboBox.addItem("")
        self.ComboBox.addItem("")
        self.ComboBox.addItem("")
        self.ComboBox.setObjectName(u"ComboBox")
        self.ComboBox.setGeometry(QRect(260, 70, 100, 25))
        self.ComboBox.setStyleSheet(u"QWidget{\n"
"    background-color: #132877;\n"
"    color: white; \n"
"	border-radius:10px;\n"
"	border: 2px solid black;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #89cff0; \n"
"    color: #1F95EF; \n"
"}\n"
"")
        self.stackedWidget.addWidget(self.Bezier_Page)
        self.Bspline_Page = QWidget()
        self.Bspline_Page.setObjectName(u"Bspline_Page")
        self.Menu_Button3 = QPushButton(self.Bspline_Page)
        self.Menu_Button3.setObjectName(u"Menu_Button3")
        self.Menu_Button3.setGeometry(QRect(0, 0, 40, 30))
        self.Menu_Button3.setStyleSheet(u"QWidget{\n"
"	background-color: #132877;\n"
"	color:white;	\n"
"}")
        self.Menu_Button3.setIcon(icon3)
        self.Menu_Button3.setIconSize(QSize(25, 25))
        self.Menu_Button3.setCheckable(True)
        self.Menu_Button3.setAutoExclusive(False)
        self.GraphicView3 = QGraphicsView(self.Bspline_Page)
        self.GraphicView3.setObjectName(u"GraphicView3")
        self.GraphicView3.setGeometry(QRect(10, 190, 600, 400))
        self.GraphicView3.setStyleSheet(u"border-radius:10px;\n"
"border: 2px solid black;\n"
"background-color: #89cff0;\n"
"")
        self.Add_Button3 = QPushButton(self.Bspline_Page)
        self.Add_Button3.setObjectName(u"Add_Button3")
        self.Add_Button3.setGeometry(QRect(260, 100, 100, 25))
        self.Add_Button3.setStyleSheet(u"QWidget{\n"
"    background-color: #132877;\n"
"    color: white; \n"
"	border-radius:10px;\n"
"	border: 2px solid black;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #89cff0; \n"
"    color: #1F95EF; \n"
"}\n"
"")
        icon7 = QIcon()
        icon7.addFile(u":/icons/add icon black.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Add_Button3.setIcon(icon7)
        self.Add_Button3.setIconSize(QSize(20, 20))
        self.Add_Button3.setCheckable(True)
        self.Add_Button3.setAutoExclusive(True)
        self.Draw_Button3 = QPushButton(self.Bspline_Page)
        self.Draw_Button3.setObjectName(u"Draw_Button3")
        self.Draw_Button3.setGeometry(QRect(260, 130, 100, 25))
        self.Draw_Button3.setStyleSheet(u"QWidget{\n"
"    background-color: #132877;\n"
"    color: white; \n"
"	border-radius:10px;\n"
"	border: 2px solid black;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #89cff0; \n"
"    color: #1F95EF; \n"
"}\n"
"")
        self.Draw_Button3.setIcon(icon4)
        self.Draw_Button3.setIconSize(QSize(20, 20))
        self.Draw_Button3.setCheckable(True)
        self.Draw_Button3.setAutoExclusive(True)
        self.Reset_Button3 = QPushButton(self.Bspline_Page)
        self.Reset_Button3.setObjectName(u"Reset_Button3")
        self.Reset_Button3.setGeometry(QRect(260, 160, 100, 25))
        self.Reset_Button3.setStyleSheet(u"QWidget{\n"
"    background-color: #132877;\n"
"    color: white; \n"
"	border-radius:10px;\n"
"	border: 2px solid black;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #89cff0; \n"
"    color: #1F95EF; \n"
"}\n"
"")
        self.Reset_Button3.setIcon(icon5)
        self.Reset_Button3.setIconSize(QSize(20, 20))
        self.Reset_Button3.setCheckable(True)
        self.Reset_Button3.setAutoExclusive(True)
        self.Reset_Button3.setAutoDefault(False)
        self.Text_Button3 = QLineEdit(self.Bspline_Page)
        self.Text_Button3.setObjectName(u"Text_Button3")
        self.Text_Button3.setGeometry(QRect(240, 70, 141, 25))
        self.Text_Button3.setTabletTracking(False)
        self.Text_Button3.setStyleSheet(u"QWidget{\n"
"    background-color: #132877;\n"
"    color: white; \n"
"	border: 2px solid black;\n"
"	border-radius:10px;\n"
"}\n"
"")
        self.Coordonate3 = QLabel(self.Bspline_Page)
        self.Coordonate3.setObjectName(u"Coordonate3")
        self.Coordonate3.setGeometry(QRect(620, 190, 100, 400))
        self.Coordonate3.setStyleSheet(u"border-radius:10px;\n"
"border: 2px solid black;\n"
"background-color: #89cff0;\n"
"")
        self.stackedWidget.addWidget(self.Bspline_Page)

        self.verticalLayout_5.addWidget(self.stackedWidget)


        self.gridLayout.addWidget(self.main_menu, 0, 2, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.Bezier_Button1.toggled.connect(self.Bezier_Button2.setChecked)
        self.Bezier_Button2.toggled.connect(self.Bezier_Button1.setChecked)
        self.Bspline_Button1.toggled.connect(self.Bspline_Button2.setChecked)
        self.Bspline_Button2.toggled.connect(self.Bspline_Button1.setChecked)
        self.SignOut_Button1.toggled.connect(MainWindow.close)
        self.SignOut_Button2.toggled.connect(MainWindow.close)
        self.Menu_Button1.toggled.connect(self.FirstTable.setHidden)
        self.Menu_Button1.toggled.connect(self.SecondTable.setVisible)
        self.Menu_Button2.toggled.connect(self.FirstTable.setVisible)
        self.Menu_Button2.toggled.connect(self.SecondTable.setHidden)
        self.Menu_Button3.toggled.connect(self.FirstTable.setVisible)
        self.Menu_Button3.toggled.connect(self.SecondTable.setHidden)
        self.Home_Button1.toggled.connect(self.Home_Button2.setChecked)
        self.Home_Button2.toggled.connect(self.Home_Button1.setChecked)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_2.setText("")
        self.Home_Button2.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.Bezier_Button2.setText(QCoreApplication.translate("MainWindow", u"Bezier", None))
        self.Bspline_Button2.setText(QCoreApplication.translate("MainWindow", u"B-Spline", None))
        self.SignOut_Button2.setText(QCoreApplication.translate("MainWindow", u"Sign Out", None))
        self.label.setText("")
        self.Home_Button1.setText("")
        self.Bezier_Button1.setText("")
        self.Bspline_Button1.setText("")
        self.SignOut_Button1.setText("")
        self.Menu_Button1.setText("")
        self.Cei3BarbatiPuternici.setPlainText(QCoreApplication.translate("MainWindow", u"Dulce Matei-Ionut", None))
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Curbe B-spline si Bezier</span></p>\n"
, None))
        self.Menu_Button2.setText("")
        self.Draw_Button2.setText(QCoreApplication.translate("MainWindow", u"Draw", None))
        self.Reset_Button2.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.Import_Button2.setText(QCoreApplication.translate("MainWindow", u"Import", None))
        self.Coordonate2.setText("")
        self.ComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"General", None))
        self.ComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Cubic", None))
        self.ComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Cuadratic", None))

        self.Menu_Button3.setText("")
        self.Add_Button3.setText(QCoreApplication.translate("MainWindow", u"Add Point", None))
        self.Draw_Button3.setText(QCoreApplication.translate("MainWindow", u"Draw", None))
        self.Reset_Button3.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.Coordonate3.setText("")
    # retranslateUi

