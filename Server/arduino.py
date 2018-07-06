import serial
import time
import threading
import sys
from PyQt4.QtCore import *

#inhering from QThread instead of threading thread (python thread)
#because this thread needs to modify main thread (UI), and therefore
#PyQt threads (QThreads) are mandatory to use
class Arduino(QThread):
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
                self.emit( SIGNAL('update_lcd(QString)'),str(self.c.ULTRASONIC_SENSOR))


            except ValueError as e:
                print "error: " + read_ser

            #Safety prevention for collision
            if read_ser < 30 and self.c.SAFETY == False:
                #safety stop triggered, safety boolean = true
                self.c.SAFETY = True
                #send a command stop
                self.c.stop(self.c.SAFETY)
                #turn red led on
                self.c.turn_red_led_on()
                #emit signal to update UI
                self.emit( SIGNAL('update(QString)'), "background-color: red")

                while self.c.SAFETY == True:
                    read_ser = self.ser.readline()

                    try:
                        read_ser = int(read_ser)
                        self.c.ULTRASONIC_SENSOR = float(read_ser)
                        #emit signal to update UI
                        self.emit( SIGNAL('update_lcd(QString)'),str(self.c.ULTRASONIC_SENSOR))


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
