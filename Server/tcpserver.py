import socket
import sys, time, datetime
import threading
from commands import Commands
from controller import Controller

c = Controller()

class TcpServer(threading.Thread):
    """ Simple socket server that listens to one single client. """

    def __init__(self, host = '0.0.0.0', port = 12345, buf_size = 1024):
        threading.Thread.__init__(self)
        """ Initialize the server with a host and port to listen to. """
        # Create a TCP/IP socket
        #AF_INET specifies the protocol family used for the communication.
        #In most cases, you will want to use AF_INET for IPv4 internet protocols
        #SOCK_STREAM is used for a TCP communication
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #setsockopt() is used to specify options on the socket.
        #Here, we set the option SO_REUSEADDR, which indicates that the system can reuse this socket
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        #if host is 127.0.0.1, limits connections to clients running on the local machine.
        #you can use 0.0.0.0, and it will be accessible from other machines on your local network.
        self.host = host
        #port that server will be listening to
        self.port = port
        self.buf_size = buf_size

    def close(self):
        """ Close the server socket. """
        if self.connection:
            print ("Found a connection, closing it")
            self.connection.close()
        if self.sock:
            print('Closing server socket (host {}, port {})'.format(self.host, self.port))
            self.sock.close()
            self.sock = None

    def run(self):
        """ Accept and handle an incoming connection. """
        try:
            #associate the socket with the server address and port
            self.sock.bind((self.host, self.port))
        except socket.error as e:
            print "Bind Error : ", e
        #puts the socket into server mode, The number you give to listen()
        #specifies how many connections can be queued for this socket
        self.sock.listen(1)

        print('Starting socket server (host {}, port {})'.format(self.host, self.port))

        while True:

            print("Wating for connection ... ")

            try:
                #accept waits for an incoming connection, returning the open connection between
                #the server and client and the address of the clientself
                #The connection is actually a different socket on another port (assigned by the kernel)
                self.connection, self.client_address = self.sock.accept()

                print('Client {} connected'.format(self.client_address))

            except Exception, e:

				print "sock closed! Error: ",e

				try:
					self.connection.close()

				except Exception, e:
					print "Client close Error",e

				self.sock.shutdown(2)
				self.sock.close()
				break

            while True:

                try:
                    data = self.connection.recv(self.buf_size).decode('utf-8')

                except Exception, e:
                    print e
                    self.connection.close()
                    break

                if not data:
                    break

                data_array = data.split(">")

                for data_command in data_array:

                    if data_command == "":

                        continue

                    if Commands.CMD_FORWARD[1:] in data_command:

                        print data_command + " at " + datetime.datetime.now().strftime("%H:%M:%S")

                        #set the direction in which motors will spin
                        c.writeBlock(c.MOTOR_LEFT_DIR,0)
                        c.writeBlock(c.MOTOR_RIGHT_DIR,0)
                        #increase power (PWM) supplied to the motor
                        for i in range(0,1000,10):
                            c.writeBlock(c.MOTOR_LEFT,i)
                            c.writeBlock(c.MOTOR_RIGHT,i)
                            time.sleep(0.005)

                    elif Commands.CMD_BACKWARD[1:] in data_command:

                        print data_command + " at " + datetime.datetime.now().strftime("%H:%M:%S")

                        #set the direction in which motors will spin
                        c.writeBlock(c.MOTOR_LEFT_DIR,1)
                        c.writeBlock(c.MOTOR_RIGHT_DIR,1)
                        #increase power (PWM) supplied to the motor
                        for i in range(0,1000,10):
                            c.writeBlock(c.MOTOR_LEFT,i)
                            c.writeBlock(c.MOTOR_RIGHT,i)
                            time.sleep(0.005)

                    elif Commands.CMD_STOP[1:] in data_command:

                        print data_command + " at " + datetime.datetime.now().strftime("%H:%M:%S")

                        c.writeBlock(c.MOTOR_LEFT,0)
                        c.writeBlock(c.MOTOR_RIGHT,0)

                    elif Commands.CMD_RGB_B[1:]  in data_command:
                        if c.Is_BLUE_LED_State_True is True:
                            c.Is_BLUE_LED_State_True = False
                            c.writeBlock(c.BLUE_LED,0)
                        elif c.Is_BLUE_LED_State_True is False:
                            c.Is_BLUE_LED_State_True = True
                            c.writeBlock(c.BLUE_LED,1)

                    elif Commands.CMD_RGB_R[1:]  in data_command:
                        if c.Is_RED_LED_State_True is True:
                            c.Is_RED_LED_State_True = False
                            c.writeBlock(c.RED_LED,0)
                        elif c.Is_RED_LED_State_True is False:
                            c.Is_RED_LED_State_True = True
                            c.writeBlock(c.RED_LED,1)

                    elif Commands.CMD_RGB_G[1:]  in data_command:
                        if c.Is_GREEN_LED_State_True is True:
                            c.Is_GREEN_LED_State_True = False
                            c.writeBlock(c.GREEN_LED,0)
                        elif c.Is_GREEN_LED_State_True is False:
                            c.Is_GREEN_LED_State_True = True
                            c.writeBlock(c.GREEN_LED,1)



def main():
    server = TcpServer()
    server.run()
    print 'Exiting'

if __name__ == "__main__":
    main()
