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

#PYQT USER INTERFACE ==> MAIN THREAD
class Main(QWidget, Ui_Form):

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        #method to setup the UI, defined in server_ui.py
        self.setupUi(self)
        #controller is instantiated here so it can be accessible for arduino thread and tcpServer thread
        self.c = Controller()

    def add(self, text):
        self.red_label.setStyleSheet(text)

    """---------------PyQt BUTTON LISTENERS---------------------"""
    #START TCP SERVER THREAD
    @pyqtSignature("")
    def on_start_server_btn_pressed(self):
        #this will start a tcpserver object in a different thread (main thread is gor GUI)
        #using for loop to avoid error raised by starting same thread
        for i in range(1):
            #pass controller object as tcp server receives commands to execute functions that will interact with
            #the robot that are defined in the controller
            t = TcpServer(self.c)
            t.setDaemon(True)
            t.start()

    #START ARDUINO SENSING THREAD
    @pyqtSignature("")
    def on_arduino_btn_pressed(self):
        #create an object arduino that will be executed on a separate thread
        #to get data from the arduino
        #using for loop to avoid error raised by starting same thread
        for i in range(1):
            #pass the controllet object so it can upload the sensor data to the controller instance
            #pass the Main object, inheriting from Ui_Form, to be able to upload sensor values in PyQt
            self.workThread = Arduino(self.c, self)
            self.connect( self.workThread, QtCore.SIGNAL("update(QString)"), self.add )
            self.workThread.start()

    #SHOW NUMBER OF THREADS ACTIVE AND DESCRIPTION
    @pyqtSignature("")
    def on_thread_btn_pressed(self):
        #get thread description
        threads = threading.enumerate()
        #process the thread description to show only thread name
        threads_string = []
        for thread in threads:
            string_thread = str(thread)
            thread_separated = string_thread.split('(')
            threads_string.append(thread_separated[0][1:] + '\n')
        #show number of active threads
        self.threads_lcd.display(threading.active_count())
        #show thread name
        self.threads_label.setText(''.join(threads_string))


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    dlg = Main()
    dlg.show()
    sys.exit(app.exec_())
