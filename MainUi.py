# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainUi.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(541, 291)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 541, 291))
        self.tabWidget.setObjectName("tabWidget")
        self.tabProcess = QtWidgets.QWidget()
        self.tabProcess.setObjectName("tabProcess")
        self.lineSliceTime = QtWidgets.QLineEdit(self.tabProcess)
        self.lineSliceTime.setGeometry(QtCore.QRect(340, 0, 61, 20))
        self.lineSliceTime.setObjectName("lineSliceTime")
        self.label_6 = QtWidgets.QLabel(self.tabProcess)
        self.label_6.setGeometry(QtCore.QRect(10, 20, 54, 12))
        self.label_6.setObjectName("label_6")
        self.label_9 = QtWidgets.QLabel(self.tabProcess)
        self.label_9.setGeometry(QtCore.QRect(180, 0, 54, 16))
        self.label_9.setObjectName("label_9")
        self.lineBlocked = QtWidgets.QLineEdit(self.tabProcess)
        self.lineBlocked.setGeometry(QtCore.QRect(60, 40, 113, 20))
        self.lineBlocked.setReadOnly(True)
        self.lineBlocked.setObjectName("lineBlocked")
        self.lineReady = QtWidgets.QLineEdit(self.tabProcess)
        self.lineReady.setGeometry(QtCore.QRect(60, 0, 113, 20))
        self.lineReady.setReadOnly(True)
        self.lineReady.setObjectName("lineReady")
        self.btnProc = QtWidgets.QPushButton(self.tabProcess)
        self.btnProc.setGeometry(QtCore.QRect(400, 0, 75, 23))
        self.btnProc.setObjectName("btnProc")
        self.tableProc = QtWidgets.QTableView(self.tabProcess)
        self.tableProc.setGeometry(QtCore.QRect(10, 70, 511, 192))
        self.tableProc.setObjectName("tableProc")
        self.btnProcClos = QtWidgets.QPushButton(self.tabProcess)
        self.btnProcClos.setGeometry(QtCore.QRect(260, 30, 75, 23))
        self.btnProcClos.setObjectName("btnProcClos")
        self.label_8 = QtWidgets.QLabel(self.tabProcess)
        self.label_8.setGeometry(QtCore.QRect(300, 0, 41, 16))
        self.label_8.setObjectName("label_8")
        self.btnBlock = QtWidgets.QPushButton(self.tabProcess)
        self.btnBlock.setGeometry(QtCore.QRect(340, 30, 75, 23))
        self.btnBlock.setObjectName("btnBlock")
        self.lineRunning = QtWidgets.QLineEdit(self.tabProcess)
        self.lineRunning.setGeometry(QtCore.QRect(60, 20, 113, 20))
        self.lineRunning.setReadOnly(True)
        self.lineRunning.setObjectName("lineRunning")
        self.label_7 = QtWidgets.QLabel(self.tabProcess)
        self.label_7.setGeometry(QtCore.QRect(420, 30, 101, 16))
        self.label_7.setObjectName("label_7")
        self.btnProcCrea = QtWidgets.QPushButton(self.tabProcess)
        self.btnProcCrea.setGeometry(QtCore.QRect(180, 30, 75, 23))
        self.btnProcCrea.setObjectName("btnProcCrea")
        self.label_5 = QtWidgets.QLabel(self.tabProcess)
        self.label_5.setGeometry(QtCore.QRect(10, 40, 54, 12))
        self.label_5.setObjectName("label_5")
        self.label_4 = QtWidgets.QLabel(self.tabProcess)
        self.label_4.setGeometry(QtCore.QRect(10, 0, 54, 12))
        self.label_4.setObjectName("label_4")
        self.lineTimeSlice = QtWidgets.QLineEdit(self.tabProcess)
        self.lineTimeSlice.setGeometry(QtCore.QRect(230, 0, 61, 20))
        self.lineTimeSlice.setObjectName("lineTimeSlice")
        self.tabWidget.addTab(self.tabProcess, "")
        self.tabMemory = QtWidgets.QWidget()
        self.tabMemory.setObjectName("tabMemory")
        self.tablePages = QtWidgets.QTableView(self.tabMemory)
        self.tablePages.setGeometry(QtCore.QRect(10, 70, 521, 191))
        self.tablePages.setObjectName("tablePages")
        self.btnPageCrea = QtWidgets.QPushButton(self.tabMemory)
        self.btnPageCrea.setGeometry(QtCore.QRect(10, 10, 71, 23))
        self.btnPageCrea.setObjectName("btnPageCrea")
        self.btnPage = QtWidgets.QPushButton(self.tabMemory)
        self.btnPage.setGeometry(QtCore.QRect(10, 40, 71, 23))
        self.btnPage.setObjectName("btnPage")
        self.label = QtWidgets.QLabel(self.tabMemory)
        self.label.setGeometry(QtCore.QRect(90, 10, 61, 20))
        self.label.setObjectName("label")
        self.lineInMem = QtWidgets.QLineEdit(self.tabMemory)
        self.lineInMem.setGeometry(QtCore.QRect(150, 10, 111, 20))
        self.lineInMem.setReadOnly(True)
        self.lineInMem.setObjectName("lineInMem")
        self.lineLenMem = QtWidgets.QLineEdit(self.tabMemory)
        self.lineLenMem.setGeometry(QtCore.QRect(320, 10, 31, 20))
        self.lineLenMem.setObjectName("lineLenMem")
        self.lineLenPage = QtWidgets.QLineEdit(self.tabMemory)
        self.lineLenPage.setGeometry(QtCore.QRect(460, 10, 41, 20))
        self.lineLenPage.setObjectName("lineLenPage")
        self.label_2 = QtWidgets.QLabel(self.tabMemory)
        self.label_2.setGeometry(QtCore.QRect(270, 10, 54, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.tabMemory)
        self.label_3.setGeometry(QtCore.QRect(420, 10, 41, 21))
        self.label_3.setObjectName("label_3")
        self.btnLenSet = QtWidgets.QPushButton(self.tabMemory)
        self.btnLenSet.setGeometry(QtCore.QRect(500, 10, 31, 21))
        self.btnLenSet.setObjectName("btnLenSet")
        self.linePageNum = QtWidgets.QLineEdit(self.tabMemory)
        self.linePageNum.setGeometry(QtCore.QRect(480, 30, 16, 20))
        self.linePageNum.setReadOnly(True)
        self.linePageNum.setObjectName("linePageNum")
        self.label_10 = QtWidgets.QLabel(self.tabMemory)
        self.label_10.setGeometry(QtCore.QRect(350, 10, 41, 21))
        self.label_10.setObjectName("label_10")
        self.lineLenBlo = QtWidgets.QLineEdit(self.tabMemory)
        self.lineLenBlo.setGeometry(QtCore.QRect(390, 10, 31, 20))
        self.lineLenBlo.setObjectName("lineLenBlo")
        self.lineBlockNum = QtWidgets.QLineEdit(self.tabMemory)
        self.lineBlockNum.setGeometry(QtCore.QRect(510, 30, 16, 20))
        self.lineBlockNum.setReadOnly(True)
        self.lineBlockNum.setObjectName("lineBlockNum")
        self.lineLenAddr = QtWidgets.QLineEdit(self.tabMemory)
        self.lineLenAddr.setGeometry(QtCore.QRect(510, 50, 21, 20))
        self.lineLenAddr.setReadOnly(True)
        self.lineLenAddr.setObjectName("lineLenAddr")
        self.label_11 = QtWidgets.QLabel(self.tabMemory)
        self.label_11.setGeometry(QtCore.QRect(460, 30, 16, 20))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.tabMemory)
        self.label_12.setGeometry(QtCore.QRect(500, 30, 16, 20))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.tabMemory)
        self.label_13.setGeometry(QtCore.QRect(460, 50, 51, 20))
        self.label_13.setObjectName("label_13")
        self.tabWidget.addTab(self.tabMemory, "")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(440, 290, 101, 20))
        self.label_14.setObjectName("label_14")
        MainWindow.setCentralWidget(self.centralwidget)
        self.actProcCre = QtWidgets.QAction(MainWindow)
        self.actProcCre.setObjectName("actProcCre")
        self.actProcRev = QtWidgets.QAction(MainWindow)
        self.actProcRev.setObjectName("actProcRev")

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "操作系统课程设计"))
        self.lineSliceTime.setText(_translate("MainWindow", "2"))
        self.label_6.setText(_translate("MainWindow", "Running"))
        self.label_9.setText(_translate("MainWindow", "时间片数"))
        self.btnProc.setText(_translate("MainWindow", "调度模拟"))
        self.btnProcClos.setText(_translate("MainWindow", "进程撤销"))
        self.label_8.setText(_translate("MainWindow", "时间片"))
        self.btnBlock.setText(_translate("MainWindow", "进程阻塞"))
        self.label_7.setText(_translate("MainWindow", "(时间片轮转调度)"))
        self.btnProcCrea.setText(_translate("MainWindow", "进程创建"))
        self.label_5.setText(_translate("MainWindow", "Blocked"))
        self.label_4.setText(_translate("MainWindow", "Ready"))
        self.lineTimeSlice.setText(_translate("MainWindow", "5"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabProcess), _translate("MainWindow", "进程管理"))
        self.btnPageCrea.setText(_translate("MainWindow", "页表添加页"))
        self.btnPage.setText(_translate("MainWindow", "页调用"))
        self.label.setText(_translate("MainWindow", "主存中页号"))
        self.lineLenMem.setText(_translate("MainWindow", "4096"))
        self.lineLenPage.setText(_translate("MainWindow", "1024"))
        self.label_2.setText(_translate("MainWindow", "主存大小"))
        self.label_3.setText(_translate("MainWindow", "页大小"))
        self.btnLenSet.setText(_translate("MainWindow", "设置"))
        self.linePageNum.setText(_translate("MainWindow", "4"))
        self.label_10.setText(_translate("MainWindow", "块大小"))
        self.lineLenBlo.setText(_translate("MainWindow", "1024"))
        self.lineBlockNum.setText(_translate("MainWindow", "4"))
        self.lineLenAddr.setText(_translate("MainWindow", "12"))
        self.label_11.setText(_translate("MainWindow", "页"))
        self.label_12.setText(_translate("MainWindow", "块"))
        self.label_13.setText(_translate("MainWindow", "地址长度"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabMemory), _translate("MainWindow", "存储管理"))
        self.label_14.setText(_translate("MainWindow", "20181205049 黄铮"))
        self.actProcCre.setText(_translate("MainWindow", "进程创建"))
        self.actProcRev.setText(_translate("MainWindow", "进程撤销"))
