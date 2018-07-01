import serial
import RPi.GPIO as GPIO
import time
import threading
import sys

class Arduino(threading.Thread):
    def __init__(self, c, f):
        threading.Thread.__init__(self)
        self.ser = serial.Serial("/dev/ttyACM0",9600)  #change ACM number as found from ls /dev/tty/ACM*
        self.ser.baudrate=9600
        self.c = c
        self.f = f

    def run (self):

        while True:
            read_ser = self.ser.readline()
            self.c.ULTRASONIC_SENSOR = float(read_ser)
            self.f.ultrasonic_lcd.display(self.c.ULTRASONIC_SENSOR)

            #Safety prevention for collision
            if read_ser < 20 and self.c.SAFETY == False:
                self.c.SAFETY = True
                self.c.stop(safety)
                self.c.turn_red_led_on()

                while self.c.SAFETY == True:
                    read_ser = self.ser.readline()
                    self.c.ULTRASONIC_SENSOR = float(read_ser)
                    self.f.ultrasonic_lcd.display(self.c.ULTRASONIC_SENSOR)

                    if read_ser >= 20:
                        self.c.SAFETY = False
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
