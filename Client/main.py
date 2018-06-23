from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import pyqtSignature
from PyQt4.QtGui import QWidget
import sys, time, datetime
import socket
import threading
from tcpclient import TcpClient
from client_ui import Ui_Form
from commands import Commands

class Main(QWidget, Ui_Form):

    tcp_client = TcpClient()

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.setupUi(self)

    @pyqtSignature("")
    def on_connect_btn_pressed(self):
        try:
            self.tcp_client.connect_to_server()
        except Exception, e:
            print "Connect to server Faild!: Server IP is right? Server is opend?", e
        print "Connecttion Successful !"

    @pyqtSignature("")
    def on_forward_btn_pressed(self):
        try:
            self.tcp_client.send_data(Commands.CMD_FORWARD)
        except Exception, e:
            print "Failed to send data", e

    @pyqtSignature("")
    def on_forward_btn_released(self):
        try:
            self.tcp_client.send_data(Commands.CMD_STOP)
        except Exception, e:
            print "Failed to send data", e

    @pyqtSignature("")
    def on_backward_btn_pressed(self):
        try:
            self.tcp_client.send_data(Commands.CMD_BACKWARD)
        except Exception, e:
            print "Failed to send data", e

    @pyqtSignature("")
    def on_backward_btn_released(self):
        try:
            self.tcp_client.send_data(Commands.CMD_STOP)
        except Exception, e:
            print "Failed to send data", e


    def keyPressEvent(self,event):
        if event.key() == Qt.Key_Up:
            try:
                self.tcp_client.send_data(Commands.CMD_FORWARD)
            except Exception, e:
                print "Failed to send data", e

    def keyReleaseEvent (self, event):
        if event.key() == Qt.Key_Up:
            try:
                self.tcp_client.send_data(Commands.CMD_STOP)
            except Exception, e:
                print "Failed to send data", e


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    dlg = Main()
    dlg.show()
    sys.exit(app.exec_())
