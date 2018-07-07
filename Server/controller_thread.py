import serial
import time
import threading
import sys
from PyQt4.QtCore import *

#inhering from QThread instead of threading thread (python thread)
#because this thread needs to modify main thread (UI), and therefore
#PyQt threads (QThreads) are mandatory to use
class Controller_Thread(QThread):
    def __init__(self, c):
        QThread.__init__(self)
        self.c = c

    def __del__(self):
        self.wait()

    def run(self):

        while True:

            try:
                #emit signal to update UI
                self.emit( SIGNAL('update_orientation_lcd(QString)'),str(self.c.ULTRASONIC_ORIENTATION))

def Main():
    controller_thread = Controller_Thread()
    controller_thread.run()
    print 'Exiting'

if __name__ == '__main__':
    try:
        Main()
    except KeyboardInterrupt:
        print 'Interrupted'
        sys.exit(0)
