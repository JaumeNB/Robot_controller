import serial
import time
import threading
import sys

class Arduino():
    def __init__(self):
        self.ser = serial.Serial("/dev/ttyACM0",9600)  #change ACM number as found from ls /dev/tty/ACM*
        self.ser.baudrate=9600

    def run(self):

        safety = False

        while True:

            try:
                read_ser = self.ser.readline()
                read_ser = int(read_ser)
                print read_ser
            except:
                print "error"

            #Safety prevention for collision
            if read_ser < 20 and safety == False:
                safety = True
                print "safety stop"

                while safety == True:
                    try:
                        read_ser = self.ser.readline()
                        read_ser = int(read_ser)
                        print read_ser
                    except:
                        print "error"

                    if read_ser >= 20:
                        safety = False
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
