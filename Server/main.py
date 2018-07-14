from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import pyqtSignature
from PyQt4.QtGui import QWidget
import sys, time, datetime
import socket
import threading
from server_ui import Ui_Form
from controller import Controller
from tcpserver import TcpServer
from arduino_thread import Arduino_Thread
from controller_thread import Controller_Thread
from auto_thread import Auto_Thread

#PYQT USER INTERFACE ==> MAIN THREAD
class Main(QWidget, Ui_Form):

    """---------------INSTANCE METHODS---------------------"""

    """SLOT FUNCTIONS"""
    #UPDATE UI LED INDICATOR
    def update_led_indicator(self, led, text):
        if led == "red":
            self.red_label.setStyleSheet(text)
            self.green_label.setStyleSheet("background-color: white")
            self.blue_label.setStyleSheet("background-color: white")
        elif led == "green":
            self.red_label.setStyleSheet("background-color: white")
            self.green_label.setStyleSheet(text)
            self.blue_label.setStyleSheet("background-color: white")
        elif led == "blue":
            self.red_label.setStyleSheet("background-color: white")
            self.green_label.setStyleSheet("background-color: white")
            self.blue_label.setStyleSheet(text)
        elif led == "off":
            self.red_label.setStyleSheet(text)
            self.green_label.setStyleSheet(text)
            self.blue_label.setStyleSheet(text)

    #UPDATE ULTRASONIC SENSOR LCD SCREEN
    def update_ultrasonic_distance_lcd(self, text):
        self.ultrasonic_distance_lcd.display(text)

    #UPDATE ULTRASONIC ORIENTATION LCD SCREEN
    def update_ultrasonic_orientation_lcd(self, text):
        self.ultrasonic_orientation_lcd.display(text)

    #UPDATE CAR ORIENTATION LCD SCREEN
    def update_wheel_orientation_lcd(self, text):
        self.wheel_orientation_lcd.display(text)

    """PyQt BUTTON LISTENERS"""
    #START TCP SERVER THREAD
    @pyqtSignature("")
    def on_start_server_btn_pressed(self):

        if self.auto_thread_active = True:
            print "Stop Auto Thread..."
            self.AutoThread.terminate()
            self.tcp_thread_active = False

        #this will start a tcpserver object in a different thread (main thread is gor GUI)
        #using for loop to avoid error raised by starting same thread
        for i in range(1):
            #pass controller object as tcp server receives commands to execute functions that will interact with
            #the robot that are defined in the controller
            self.TCPThread = TcpServer(self.c)
            #connect signal (emit in this workthread) and slot (function add)
            self.connect( self.workThread, QtCore.SIGNAL("update_led_label(QString, QString)"), self.update_led_indicator )
            self.connect( self.workThread, QtCore.SIGNAL("update_ultrasonic_orientation_lcd(QString)"), self.update_ultrasonic_orientation_lcd )
            self.connect( self.workThread, QtCore.SIGNAL("update_wheel_orientation_lcd(QString)"), self.update_wheel_orientation_lcd )
            #start thread
            self.TCPThread.start()
            self.tcp_thread_active = True

    #START AUTONOMOUS MODE
    @pyqtSignature("")
    def on_auto_btn_pressed(self):

        if self.tcp_thread_active == True:
            print "Stop TCP Server Thread..."
            self.TCPThread.stopTCPServer()
            self.TCPThread.terminate()
            self.tcp_thread_active = False

        for i in range(1):
            self.AutoThread = Auto_Thread(self.c)
            #start thread
            self.AutoThread.start()
            self.auto_thread_active = True

    """THREAD FUNCTIONS"""
    #START ARDUINO SENSING THREAD
    def start_arduino_thread(self):
        #create an object arduino that will be executed on a separate thread
        #to get data from the arduino
        #using for loop to avoid error raised by starting same thread
        for i in range(1):
            #pass the controllet object so it can upload the sensor data to the controller instance
            #pass the Main object, inheriting from Ui_Form, to be able to upload sensor values in PyQt
            #using a QThread that will be able to talk to this thread (main one)
            #through signals and slots
            self.workThread = Arduino_Thread(self.c)
            #connect signal (emit in this workthread) and slot (function add)
            self.connect( self.workThread, QtCore.SIGNAL("update_led_label(QString, QString)"), self.update_led_indicator )
            self.connect( self.workThread, QtCore.SIGNAL("update_ultrasonic_distance_lcd(QString)"), self.update_ultrasonic_distance_lcd )

            #start thread
            self.workThread.start()

    """---------------CLASS CONSTRUCTOR---------------------"""
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        #method to setup the UI, defined in server_ui.py
        self.setupUi(self)
        #controller is instantiated here so it can be accessible
        #for arduino thread, controler thread
        #and tcpServer thread
        self.c = Controller()
        #start arduino thread
        self.start_arduino_thread()

        self.tcp_thread_active = False
        self.auto_thread_active = False

"""----------------------MAIN PROGRAM---------------------------"""
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    dlg = Main()
    dlg.show()
    sys.exit(app.exec_())
