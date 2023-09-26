# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(787, 739)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(620, 520))
        MainWindow.setMouseTracking(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../icon.jpg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralWidget)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralWidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.layoutWidget = QtWidgets.QWidget(self.tab)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 394, 715, 236))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.tableWidget_result = QtWidgets.QTableWidget(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget_result.sizePolicy().hasHeightForWidth())
        self.tableWidget_result.setSizePolicy(sizePolicy)
        self.tableWidget_result.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.CursorShape.IBeamCursor))
        self.tableWidget_result.setAutoFillBackground(False)
        self.tableWidget_result.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.tableWidget_result.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.tableWidget_result.setLineWidth(1)
        self.tableWidget_result.setMidLineWidth(1)
        self.tableWidget_result.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.tableWidget_result.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.tableWidget_result.setAutoScroll(True)
        self.tableWidget_result.setAlternatingRowColors(True)
        self.tableWidget_result.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollMode.ScrollPerPixel)
        self.tableWidget_result.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollMode.ScrollPerPixel)
        self.tableWidget_result.setGridStyle(QtCore.Qt.PenStyle.SolidLine)
        self.tableWidget_result.setRowCount(5)
        self.tableWidget_result.setColumnCount(2)
        self.tableWidget_result.setObjectName("tableWidget_result")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_result.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_result.setHorizontalHeaderItem(1, item)
        self.tableWidget_result.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget_result.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_result.verticalHeader().setCascadingSectionResizes(False)
        self.horizontalLayout_2.addWidget(self.tableWidget_result)
        spacerItem = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.label_notes = QtWidgets.QLabel(self.layoutWidget)
        self.label_notes.setMinimumSize(QtCore.QSize(200, 25))
        self.label_notes.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(10)
        self.label_notes.setFont(font)
        self.label_notes.setAutoFillBackground(False)
        self.label_notes.setFrameShape(QtWidgets.QFrame.Shape.Panel)
        self.label_notes.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.label_notes.setText("")
        self.label_notes.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignTop)
        self.label_notes.setObjectName("label_notes")
        self.horizontalLayout_2.addWidget(self.label_notes)
        self.layoutWidget1 = QtWidgets.QWidget(self.tab)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 140, 715, 237))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setFormAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.formLayout.setSpacing(6)
        self.formLayout.setObjectName("formLayout")
        self.Label_target = QtWidgets.QLabel(self.layoutWidget1)
        self.Label_target.setObjectName("Label_target")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.Label_target)
        self.LineEdit_target = QtWidgets.QLineEdit(self.layoutWidget1)
        self.LineEdit_target.setMinimumSize(QtCore.QSize(200, 25))
        self.LineEdit_target.setStatusTip("")
        self.LineEdit_target.setObjectName("LineEdit_target")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.LineEdit_target)
        self.Label_user = QtWidgets.QLabel(self.layoutWidget1)
        self.Label_user.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.Label_user.setObjectName("Label_user")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.Label_user)
        self.LineEdit_user = QtWidgets.QLineEdit(self.layoutWidget1)
        self.LineEdit_user.setMinimumSize(QtCore.QSize(200, 25))
        self.LineEdit_user.setObjectName("LineEdit_user")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.LineEdit_user)
        self.Label_pwd = QtWidgets.QLabel(self.layoutWidget1)
        self.Label_pwd.setObjectName("Label_pwd")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.Label_pwd)
        self.LineEdit_pwd = QtWidgets.QLineEdit(self.layoutWidget1)
        self.LineEdit_pwd.setMinimumSize(QtCore.QSize(200, 25))
        self.LineEdit_pwd.setText("")
        self.LineEdit_pwd.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.LineEdit_pwd.setObjectName("LineEdit_pwd")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.LineEdit_pwd)
        self.gapLabel = QtWidgets.QLabel(self.layoutWidget1)
        self.gapLabel.setObjectName("gapLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.gapLabel)
        self.LineEdit_timegap = QtWidgets.QLineEdit(self.layoutWidget1)
        self.LineEdit_timegap.setMinimumSize(QtCore.QSize(200, 25))
        self.LineEdit_timegap.setObjectName("LineEdit_timegap")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.LineEdit_timegap)
        self.Label_time = QtWidgets.QLabel(self.layoutWidget1)
        self.Label_time.setObjectName("Label_time")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.ItemRole.LabelRole, self.Label_time)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lineEdit_timeStart = QtWidgets.QLineEdit(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_timeStart.sizePolicy().hasHeightForWidth())
        self.lineEdit_timeStart.setSizePolicy(sizePolicy)
        self.lineEdit_timeStart.setMinimumSize(QtCore.QSize(20, 0))
        self.lineEdit_timeStart.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_timeStart.setObjectName("lineEdit_timeStart")
        self.horizontalLayout_3.addWidget(self.lineEdit_timeStart)
        self.lineEdit_timeEnd = QtWidgets.QLineEdit(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_timeEnd.sizePolicy().hasHeightForWidth())
        self.lineEdit_timeEnd.setSizePolicy(sizePolicy)
        self.lineEdit_timeEnd.setMinimumSize(QtCore.QSize(50, 0))
        self.lineEdit_timeEnd.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_timeEnd.setObjectName("lineEdit_timeEnd")
        self.horizontalLayout_3.addWidget(self.lineEdit_timeEnd)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.label = QtWidgets.QLabel(self.layoutWidget1)
        self.label.setMinimumSize(QtCore.QSize(60, 0))
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.lineEdit_keyword = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineEdit_keyword.setMinimumSize(QtCore.QSize(20, 0))
        self.lineEdit_keyword.setObjectName("lineEdit_keyword")
        self.horizontalLayout_3.addWidget(self.lineEdit_keyword)
        self.formLayout.setLayout(4, QtWidgets.QFormLayout.ItemRole.FieldRole, self.horizontalLayout_3)
        self.horizontalLayout.addLayout(self.formLayout)
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(0, -1, -1, -1)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_start = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton_start.setMinimumSize(QtCore.QSize(20, 50))
        self.pushButton_start.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton_start.setIconSize(QtCore.QSize(24, 24))
        self.pushButton_start.setObjectName("pushButton_start")
        self.verticalLayout.addWidget(self.pushButton_start)
        self.checkBox = QtWidgets.QCheckBox(self.layoutWidget1)
        self.checkBox.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.checkBox.setStatusTip("")
        self.checkBox.setAutoFillBackground(True)
        self.checkBox.setChecked(True)
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout.addWidget(self.checkBox)
        self.pushButton_stop = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton_stop.setMinimumSize(QtCore.QSize(20, 50))
        self.pushButton_stop.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton_stop.setObjectName("pushButton_stop")
        self.verticalLayout.addWidget(self.pushButton_stop)
        self.horizontalLayout.addLayout(self.verticalLayout)
        spacerItem3 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.horizontalLayout.setStretch(0, 1)
        self.label_head = QtWidgets.QLabel(self.tab)
        self.label_head.setGeometry(QtCore.QRect(10, -3, 715, 141))
        self.label_head.setMinimumSize(QtCore.QSize(0, 120))
        self.label_head.setObjectName("label_head")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.Label_time_2 = QtWidgets.QLabel(self.tab_2)
        self.Label_time_2.setGeometry(QtCore.QRect(90, 190, 36, 21))
        self.Label_time_2.setObjectName("Label_time_2")
        self.lineEdit_keyword_2 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_keyword_2.setGeometry(QtCore.QRect(130, 190, 158, 20))
        self.lineEdit_keyword_2.setMinimumSize(QtCore.QSize(20, 0))
        self.lineEdit_keyword_2.setObjectName("lineEdit_keyword_2")
        self.label_head_2 = QtWidgets.QLabel(self.tab_2)
        self.label_head_2.setGeometry(QtCore.QRect(10, 0, 715, 124))
        self.label_head_2.setMinimumSize(QtCore.QSize(0, 120))
        self.label_head_2.setObjectName("label_head_2")
        self.pushButton_stop_2 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_stop_2.setGeometry(QtCore.QRect(520, 230, 80, 50))
        self.pushButton_stop_2.setMinimumSize(QtCore.QSize(20, 50))
        self.pushButton_stop_2.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton_stop_2.setObjectName("pushButton_stop_2")
        self.pushButton_start_2 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_start_2.setGeometry(QtCore.QRect(520, 154, 80, 50))
        self.pushButton_start_2.setMinimumSize(QtCore.QSize(20, 50))
        self.pushButton_start_2.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton_start_2.setIconSize(QtCore.QSize(24, 24))
        self.pushButton_start_2.setObjectName("pushButton_start_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.label_yf = QtWidgets.QLabel(self.tab_3)
        self.label_yf.setGeometry(QtCore.QRect(0, 120, 751, 331))
        self.label_yf.setText("")
        self.label_yf.setObjectName("label_yf")
        self.tabWidget.addTab(self.tab_3, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 787, 37))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.ToolBarArea.TopToolBarArea, self.mainToolBar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(2)
        self.pushButton_start.clicked.connect(self.Start_Run) # type: ignore
        self.pushButton_stop.clicked.connect(self.Stop_Run) # type: ignore
        self.pushButton_start_2.clicked.connect(self.Start_Run_2) # type: ignore
        self.pushButton_stop_2.clicked.connect(self.Stop_Run_2) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "微信公众号文章"))
        self.tableWidget_result.setSortingEnabled(False)
        item = self.tableWidget_result.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Title"))
        item = self.tableWidget_result.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "URL"))
        self.label_notes.setWhatsThis(_translate("MainWindow", "调试窗口"))
        self.Label_target.setText(_translate("MainWindow", "目标公众号英文名"))
        self.LineEdit_target.setPlaceholderText(_translate("MainWindow", "为空则默认新华社(xinhuashefabu1)"))
        self.Label_user.setText(_translate("MainWindow", "个人公众号账号"))
        self.LineEdit_user.setPlaceholderText(_translate("MainWindow", "为空则自动打开页面后手动输入"))
        self.Label_pwd.setText(_translate("MainWindow", "个人公众号密码"))
        self.LineEdit_pwd.setPlaceholderText(_translate("MainWindow", "为空则自动打开页面后手动输入"))
        self.gapLabel.setText(_translate("MainWindow", "查询间隔(s)"))
        self.LineEdit_timegap.setPlaceholderText(_translate("MainWindow", "为空则默认为5s,一页约10条，越短越快被限制"))
        self.Label_time.setText(_translate("MainWindow", "时间范围(年)"))
        self.lineEdit_timeStart.setPlaceholderText(_translate("MainWindow", "1999"))
        self.lineEdit_timeEnd.setPlaceholderText(_translate("MainWindow", "2019"))
        self.label.setText(_translate("MainWindow", "关键词"))
        self.pushButton_start.setText(_translate("MainWindow", "启动(*^▽^*)"))
        self.checkBox.setWhatsThis(_translate("MainWindow", "记住密码"))
        self.checkBox.setText(_translate("MainWindow", "记住密码"))
        self.pushButton_stop.setText(_translate("MainWindow", "终止￣へ￣"))
        self.label_head.setText(_translate("MainWindow", "****************************************************************************************************\n"
"* 程序原理:\n"
">> 通过selenium登录获取token和cookie，再自动爬取和下载\n"
"* 使用前提： *\n"
">> 电脑已装Firefox、Chrome、Opera、Edge等浏览器(默认Firefox驱动)\n"
">> 下载selenium驱动放入python安装目录，将目录添加至环境变量(https://www.seleniumhq.org/download/)\n"
">> 申请一个微信公众号(https://mp.weixin.qq.com)\n"
"                         Copyright © SXF  本软件禁止一切形式的商业活动\n"
"****************************************************************************************************"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "  公众号搜文章  "))
        self.Label_time_2.setText(_translate("MainWindow", "关键词"))
        self.label_head_2.setText(_translate("MainWindow", "****************************************************************************************************\n"
"* demo说明:\n"
">> 现在“公众号搜文章”页填完整信息\n"
">> 再在本页填入关键词\n"
">> 点击“启动”即可\n"
"                         Copyright © SXF  本软件禁止一切形式的商业活动\n"
"****************************************************************************************************"))
        self.pushButton_stop_2.setText(_translate("MainWindow", "终止￣へ￣"))
        self.pushButton_start_2.setText(_translate("MainWindow", "启动(*^▽^*)"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "  关键词搜文章  "))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "关于"))
