import serial
import RPi.GPIO as GPIO
import time
import threading
import sys

class Arduino(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.ser = serial.Serial("/dev/ttyACM0",9600)  #change ACM number as found from ls /dev/tty/ACM*
        self.ser.baudrate=9600

    def run (self):
        while True:
            read_ser = self.ser.readline()
            print(read_ser)

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
