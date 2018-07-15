import serial
import time
import sys
from PyQt4.QtCore import *

class Auto_Thread(QThread):
    def __init__(self, c):
        QThread.__init__(self)
        self.c = c
        self.thread_to_stop = False

    def __del__(self):
        self.wait()

    def run(self):

        #while thread allowed to work
        while self.thread_to_stop == False:

            self.c.forward()
            self.c.STATUS = 'FORWARD'

            if self.c.SAFETY == True:

                self.c.stop()
                self.c.STATUS = 'STOP'

                while self.c.SAFETY == True:

                    print('safety')

        self.c.stop()

    def finish_thread(self):
        self.thread_to_stop = True

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
