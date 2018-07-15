import serial
import time
import threading
import sys
from PyQt4.QtCore import *

#inhering from QThread instead of threading thread (python thread)
#because this thread needs to modify main thread (UI), and therefore
#PyQt threads (QThreads) are mandatory to use
class Arduino_Thread(QThread):
    def __init__(self, c):
        QThread.__init__(self)
        self.ser = serial.Serial("/dev/ttyACM0",9600)  #change ACM number as found from ls /dev/tty/ACM*
        self.ser.baudrate=9600
        self.c = c

    def __del__(self):
        self.wait()

    def run(self):

        while True:
            read_ser = self.ser.readline()

            try:
                #read serial (data coming from arduino)
                read_ser = int(read_ser)
                #assign distance value to controller object
                self.c.ULTRASONIC_SENSOR = float(read_ser)
                #emit signal to update UI
                self.emit( SIGNAL('update_ultrasonic_distance_lcd(QString)'),str(self.c.ULTRASONIC_SENSOR))

                if read_ser < 30:
                    #safety stop triggered
                    self.c.SAFETY = True
                    #turn red led on
                    self.c.turn_red_led_on()
                    #emit signal to update UI
                    self.emit( SIGNAL('update_led_label(QString, QString)'), "red", "background-color: red")
                    print "safety stop"

                else:
                    #safety stop deactivated
                    self.c.SAFETY = False
                    #turn off leds
                    self.c.turn_led_off()
                    #emit signal to main thread (UI) that will trigger a function
                    #that will change the red led dashboard label
                    self.emit( SIGNAL('update_led_label(QString, QString)'), "red", "background-color: white")
                    print "No danger of collision"

            except ValueError as e:
                print "error: " + read_ser


def Main():
    ard = Arduino()
    ard.run()
    print 'Exiting'

if __name__ == '__main__':
    try:
        Main()
    except KeyboardInterrupt:
        print 'Interrupted'
        sys.exit(0)
