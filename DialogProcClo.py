# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DialogProcClo.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DiaClo(object):
    def setupUi(self, DiaClo):
        DiaClo.setObjectName("DiaClo")
        DiaClo.resize(208, 107)
        self.buttonBox = QtWidgets.QDialogButtonBox(DiaClo)
        self.buttonBox.setGeometry(QtCore.QRect(60, 70, 81, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(DiaClo)
        self.label.setGeometry(QtCore.QRect(10, 40, 54, 12))
        self.label.setObjectName("label")
        self.linePid = QtWidgets.QLineEdit(DiaClo)
        self.linePid.setGeometry(QtCore.QRect(80, 40, 113, 20))
        self.linePid.setObjectName("linePid")

        self.retranslateUi(DiaClo)
        self.buttonBox.accepted.connect(DiaClo.accept)
        self.buttonBox.rejected.connect(DiaClo.reject)
        QtCore.QMetaObject.connectSlotsByName(DiaClo)

    def retranslateUi(self, DiaClo):
        _translate = QtCore.QCoreApplication.translate
        DiaClo.setWindowTitle(_translate("DiaClo", "进程撤销"))
        self.label.setText(_translate("DiaClo", "PID"))
