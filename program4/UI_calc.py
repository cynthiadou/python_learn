# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_calc.ui',
# licensing of 'UI_calc.ui' applies.
#
# Created: Mon Nov 25 20:31:09 2019
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(518, 375)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 10, 501, 311))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.widget.setPalette(palette)
        self.widget.setObjectName("widget")
        self.layoutWidget = QtWidgets.QWidget(self.widget)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 0, 497, 311))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Result = QtWidgets.QLineEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding,
                                           QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Result.sizePolicy().hasHeightForWidth())
        self.Result.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setWeight(75)
        font.setBold(True)
        self.Result.setFont(font)
        self.Result.setText("")
        self.Result.setObjectName("Result")
        self.verticalLayout.addWidget(self.Result)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.sym_div = QtWidgets.QPushButton(self.layoutWidget)
        self.sym_div.setObjectName("sym_div")
        self.gridLayout.addWidget(self.sym_div, 5, 4, 1, 1)
        self.sym_add = QtWidgets.QPushButton(self.layoutWidget)
        self.sym_add.setObjectName("sym_add")
        self.gridLayout.addWidget(self.sym_add, 0, 5, 1, 1)
        self.num_5 = QtWidgets.QPushButton(self.layoutWidget)
        self.num_5.setObjectName("num_5")
        self.gridLayout.addWidget(self.num_5, 3, 3, 1, 1)
        self.num_6 = QtWidgets.QPushButton(self.layoutWidget)
        self.num_6.setObjectName("num_6")
        self.gridLayout.addWidget(self.num_6, 3, 4, 1, 1)
        self.fun_esc = QtWidgets.QPushButton(self.layoutWidget)
        self.fun_esc.setObjectName("fun_esc")
        self.gridLayout.addWidget(self.fun_esc, 0, 1, 1, 1)
        self.fun_clear = QtWidgets.QPushButton(self.layoutWidget)
        self.fun_clear.setObjectName("fun_clear")
        self.gridLayout.addWidget(self.fun_clear, 0, 3, 1, 1)
        self.num_4 = QtWidgets.QPushButton(self.layoutWidget)
        self.num_4.setObjectName("num_4")
        self.gridLayout.addWidget(self.num_4, 3, 1, 1, 1)
        self.num_9 = QtWidgets.QPushButton(self.layoutWidget)
        self.num_9.setObjectName("num_9")
        self.gridLayout.addWidget(self.num_9, 4, 4, 1, 1)
        self.fun_backspace = QtWidgets.QPushButton(self.layoutWidget)
        self.fun_backspace.setObjectName("fun_backspace")
        self.gridLayout.addWidget(self.fun_backspace, 0, 4, 1, 1)
        self.num_3 = QtWidgets.QPushButton(self.layoutWidget)
        self.num_3.setObjectName("num_3")
        self.gridLayout.addWidget(self.num_3, 5, 1, 1, 1)
        self.sym_sub = QtWidgets.QPushButton(self.layoutWidget)
        self.sym_sub.setObjectName("sym_sub")
        self.gridLayout.addWidget(self.sym_sub, 2, 5, 1, 1)
        self.num_2 = QtWidgets.QPushButton(self.layoutWidget)
        self.num_2.setObjectName("num_2")
        self.gridLayout.addWidget(self.num_2, 2, 3, 1, 1)
        self.num_8 = QtWidgets.QPushButton(self.layoutWidget)
        self.num_8.setObjectName("num_8")
        self.gridLayout.addWidget(self.num_8, 2, 4, 1, 1)
        self.sym_multi = QtWidgets.QPushButton(self.layoutWidget)
        self.sym_multi.setObjectName("sym_multi")
        self.gridLayout.addWidget(self.sym_multi, 5, 3, 1, 1)
        self.num_1 = QtWidgets.QPushButton(self.layoutWidget)
        self.num_1.setObjectName("num_1")
        self.gridLayout.addWidget(self.num_1, 2, 1, 1, 1)
        self.num_0 = QtWidgets.QPushButton(self.layoutWidget)
        self.num_0.setObjectName("num_0")
        self.gridLayout.addWidget(self.num_0, 4, 3, 1, 1)
        self.sym_dot = QtWidgets.QPushButton(self.layoutWidget)
        self.sym_dot.setObjectName("sym_dot")
        self.gridLayout.addWidget(self.sym_dot, 3, 5, 1, 1)
        self.num_7 = QtWidgets.QPushButton(self.layoutWidget)
        self.num_7.setObjectName("num_7")
        self.gridLayout.addWidget(self.num_7, 4, 1, 1, 1)
        self.sym_equal = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed,
                                           QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.sym_equal.sizePolicy().hasHeightForWidth())
        self.sym_equal.setSizePolicy(sizePolicy)
        self.sym_equal.setObjectName("sym_equal")
        self.gridLayout.addWidget(self.sym_equal, 4, 5, 2, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 518, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        # 信号和槽的绑定
        QtCore.QObject.connect(self.num_1, QtCore.SIGNAL("clicked()"),
                               MainWindow.ButtonAct)
        QtCore.QObject.connect(self.num_2, QtCore.SIGNAL("clicked()"),
                               MainWindow.ButtonAct)
        QtCore.QObject.connect(self.num_8, QtCore.SIGNAL("clicked()"),
                               MainWindow.ButtonAct)
        QtCore.QObject.connect(self.sym_dot, QtCore.SIGNAL("clicked()"),
                               MainWindow.ButtonAct)
        QtCore.QObject.connect(self.sym_add, QtCore.SIGNAL("clicked()"),
                               MainWindow.ButtonAct)
        QtCore.QObject.connect(self.num_4, QtCore.SIGNAL("clicked()"),
                               MainWindow.ButtonAct)
        QtCore.QObject.connect(self.num_4, QtCore.SIGNAL("clicked()"),
                               MainWindow.ButtonAct)
        QtCore.QObject.connect(self.num_7, QtCore.SIGNAL("clicked()"),
                               MainWindow.ButtonAct)
        QtCore.QObject.connect(self.num_3, QtCore.SIGNAL("clicked()"),
                               MainWindow.ButtonAct)
        QtCore.QObject.connect(self.sym_multi, QtCore.SIGNAL("clicked()"),
                               MainWindow.ButtonAct)
        QtCore.QObject.connect(self.num_5, QtCore.SIGNAL("clicked()"),
                               MainWindow.ButtonAct)
        QtCore.QObject.connect(self.num_0, QtCore.SIGNAL("clicked()"),
                               MainWindow.ButtonAct)
        QtCore.QObject.connect(self.num_9, QtCore.SIGNAL("clicked()"),
                               MainWindow.ButtonAct)
        QtCore.QObject.connect(self.num_6, QtCore.SIGNAL("clicked()"),
                               MainWindow.ButtonAct)
        QtCore.QObject.connect(self.sym_equal, QtCore.SIGNAL("clicked()"),
                               MainWindow.ButtonAct)
        QtCore.QObject.connect(self.sym_sub, QtCore.SIGNAL("clicked()"),
                               MainWindow.ButtonAct)
        QtCore.QObject.connect(self.sym_div, QtCore.SIGNAL("clicked()"),
                               MainWindow.ButtonAct)

        QtCore.QObject.connect(self.fun_esc, QtCore.SIGNAL("clicked()"),
                               MainWindow.ButtonAct)
        QtCore.QObject.connect(self.fun_backspace, QtCore.SIGNAL("clicked()"),
                               MainWindow.ButtonAct)
        QtCore.QObject.connect(self.fun_clear, QtCore.SIGNAL("clicked()"),
                               MainWindow.ButtonAct)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QtWidgets.QApplication.translate("MainWindow", "豆豆的计算器", None, -1))
        self.sym_div.setText(
            QtWidgets.QApplication.translate("MainWindow", "/", None, -1))
        self.sym_add.setText(
            QtWidgets.QApplication.translate("MainWindow", "+", None, -1))
        self.num_5.setText(
            QtWidgets.QApplication.translate("MainWindow", "5", None, -1))
        self.num_6.setText(
            QtWidgets.QApplication.translate("MainWindow", "6", None, -1))
        self.fun_esc.setText(
            QtWidgets.QApplication.translate("MainWindow", "ESC", None, -1))
        self.fun_clear.setText(
            QtWidgets.QApplication.translate("MainWindow", "Clear", None, -1))
        self.num_4.setText(
            QtWidgets.QApplication.translate("MainWindow", "4", None, -1))
        self.num_9.setText(
            QtWidgets.QApplication.translate("MainWindow", "9", None, -1))
        self.fun_backspace.setText(
            QtWidgets.QApplication.translate("MainWindow", "Backspace", None,
                                             -1))
        self.num_3.setText(
            QtWidgets.QApplication.translate("MainWindow", "0", None, -1))
        self.sym_sub.setText(
            QtWidgets.QApplication.translate("MainWindow", "-", None, -1))
        self.num_2.setText(
            QtWidgets.QApplication.translate("MainWindow", "2", None, -1))
        self.num_8.setText(
            QtWidgets.QApplication.translate("MainWindow", "3", None, -1))
        self.sym_multi.setText(
            QtWidgets.QApplication.translate("MainWindow", "*", None, -1))
        self.num_1.setText(
            QtWidgets.QApplication.translate("MainWindow", "1", None, -1))
        self.num_0.setText(
            QtWidgets.QApplication.translate("MainWindow", "8", None, -1))
        self.sym_dot.setText(
            QtWidgets.QApplication.translate("MainWindow", ".", None, -1))
        self.num_7.setText(
            QtWidgets.QApplication.translate("MainWindow", "7", None, -1))
        self.sym_equal.setText(
            QtWidgets.QApplication.translate("MainWindow", "=", None, -1))
