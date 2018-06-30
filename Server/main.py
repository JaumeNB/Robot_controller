from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import pyqtSignature
from PyQt4.QtGui import QWidget
import sys, time, datetime
import socket
import threading
from tcpserver import TcpServer
from server_ui import Ui_Form
from PyQt4.QtCore import QObject, pyqtSignal, pyqtSlot


class Main(QWidget, Ui_Form):



    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.setupUi(self)



    """---------------PyQt BUTTON LISTENERS---------------------"""
    @pyqtSignature("")
    def on_start_server_btn_pressed(self):
        #this will start a tcpserver object in a different thread (main thread is gor GUI)
        #using for loop to avoid error raised by starting same thread
        for i in range(1):
            t = TcpServer()
            t.setDaemon(True)
            t.start()


    @pyqtSignature("")
    def on_red_btn_pressed(self):
        self.red_btn.setStyleSheet("background-color: red")
        self.red_btn.setText('RED')

    @pyqtSlot(int)
    def on_moved(x):
        self.red_btn.setText(x)



if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    dlg = Main()
    dlg.show()
    sys.exit(app.exec_())
