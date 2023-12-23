# Form implementation generated from reading ui file '.\main_ui.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(711, 606)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(711, 606))
        MainWindow.setMaximumSize(QtCore.QSize(711, 606))
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.convert_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.convert_button.setGeometry(QtCore.QRect(10, 260, 181, 41))
        self.convert_button.setObjectName("convert_button")
        self.import_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.import_button.setGeometry(QtCore.QRect(10, 10, 181, 41))
        font = QtGui.QFont()
        font.setFamily("SF UI Display")
        font.setPointSize(10)
        font.setBold(True)
        self.import_button.setFont(font)
        self.import_button.setObjectName("import_button")
        self.save_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.save_button.setGeometry(QtCore.QRect(10, 60, 181, 41))
        font = QtGui.QFont()
        font.setFamily("SF UI Display")
        font.setPointSize(10)
        font.setBold(True)
        self.save_button.setFont(font)
        self.save_button.setObjectName("save_button")
        self.line = QtWidgets.QFrame(parent=self.centralwidget)
        self.line.setGeometry(QtCore.QRect(200, 10, 21, 571))
        self.line.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.progress_bar = QtWidgets.QProgressBar(parent=self.centralwidget)
        self.progress_bar.setGeometry(QtCore.QRect(10, 330, 181, 23))
        font = QtGui.QFont()
        font.setFamily("SF Pro Display")
        self.progress_bar.setFont(font)
        self.progress_bar.setProperty("value", 0)
        self.progress_bar.setObjectName("progress_bar")
        self.line_3 = QtWidgets.QFrame(parent=self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(10, 310, 181, 16))
        self.line_3.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_3.setObjectName("line_3")
        self.logMessage = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.logMessage.setGeometry(QtCore.QRect(10, 360, 181, 111))
        font = QtGui.QFont()
        font.setFamily("SF UI  Text")
        font.setKerning(False)
        self.logMessage.setFont(font)
        self.logMessage.setObjectName("logMessage")
        self.groupBox = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 480, 181, 80))
        self.groupBox.setObjectName("groupBox")
        self.label_2 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 30, 181, 16))
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(parent=self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 20, 181, 16))
        font = QtGui.QFont()
        font.setFamily("SF UI Display")
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.groupBox_2 = QtWidgets.QGroupBox(parent=self.groupBox)
        self.groupBox_2.setGeometry(QtCore.QRect(0, 0, 181, 80))
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_3 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(10, 30, 181, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(10, 20, 181, 16))
        font = QtGui.QFont()
        font.setFamily("SF UI Display")
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.Settings_Group = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.Settings_Group.setGeometry(QtCore.QRect(10, 110, 181, 141))
        self.Settings_Group.setObjectName("Settings_Group")
        self.comboBox_2 = QtWidgets.QComboBox(parent=self.Settings_Group)
        self.comboBox_2.setGeometry(QtCore.QRect(20, 110, 151, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.Convert_from = QtWidgets.QLabel(parent=self.Settings_Group)
        self.Convert_from.setGeometry(QtCore.QRect(20, 30, 161, 21))
        font = QtGui.QFont()
        font.setFamily("SF UI  Text Med")
        font.setPointSize(10)
        self.Convert_from.setFont(font)
        self.Convert_from.setObjectName("Convert_from")
        self.Convert_to = QtWidgets.QLabel(parent=self.Settings_Group)
        self.Convert_to.setGeometry(QtCore.QRect(20, 90, 161, 21))
        font = QtGui.QFont()
        font.setFamily("SF UI  Text Med")
        font.setPointSize(10)
        self.Convert_to.setFont(font)
        self.Convert_to.setObjectName("Convert_to")
        self.convert_from_comboBox = QtWidgets.QComboBox(parent=self.Settings_Group)
        self.convert_from_comboBox.setGeometry(QtCore.QRect(20, 50, 151, 22))
        self.convert_from_comboBox.setObjectName("convert_from_comboBox")
        self.convert_from_comboBox.addItem("")
        self.convert_from_comboBox.addItem("")
        self.convert_from_comboBox.addItem("")
        self.convert_from_comboBox.addItem("")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 711, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.convert_button.setText(_translate("MainWindow", "CONVERT"))
        self.import_button.setText(_translate("MainWindow", "IMPORT FILE"))
        self.save_button.setText(_translate("MainWindow", "SAVE TO"))
        self.groupBox.setTitle(_translate("MainWindow", "Information:"))
        self.label_2.setText(_translate("MainWindow", "Kenneth Gonzales (Mr.G)"))
        self.label.setText(_translate("MainWindow", "HESTIA CONVERTER"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Information:"))
        self.label_3.setText(_translate("MainWindow", "Kenneth Gonzales (Mr.G)"))
        self.label_4.setText(_translate("MainWindow", "HESTIA CONVERTER"))
        self.Settings_Group.setTitle(_translate("MainWindow", "Settings:"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", ".jpg"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", ".mp3"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", ".png"))
        self.Convert_from.setText(_translate("MainWindow", "Convert From..."))
        self.Convert_to.setText(_translate("MainWindow", "Convert To..."))
        self.convert_from_comboBox.setItemText(0, _translate("MainWindow", ".mp4"))
        self.convert_from_comboBox.setItemText(1, _translate("MainWindow", ".png"))
        self.convert_from_comboBox.setItemText(2, _translate("MainWindow", ".jpg"))
        self.convert_from_comboBox.setItemText(3, _translate("MainWindow", ".webp"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())