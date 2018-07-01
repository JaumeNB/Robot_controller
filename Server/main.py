from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import pyqtSignature
from PyQt4.QtGui import QWidget
import sys, time, datetime
import socket
import threading
from tcpserver import TcpServer
from arduino import Arduino
from server_ui import Ui_Form
from controller import Controller


class Main(QWidget, Ui_Form):

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.setupUi(self)
        self.c = Controller()

    """---------------PyQt BUTTON LISTENERS---------------------"""
    @pyqtSignature("")
    def on_start_server_btn_pressed(self):
        #this will start a tcpserver object in a different thread (main thread is gor GUI)
        #using for loop to avoid error raised by starting same thread
        for i in range(1):
            t = TcpServer(self.c)
            t.setDaemon(True)
            t.start()

    @pyqtSignature("")
    def on_arduino_btn_pressed(self):
        #this will start a tcpserver object in a different thread (main thread is gor GUI)
        #using for loop to avoid error raised by starting same thread
        for i in range(1):
            a = Arduino(self.c)
            a.setDaemon(True)
            a.start()

    @pyqtSignature("")
    def on_thread_btn_pressed(self):
        #check how many threads are active and a description
        threads = threading.enumerate()

        list_threads = []

        for thread in threads:
            string_thread = str(thread)
            thread_separated = string_thread.split('(')
            list_threads.append(thread_separated[0] + '\n')

        self.threads_lcd.display(threading.active_count())
        self.threads_text.setText(str(list_threads))

    @pyqtSignature("")
    def on_ultrasonic_btn_pressed(self):
        #check how many threads are active and a description
        self.threads_lcd.display(self.c.ULTRASONIC_SENSOR)


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    dlg = Main()
    dlg.show()
    sys.exit(app.exec_())
