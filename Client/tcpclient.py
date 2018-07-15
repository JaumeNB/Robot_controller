import socket
import sys, time, datetime

class TcpClient():

    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = '192.168.1.145'
        self.port = 12345
        self.buf_size = 1024
        self.address = (self.host, self.port)

    def connect(self):
        self.sock.connect(self.address)

    def disconnect(self):
        self.sock.close()

    def send_data(self, data):
        try:
            self.sock.send(data.encode('utf-8'))
        except Exception, e:
            print Exception, "Send TCP Data error:", e

def main():
    client = TcpClient()
    client.run()
    print 'Exiting'

if __name__ == "__main__":
    main()
