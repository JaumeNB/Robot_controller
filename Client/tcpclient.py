import socket
import sys, time, datetime

class TcpClient():

    def __init__(self, host = '192.168.1.145', port = 12345, buf_size = 1024):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = host
        self.port = port
        self.buf_size = buf_size
        self.address = (self.host, self.port)

    def connect_to_server(self):
        self.sock.connect(self.address)

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
