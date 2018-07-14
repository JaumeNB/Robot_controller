import serial
import time
import sys
from PyQt4.QtCore import *

class Auto_Thread(QThread):
    def __init__(self, c):
        QThread.__init__(self)
        self.c = c
        self.status = "stop"

    def __del__(self):
        self.wait()

    def run(self):

        while True:

            if self.status == "stop":
                self.c.forward()
                self.status = "forward"

            if self.c.SAFETY and self.status == "forward":
                self.c.stop(self.c.SAFETY)
                break

def Main():
    auto = Auto_Thread()
    auto.run()
    print 'Exiting'

if __name__ == '__main__':
    try:
        Main()
    except KeyboardInterrupt:
        print 'Interrupted'
        sys.exit(0)
