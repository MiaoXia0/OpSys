# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DialogPageCrea.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DiaPage(object):
    def setupUi(self, DiaPage):
        DiaPage.setObjectName("DiaPage")
        DiaPage.resize(192, 132)
        self.btnCrea = QtWidgets.QPushButton(DiaPage)
        self.btnCrea.setGeometry(QtCore.QRect(80, 100, 75, 23))
        self.btnCrea.setObjectName("btnCrea")
        self.linePage = QtWidgets.QLineEdit(DiaPage)
        self.linePage.setGeometry(QtCore.QRect(60, 10, 113, 20))
        self.linePage.setObjectName("linePage")
        self.label = QtWidgets.QLabel(DiaPage)
        self.label.setGeometry(QtCore.QRect(10, 10, 41, 16))
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(DiaPage)
        self.label_3.setGeometry(QtCore.QRect(10, 40, 51, 16))
        self.label_3.setObjectName("label_3")
        self.lineExt = QtWidgets.QLineEdit(DiaPage)
        self.lineExt.setGeometry(QtCore.QRect(60, 40, 113, 20))
        self.lineExt.setObjectName("lineExt")
        self.checkBox = QtWidgets.QCheckBox(DiaPage)
        self.checkBox.setGeometry(QtCore.QRect(10, 100, 71, 16))
        self.checkBox.setObjectName("checkBox")
        self.lineMain = QtWidgets.QLineEdit(DiaPage)
        self.lineMain.setEnabled(False)
        self.lineMain.setGeometry(QtCore.QRect(60, 70, 113, 20))
        self.lineMain.setObjectName("lineMain")
        self.label_4 = QtWidgets.QLabel(DiaPage)
        self.label_4.setGeometry(QtCore.QRect(10, 70, 51, 16))
        self.label_4.setObjectName("label_4")

        self.retranslateUi(DiaPage)
        self.btnCrea.clicked.connect(DiaPage.accept)
        QtCore.QMetaObject.connectSlotsByName(DiaPage)

    def retranslateUi(self, DiaPage):
        _translate = QtCore.QCoreApplication.translate
        DiaPage.setWindowTitle(_translate("DiaPage", "Dialog"))
        self.btnCrea.setText(_translate("DiaPage", "创建"))
        self.label.setText(_translate("DiaPage", "页号"))
        self.label_3.setText(_translate("DiaPage", "辅存块号"))
        self.checkBox.setText(_translate("DiaPage", "在主存中"))
        self.label_4.setText(_translate("DiaPage", "主存块号"))
