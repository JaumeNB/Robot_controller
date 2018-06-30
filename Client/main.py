from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *
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

    """--------------------KEYBOARD COMMANDS----------------------"""
    #PRESS A KEY
    def keyPressEvent(self,event):

        #print key pressed
        print "You Pressed Key : ", event.key(), event.text()

        #R: turn ON red led
        if event.key() == Qt.Key_R:
            self.tcp_client.send_data(Commands.CMD_RGB_R)
        #G: turn ON green led
        elif event.key() == Qt.Key_G:
            self.tcp_client.send_data(Commands.CMD_RGB_G)
        #B: turn ON blue led
        elif event.key() == Qt.Key_B:
            self.tcp_client.send_data(Commands.CMD_RGB_B)
        #O: turn OFF led
        elif event.key() == Qt.Key_O:
            self.tcp_client.send_data(Commands.CMD_RGB_OFF)
        #I: go forward
        elif event.key() == Qt.Key_I:
            self.tcp_client.send_data(Commands.CMD_FORWARD)
        #K: go backwards
        elif event.key() == Qt.Key_K:
            self.tcp_client.send_data(Commands.CMD_BACKWARD)
        #J: turn left
        elif event.key() == Qt.Key_J:
            self.tcp_client.send_data(Commands.CMD_TURN_LEFT)
        #L: turn right
        elif event.key() == Qt.Key_L:
            self.tcp_client.send_data(Commands.CMD_TURN_RIGHT)
        #SPACE: stop
        elif event.key() == Qt.Key_Space:
            self.tcp_client.send_data(Commands.CMD_TURN_STOP)

    #RELEASE A KEY
    def keyReleaseEvent(self, event):

        if event.isAutoRepeat():
            pass
        else:
            print "You Released Key : ", event.key()

            #if event.key() == Qt.Key_I or event.key() == Qt.Key_K :
                #self.tcp_client.send_data(Commands.CMD_STOP)


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    dlg = Main()
    dlg.show()
    sys.exit(app.exec_())
