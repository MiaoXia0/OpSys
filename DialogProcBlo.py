# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DialogProcBlo.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DiaBlo(object):
    def setupUi(self, DiaBlo):
        DiaBlo.setObjectName("DiaBlo")
        DiaBlo.resize(209, 104)
        self.buttonBox = QtWidgets.QDialogButtonBox(DiaBlo)
        self.buttonBox.setGeometry(QtCore.QRect(50, 70, 81, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(DiaBlo)
        self.label.setGeometry(QtCore.QRect(10, 40, 54, 12))
        self.label.setObjectName("label")
        self.linePid = QtWidgets.QLineEdit(DiaBlo)
        self.linePid.setGeometry(QtCore.QRect(80, 40, 113, 20))
        self.linePid.setObjectName("linePid")

        self.retranslateUi(DiaBlo)
        self.buttonBox.accepted.connect(DiaBlo.accept)
        self.buttonBox.rejected.connect(DiaBlo.reject)
        QtCore.QMetaObject.connectSlotsByName(DiaBlo)

    def retranslateUi(self, DiaBlo):
        _translate = QtCore.QCoreApplication.translate
        DiaBlo.setWindowTitle(_translate("DiaBlo", "进程阻塞"))
        self.label.setText(_translate("DiaBlo", "PID"))
