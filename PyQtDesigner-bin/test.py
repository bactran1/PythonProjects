# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PyQtDesigner-bin\test.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1066, 872)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/icon/AI icons/png/009-ai.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setToolTipDuration(-8)
        self.centralwidget.setStyleSheet("*{\n"
"background-color: #003153;\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(3, 3, 3, 3)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Header_frame = QtWidgets.QFrame(self.centralwidget)
        self.Header_frame.setEnabled(True)
        self.Header_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Header_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Header_frame.setObjectName("Header_frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.Header_frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.header_left = QtWidgets.QFrame(self.Header_frame)
        self.header_left.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.header_left.setFrameShadow(QtWidgets.QFrame.Raised)
        self.header_left.setObjectName("header_left")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.header_left)
        self.horizontalLayout_4.setContentsMargins(3, 3, 3, 3)
        self.horizontalLayout_4.setSpacing(2)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pushButton_2 = QtWidgets.QPushButton(self.header_left)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(14)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton\n"
"{\n"
"    border:none;\n"
"    color:#ffffff; \n"
"}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icon/icon/linea_arrows_1.0/_SVG/arrows_hamburger 2.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_4.addWidget(self.pushButton_2, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.horizontalLayout.addWidget(self.header_left, 0, QtCore.Qt.AlignTop)
        self.header_middle = QtWidgets.QFrame(self.Header_frame)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 49, 83))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 49, 83))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 49, 83))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 49, 83))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 49, 83))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 49, 83))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 49, 83))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 49, 83))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 49, 83))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.header_middle.setPalette(palette)
        self.header_middle.setStyleSheet("*{\n"
"color:#ffffff;\n"
"}\n"
"")
        self.header_middle.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.header_middle.setFrameShadow(QtWidgets.QFrame.Raised)
        self.header_middle.setObjectName("header_middle")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.header_middle)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.App_Icon = QtWidgets.QLabel(self.header_middle)
        self.App_Icon.setMaximumSize(QtCore.QSize(32, 20))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(14)
        self.App_Icon.setFont(font)
        self.App_Icon.setText("")
        self.App_Icon.setPixmap(QtGui.QPixmap(":/icon/icon/AI icons/png/005-deep-learning-1.png"))
        self.App_Icon.setScaledContents(True)
        self.App_Icon.setObjectName("App_Icon")
        self.horizontalLayout_3.addWidget(self.App_Icon, 0, QtCore.Qt.AlignTop)
        self.App_Name = QtWidgets.QLabel(self.header_middle)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(14)
        self.App_Name.setFont(font)
        self.App_Name.setStyleSheet("*{\n"
"color:#ffffff;\n"
"}\n"
"")
        self.App_Name.setScaledContents(False)
        self.App_Name.setObjectName("App_Name")
        self.horizontalLayout_3.addWidget(self.App_Name, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.horizontalLayout.addWidget(self.header_middle)
        self.header_right = QtWidgets.QFrame(self.Header_frame)
        self.header_right.setStyleSheet("*{\n"
"    border:none;\n"
"    color:#ffffff;\n"
"}")
        self.header_right.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.header_right.setFrameShadow(QtWidgets.QFrame.Raised)
        self.header_right.setObjectName("header_right")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.header_right)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.MinimizeBtn = QtWidgets.QPushButton(self.header_right)
        self.MinimizeBtn.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icon/icon/Icon Pack Vol. 1/SVG/MINUS.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.MinimizeBtn.setIcon(icon2)
        self.MinimizeBtn.setObjectName("MinimizeBtn")
        self.horizontalLayout_2.addWidget(self.MinimizeBtn)
        self.RestoreWindowBtn = QtWidgets.QPushButton(self.header_right)
        self.RestoreWindowBtn.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icon/icon/Icon Pack Vol. 1/SVG/MINIMIZE.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.RestoreWindowBtn.setIcon(icon3)
        self.RestoreWindowBtn.setIconSize(QtCore.QSize(32, 20))
        self.RestoreWindowBtn.setObjectName("RestoreWindowBtn")
        self.horizontalLayout_2.addWidget(self.RestoreWindowBtn)
        self.CloseBtn = QtWidgets.QPushButton(self.header_right)
        self.CloseBtn.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icon/icon/Icon Pack Vol. 1/SVG/CLOSE.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.CloseBtn.setIcon(icon4)
        self.CloseBtn.setIconSize(QtCore.QSize(32, 20))
        self.CloseBtn.setObjectName("CloseBtn")
        self.horizontalLayout_2.addWidget(self.CloseBtn)
        self.horizontalLayout.addWidget(self.header_right, 0, QtCore.Qt.AlignRight|QtCore.Qt.AlignTop)
        self.verticalLayout.addWidget(self.Header_frame, 0, QtCore.Qt.AlignTop)
        self.Body_frame = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Body_frame.sizePolicy().hasHeightForWidth())
        self.Body_frame.setSizePolicy(sizePolicy)
        self.Body_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Body_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Body_frame.setObjectName("Body_frame")
        self.verticalLayout.addWidget(self.Body_frame)
        self.Footer_frame = QtWidgets.QFrame(self.centralwidget)
        self.Footer_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Footer_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Footer_frame.setObjectName("Footer_frame")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.Footer_frame)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.Footer_version = QtWidgets.QFrame(self.Footer_frame)
        self.Footer_version.setStyleSheet("*{\n"
"color:#ffffff;\n"
"}\n"
"")
        self.Footer_version.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Footer_version.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Footer_version.setObjectName("Footer_version")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.Footer_version)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.Version = QtWidgets.QLabel(self.Footer_version)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(10)
        self.Version.setFont(font)
        self.Version.setScaledContents(False)
        self.Version.setObjectName("Version")
        self.horizontalLayout_5.addWidget(self.Version, 0, QtCore.Qt.AlignBottom)
        self.horizontalLayout_7.addWidget(self.Footer_version)
        self.Footer_help = QtWidgets.QFrame(self.Footer_frame)
        self.Footer_help.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Footer_help.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Footer_help.setObjectName("Footer_help")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.Footer_help)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.Version_2 = QtWidgets.QLabel(self.Footer_help)
        self.Version_2.setMaximumSize(QtCore.QSize(32, 32))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(10)
        self.Version_2.setFont(font)
        self.Version_2.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.Version_2.setText("")
        self.Version_2.setPixmap(QtGui.QPixmap(":/icon/icon/linea_arrows_1.0/_SVG/arrows_question.svg"))
        self.Version_2.setScaledContents(True)
        self.Version_2.setObjectName("Version_2")
        self.horizontalLayout_6.addWidget(self.Version_2, 0, QtCore.Qt.AlignRight|QtCore.Qt.AlignBottom)
        self.horizontalLayout_7.addWidget(self.Footer_help)
        self.verticalLayout.addWidget(self.Footer_frame)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_2.setText(_translate("MainWindow", "Menu"))
        self.App_Name.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Highliner Machine Learning Test</span></p></body></html>"))
        self.Version.setText(_translate("MainWindow", "Version 0.0.1 | Copyright Elmore Electric LLC."))
import icon_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
