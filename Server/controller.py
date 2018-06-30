import smbus
import time
import sys

"""----------------------CLASS CONTROLLER---------------------------"""

class Controller:

    """CLASS ATTRIBUTES"""
    #COMMANDS
    SERVO_1 = 0                         #SERVO 1
    SERVO_2 = 1                         #SERVO 2
    SERVO_3 = 2                         #SERVO 3
    MOTOR_LEFT = 4                      #LEFT WHEEL MOTOR POWER
    MOTOR_RIGHT = 5                     #RIGHT WHEEL MOTOR POWER
    MOTOR_LEFT_DIR = 6                  #LEFT MOTOR DIRECTION
    MOTOR_RIGHT_DIR = 7                 #RIGHT MOTOR DIRECTION
    BUZZER = 8                          #BUZZER
    RED_LED = 9                         #RED LED
    BLUE_LED = 10                       #BLUE LED
    GREEN_LED = 11                      #GREEN LED
    #STATE
    CURRENT_DIRECTION = 0               #TILT OF DIRECTION ON BOTH WHEELS

    """CLASS CONSTRUCTOR"""
    def __init__(self):
        self.address = 0x18             #address of the I2C device
	self.bus=smbus.SMBus(1)             #initialize bus

    """INSTANCE METHODS"""
    def writeBlock(self,command,data):  #writes data in blocks up to 16 bytes per block
        try:
            #data sent to address, first byte of data is a command. Other bytes are transformed for correct data processing
            self.bus.write_i2c_block_data(self.address,command,[data>>8,data&0xff])
	    time.sleep(0.001)
        except Exception,e:
	    print Exception,"I2C Error :",e

    #TURNS DIRECTION TO THE RIGHT
    def turn_right(self):
        #increase direction tilt towards right
        self.CURRENT_DIRECTION += 10
        #set the direction in which motors will spin
        self.writeBlock(self.SERVO_1,self.numMap(self.CURRENT_DIRECTION,0,180,500,2500))
    #TURNS LED OFF
    def turn_led_off(self):
        #turn OFF red led
        self.writeBlock(self.RED_LED, 1)
        #turn OFF blue led
        self.writeBlock(self.BLUE_LED, 1)
        #turn OFF green led
        self.writeBlock(self.GREEN_LED, 1)

    #TURNS RED LED ON AND TURNS OFF OTHERS
    def turn_red_led_on(self):
        #turn ON red led
        self.writeBlock(self.RED_LED, 0)
        #turn OFF blue led
        self.writeBlock(self.BLUE_LED, 1)
        #turn OFF green led
        self.writeBlock(self.GREEN_LED, 1)

    #TURNS GREEN LED ON AND TURNS OFF OTHERS
    def turn_green_led_on(self):
        #turn OFF red led
        self.writeBlock(self.RED_LED, 1)
        #turn OFF blue led
        self.writeBlock(self.BLUE_LED, 1)
        #turn ON green led
        self.writeBlock(self.GREEN_LED, 0)

    #TURNS BLUE LED ON AND TURNS OFF OTHERS
    def turn_blue_led_on(self):
        #turn OFF red led
        self.writeBlock(self.RED_LED, 1)
        #turn ON blue led
        self.writeBlock(self.BLUE_LED, 0)
        #turn OFF green led
        self.writeBlock(self.GREEN_LED, 1)

    """STATIC METHODS"""
    @staticmethod
    #MAPS VALUE FROM ONE RANGE TO ANOTHER RANGE
    def numMap(value,fromLow,fromHigh,toLow,toHigh):
        #map a value from a range to another range
        return (toHigh-toLow)*(value-fromLow) / (fromHigh-fromLow) + toLow

"""----------------------FUNCTIONS---------------------------"""

def blink(controller, led):
    #blink the RGB LED Module for testing, blinks the choosen color
    command = getattr(controller, led)
    for i in range(0, 10):
        controller.writeBlock(command, 0)
        time.sleep(0.2)
        controller.writeBlock(command, 1)
        time.sleep(0.2)

def numMap(value,fromLow,fromHigh,toLow,toHigh):
    #map a value from a range to another range
    return (toHigh-toLow)*(value-fromLow) / (fromHigh-fromLow) + toLow

def rotate_servo(controller, servo):
    #rotate the servo back and forth
    center_angle = 90
    command = getattr(controller, servo)
    if servo == "SERVO_3":
        #SERVO 3 to start on 90 degrees otherwise it collides
        start_angle = 90
        end_angle = 180
    elif servo == "SERVO_2":
        #SERVO 2 can move freely from 15 to 180, no collision
        start_angle = 15
        end_angle = 180
    else:
        start_angle = 50
        end_angle = 140

    for i in range(center_angle,start_angle,-1):
        controller.writeBlock(command,numMap(i,0,180,500,2500))
        time.sleep(0.005)
    for i in range(start_angle,end_angle,1):
        controller.writeBlock(command,numMap(i,0,180,500,2500))
        time.sleep(0.005)
    for i in range(end_angle,center_angle,-1):
        controller.writeBlock(command,numMap(i,0,180,500,2500))
        time.sleep(0.005)




"""----------------------MAIN PROGRAM---------------------------"""

if __name__ == '__main__':

    #Create an instance of the class controller
    c = controller()
    #sys.argv allows to execute python scripts with arguments (e.g. python control.py RED_LED)
    try:

        #test the leds
        if sys.argv[1] == "RED_LED" or sys.argv[1] == "GREEN_LED" or sys.argv[1] == "BLUE_LED":
            blink(c,sys.argv[1])

        #turns off the LED
        if sys.argv[1] == "LED_OFF":
            c.writeBlock(c.RED_LED,1)
            c.writeBlock(c.GREEN_LED,1)
            c.writeBlock(c.BLUE_LED,1)

        #test the servos
        if sys.argv[1] == "SERVO_1" or sys.argv[1] == "SERVO_2" or sys.argv[1] == "SERVO_3":
            rotate_servo(c, sys.argv[1])
        if sys.argv[1] == "SERVO_1_CENTER" or sys.argv[1] == "SERVO_2_CENTER" or sys.argv[1] == "SERVO_3_CENTER":
            servo = sys.argv[1].split("_")
            command = getattr(c, servo[0] + "_" + servo[1])
            c.writeBlock(command,numMap(90,0,180,500,2500))

        #testing the buzzer
        if sys.argv[1] == "BUZZER":
	    c.writeBlock(c.BUZZER,500)
	    time.sleep(1)
	    c.writeBlock(c.BUZZER,0)

	#testing the motors
	if sys.argv[1] == "MOTOR_RIGHT" or sys.argv[1] == "MOTOR_LEFT":
            #get the power command for the motor (left or right)
            power_command = getattr(controller, sys.argv[1])
            #go backward (0) and forward (1)
            for x in range (0,2):
                #get the direction command for the motor (left or right)
                direction_command = getattr(controller, sys.argv[1] + "_DIR")
                #set the direction in which motor will spin
                c.writeBlock(direction_command,x)
                #increase power (PWM) supplied to the motor
                for i in range(0,1000,10):
                    c.writeBlock(power_command,i)
                    time.sleep(0.005)
                time.sleep(1)
                #decrease power (PWM) supplied to the motor
                for i in range(1000,0,-10):
                    c.writeBlock(power_command,i)
                    time.sleep(0.005)

    except KeyboardInterrupt:
        print 'Interrupted'
        sys.exit(0)
