from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication
import sys

from MyMainWindow import MyMainWindow

if __name__ == '__main__':
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)
    MainWindow = MyMainWindow()
    MainWindow.show()
    sys.exit(app.exec_())  # 运行窗口执行完后结束程序
