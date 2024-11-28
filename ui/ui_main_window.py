# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QGraphicsView, QHBoxLayout, QHeaderView,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QTextEdit, QTreeWidget,
    QTreeWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1078, 783)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.mainLayout = QHBoxLayout(self.centralwidget)
        self.mainLayout.setObjectName(u"mainLayout")
        self.treeAlgorithms = QTreeWidget(self.centralwidget)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, u"1");
        self.treeAlgorithms.setHeaderItem(__qtreewidgetitem)
        self.treeAlgorithms.setObjectName(u"treeAlgorithms")
        self.treeAlgorithms.setMinimumSize(QSize(200, 0))
        self.treeAlgorithms.setMaximumSize(QSize(200, 16777215))
        self.treeAlgorithms.setHeaderHidden(True)

        self.mainLayout.addWidget(self.treeAlgorithms)

        self.centerLayout = QVBoxLayout()
        self.centerLayout.setObjectName(u"centerLayout")
        self.graphicsView = QGraphicsView(self.centralwidget)
        self.graphicsView.setObjectName(u"graphicsView")
        self.graphicsView.setMinimumSize(QSize(600, 400))

        self.centerLayout.addWidget(self.graphicsView)

        self.controlLayout = QHBoxLayout()
        self.controlLayout.setObjectName(u"controlLayout")
        self.btnStart = QPushButton(self.centralwidget)
        self.btnStart.setObjectName(u"btnStart")
        icon = QIcon()
        icon.addFile(u"ui/icons/play_button.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnStart.setIcon(icon)

        self.controlLayout.addWidget(self.btnStart)

        self.btnStop = QPushButton(self.centralwidget)
        self.btnStop.setObjectName(u"btnStop")
        icon1 = QIcon()
        icon1.addFile(u"ui/icons/stop_button.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnStop.setIcon(icon1)

        self.controlLayout.addWidget(self.btnStop)

        self.btnStepForward = QPushButton(self.centralwidget)
        self.btnStepForward.setObjectName(u"btnStepForward")
        icon2 = QIcon()
        icon2.addFile(u"ui/icons/arrow_right_button.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnStepForward.setIcon(icon2)

        self.controlLayout.addWidget(self.btnStepForward)

        self.btnStepBackward = QPushButton(self.centralwidget)
        self.btnStepBackward.setObjectName(u"btnStepBackward")
        icon3 = QIcon()
        icon3.addFile(u"ui/icons/arrow_left_button.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnStepBackward.setIcon(icon3)

        self.controlLayout.addWidget(self.btnStepBackward)


        self.centerLayout.addLayout(self.controlLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.textDescription = QTextEdit(self.centralwidget)
        self.textDescription.setObjectName(u"textDescription")
        self.textDescription.setReadOnly(True)

        self.horizontalLayout.addWidget(self.textDescription)


        self.centerLayout.addLayout(self.horizontalLayout)


        self.mainLayout.addLayout(self.centerLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1078, 22))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Algorithm Visualizer", None))
        self.btnStart.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.btnStop.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.btnStepForward.setText(QCoreApplication.translate("MainWindow", u"Step Forward", None))
        self.btnStepBackward.setText(QCoreApplication.translate("MainWindow", u"Step Backward", None))
        self.textDescription.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Algorithm Description or Logs...", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

