import serial
import time
import threading
import sys
from PyQt4.QtCore import *

#inhering from QThread instead of threading thread (python thread)
#because this thread needs to modify main thread (UI), and therefore
#PyQt threads (QThreads) are mandatory to use
class Arduino(QThread):
    def __init__(self, c, f):
        QThread.__init__(self)
        self.ser = serial.Serial("/dev/ttyACM0",9600)  #change ACM number as found from ls /dev/tty/ACM*
        self.ser.baudrate=9600
        self.c = c
        self.f = f

    def __del__(self):
        self.wait()

    def run(self):

        while True:
            read_ser = self.ser.readline()

            try:
                read_ser = int(read_ser)
                self.c.ULTRASONIC_SENSOR = float(read_ser)
                self.f.ultrasonic_lcd.display(self.c.ULTRASONIC_SENSOR)


            except ValueError as e:
                print "error: " + read_ser

            #Safety prevention for collision
            if read_ser < 30 and self.c.SAFETY == False:
                self.c.SAFETY = True
                self.c.stop(self.c.SAFETY)
                self.c.turn_red_led_on()
                self.emit( SIGNAL('update(QString)'), "background-color: red")

                while self.c.SAFETY == True:
                    read_ser = self.ser.readline()

                    try:
                        read_ser = int(read_ser)
                        self.c.ULTRASONIC_SENSOR = float(read_ser)
                        self.f.ultrasonic_lcd.display(self.c.ULTRASONIC_SENSOR)

                    except ValueError as e:
                        print "error: " + read_ser

                    if read_ser >= 30:
                        self.c.SAFETY = False
                        self.c.turn_led_off()
                        #emit signal to main thread (UI) that will trigger a function
                        #that will change the red led dashboard label
                        self.emit( SIGNAL('update(QString)'), "background-color: white")
                        print "No danger of collision"

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
