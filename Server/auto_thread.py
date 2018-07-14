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

        for i in range(2):

            self.c.turn_blue_led_on()
            time.sleep(1)
            self.c.turn_blue_led_on()
            time.sleep(1)


        """
        #Safety prevention for collision
        if read_ser < 30 and self.c.SAFETY == False:
            #safety stop triggered, safety boolean = true
            self.c.SAFETY = True
            #send a command stop
            self.c.stop(self.c.SAFETY)
            #turn red led on
            self.c.turn_red_led_on()
            #trigger buzzer
            self.c.buzzer_on()
            #emit signal to update UI
            self.emit( SIGNAL('update_led_label(QString, QString)'), "red", "background-color: red")

            while self.c.SAFETY == True:
                read_ser = self.ser.readline()

                try:
                    read_ser = int(read_ser)
                    self.c.ULTRASONIC_SENSOR = float(read_ser)
                    #emit signal to update UI
                    self.emit( SIGNAL('update_ultrasonic_distance_lcd(QString)'),str(self.c.ULTRASONIC_SENSOR))


                except ValueError as e:
                    print "error: " + read_ser

                if read_ser >= 30:
                    self.c.SAFETY = False
                    #turn off leds
                    self.c.turn_led_off()
                    #turn off buzzer
                    self.c.buzzer_off()
                    #emit signal to main thread (UI) that will trigger a function
                    #that will change the red led dashboard label
                    self.emit( SIGNAL('update_led_label(QString, QString)'), "red", "background-color: white")
                    print "No danger of collision"
        """

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
