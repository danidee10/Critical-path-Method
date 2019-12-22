from PyQt5 import QtCore, QtGui ,QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(995, 717)
        MainWindow.setMinimumSize(QtCore.QSize(995, 695))
        MainWindow.setMaximumSize(QtCore.QSize(995, 695))
        MainWindow.setStyleSheet("background-color: rgb(63, 63, 63); color: #ffffff;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(0, 40, 740, 301))
        self.tableWidget.setMaximumSize(QtCore.QSize(740, 301))
        self.tableWidget.setStyleSheet("background-color: #ffffff; color: #000;")
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        self.resultWidget = QtWidgets.QFrame(self.centralwidget)
        self.resultWidget.setGeometry(QtCore.QRect(745, 2, 245, 338))
        self.resultWidget.setStyleSheet("QFrame{\n"
"border: 1px solid #ffffff;\n"
"}\n"
"\n"
"QLabel{\n"
"border:none;\n"
"}\n"
"\n"
"QMenu{\n"
"background-color: red;\n"
"}")
        self.resultWidget.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.resultWidget.setFrameShadow(QtWidgets.QFrame.Raised)
        self.resultWidget.setObjectName("resultWidget")
        self.efficiencyLabel = QtWidgets.QLabel(self.resultWidget)
        self.efficiencyLabel.setGeometry(QtCore.QRect(10, 190, 221, 17))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.efficiencyLabel.setFont(font)
        self.efficiencyLabel.setText("")
        self.efficiencyLabel.setObjectName("efficiencyLabel")
        self.criticalPathLabel = QtWidgets.QLabel(self.resultWidget)
        self.criticalPathLabel.setGeometry(QtCore.QRect(10, 40, 211, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.criticalPathLabel.setFont(font)
        self.criticalPathLabel.setStyleSheet("")
        self.criticalPathLabel.setText("")
        self.criticalPathLabel.setObjectName("criticalPathLabel")
        self.projectDurationLabel = QtWidgets.QLabel(self.resultWidget)
        self.projectDurationLabel.setGeometry(QtCore.QRect(10, 120, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.projectDurationLabel.setFont(font)
        self.projectDurationLabel.setStyleSheet("")
        self.projectDurationLabel.setText("")
        self.projectDurationLabel.setObjectName("projectDurationLabel")
        self.efficiencyTitle = QtWidgets.QLabel(self.resultWidget)
        self.efficiencyTitle.setGeometry(QtCore.QRect(10, 170, 221, 17))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(13)
        font.setWeight(75)
        font.setBold(True)
        self.efficiencyTitle.setFont(font)
        self.efficiencyTitle.setStyleSheet("font-family: \'Ubuntu\'; font-weight: bold;")
        self.efficiencyTitle.setText("")
        self.efficiencyTitle.setObjectName("efficiencyTitle")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(0, 343, 991, 351))
        self.scrollArea.setStyleSheet("border: none;")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.networkDiagram = QtWidgets.QLabel(self.scrollArea)
        self.networkDiagram.setGeometry(QtCore.QRect(10, 0, 981, 341))
        self.networkDiagram.setText("")
        self.networkDiagram.setObjectName("networkDiagram")
        self.scrollArea.setWidget(self.networkDiagram)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 741, 39))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 3, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.calculateButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(14)
        font.setWeight(50)
        font.setUnderline(False)
        font.setBold(False)
        self.calculateButton.setFont(font)
        self.calculateButton.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.calculateButton.setStyleSheet("QPushButton {\n"
"background-color: rgb(85, 170, 0); \n"
"color: #ffffff; \n"
"border: 1px solid rgb(85, 170, 0); \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"color: #333;\n"
"border: 1px solid #ffffff;\n"
"}")
        self.calculateButton.setObjectName("calculateButton")
        self.horizontalLayout.addWidget(self.calculateButton)
        self.addRowButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(14)
        font.setWeight(50)
        font.setBold(False)
        self.addRowButton.setFont(font)
        self.addRowButton.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.addRowButton.setStyleSheet("QPushButton {\n"
"color: #ffffff;\n"
"background-color: rgb(85, 170, 0); \n"
"border: 1px solid rgb(85, 170, 0); \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"color: #333;\n"
"border: 1px solid #ffffff;\n"
"}\n"
"")
        self.addRowButton.setObjectName("addRowButton")
        self.horizontalLayout.addWidget(self.addRowButton)
        self.delRowButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(14)
        font.setWeight(50)
        font.setBold(False)
        self.delRowButton.setFont(font)
        self.delRowButton.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.delRowButton.setStyleSheet("QPushButton{\n"
"color: #ffffff; \n"
"background-color:  \n"
"tomato; \n"
"border: 1px solid tomato; \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"color: #333;\n"
"border: 1px solid #ffffff;\n"
"}")
        self.delRowButton.setObjectName("delRowButton")
        self.horizontalLayout.addWidget(self.delRowButton)
        self.viewResourceButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(14)
        font.setWeight(50)
        font.setBold(False)
        self.viewResourceButton.setFont(font)
        self.viewResourceButton.setStyleSheet("QPushButton {\n"
"background-color: rgb(85, 170, 0); \n"
"color: #ffffff; \n"
"border: 1px solid rgb(85, 170, 0); \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"color: #333;\n"
"border: 1px solid #ffffff;\n"
"}")
        self.viewResourceButton.setObjectName("viewResourceButton")
        self.horizontalLayout.addWidget(self.viewResourceButton)
        self.clearButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(14)
        font.setWeight(50)
        font.setBold(False)
        self.clearButton.setFont(font)
        self.clearButton.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.clearButton.setStyleSheet("QPushButton{\n"
"color: #ffffff; \n"
"background-color:  tomato; \n"
"border: 1px solid tomato; \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"color: #333;\n"
"border: 1px solid #ffffff;\n"
"}")
        self.clearButton.setObjectName("clearButton")
        self.horizontalLayout.addWidget(self.clearButton)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 995, 21))
        self.menubar.setStyleSheet("background: none; color: black;")
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow","Maven", None ))
        self.tableWidget.horizontalHeaderItem(0).setText(QtWidgets.QApplication.translate("MainWindow", "Id", None))
        self.tableWidget.horizontalHeaderItem(1).setText(QtWidgets.QApplication.translate("MainWindow", "Description", None))
        self.tableWidget.horizontalHeaderItem(1).setWhatsThis(QtWidgets.QApplication.translate("MainWindow", "The Description is optional and not needed for the calculation", None))
        self.tableWidget.horizontalHeaderItem(2).setText(QtWidgets.QApplication.translate("MainWindow", "Predecessor(s)", None))
        self.tableWidget.horizontalHeaderItem(3).setText(QtWidgets.QApplication.translate("MainWindow", "Duration", None))
        self.tableWidget.horizontalHeaderItem(4).setText(QtWidgets.QApplication.translate("MainWindow", "Resources", None))
        self.tableWidget.horizontalHeaderItem(5).setText(QtWidgets.QApplication.translate("MainWindow", "EST", None))
        self.tableWidget.horizontalHeaderItem(6).setText(QtWidgets.QApplication.translate("MainWindow", "LST", None))
        self.calculateButton.setText(QtWidgets.QApplication.translate("MainWindow", "calculate", None))
        self.addRowButton.setText(QtWidgets.QApplication.translate("MainWindow", "add row", None))
        self.delRowButton.setText(QtWidgets.QApplication.translate("MainWindow", "delete row", None))
        self.viewResourceButton.setText(QtWidgets.QApplication.translate("MainWindow", "view resource loading", None,))
        self.clearButton.setText(QtWidgets.QApplication.translate("MainWindow", "Clear", None))

