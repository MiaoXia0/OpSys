# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DialogPageWrite.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DiaWrite(object):
    def setupUi(self, DiaWrite):
        DiaWrite.setObjectName("DiaWrite")
        DiaWrite.resize(554, 94)
        self.buttonBox = QtWidgets.QDialogButtonBox(DiaWrite)
        self.buttonBox.setGeometry(QtCore.QRect(240, 60, 71, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.lblAddr = QtWidgets.QLabel(DiaWrite)
        self.lblAddr.setGeometry(QtCore.QRect(10, 10, 61, 16))
        self.lblAddr.setObjectName("lblAddr")
        self.radioWrite = QtWidgets.QRadioButton(DiaWrite)
        self.radioWrite.setGeometry(QtCore.QRect(20, 40, 51, 16))
        self.radioWrite.setChecked(True)
        self.radioWrite.setObjectName("radioWrite")
        self.lineAddr = QtWidgets.QLineEdit(DiaWrite)
        self.lineAddr.setGeometry(QtCore.QRect(70, 10, 471, 20))
        self.lineAddr.setObjectName("lineAddr")
        self.radioNotWrite = QtWidgets.QRadioButton(DiaWrite)
        self.radioNotWrite.setGeometry(QtCore.QRect(80, 40, 61, 16))
        self.radioNotWrite.setObjectName("radioNotWrite")

        self.retranslateUi(DiaWrite)
        self.buttonBox.accepted.connect(DiaWrite.accept)
        self.buttonBox.rejected.connect(DiaWrite.reject)
        QtCore.QMetaObject.connectSlotsByName(DiaWrite)

    def retranslateUi(self, DiaWrite):
        _translate = QtCore.QCoreApplication.translate
        DiaWrite.setWindowTitle(_translate("DiaWrite", "调用"))
        self.lblAddr.setText(_translate("DiaWrite", "页逻辑地址"))
        self.radioWrite.setText(_translate("DiaWrite", "修改"))
        self.radioNotWrite.setText(_translate("DiaWrite", "不修改"))