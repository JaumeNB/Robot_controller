from PyQt4 import QtCore, QtGui
import sys, time, datetime
import socket
from threading import Thread


"""---------------------------------------------------------------------------------------------------"""
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(400, 300)
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSpacing(45)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.start_server_btn = QtGui.QPushButton(Form)
        self.start_server_btn.setObjectName(_fromUtf8("start_server_btn"))
        self.horizontalLayout.addWidget(self.start_server_btn)
        self.terminate_server_btn = QtGui.QPushButton(Form)
        self.terminate_server_btn.setObjectName(_fromUtf8("terminate_server_btn"))
        self.horizontalLayout.addWidget(self.terminate_server_btn)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "TCP Server", None))
        self.start_server_btn.setText(_translate("Form", "Start TCP Server", None))
        self.terminate_server_btn.setText(_translate("Form", "Terminate TCP Server", None))
        """---------------------------------------------------------------------------------------------------"""
        self.start_server_btn.clicked.connect(self.start_TCP_server)

    def start_TCP_server(self):
        host = ''
        port = 12345
        print ("TCP server listening to port " + str(port))
        print ("Waiting for clients...")

        s = socket.socket()
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        try:
            s.bind((host, port))
        except socket.error as e:
            print (str(e))

        s.listen(1)
        c, addr = s.accept()

        print("Connection from: " + str(addr))

        while True:

            try:
                data = c.recv(1024).decode('utf-8')
                if not data:
                    break
                print("\nData received: " + data + "at " + datetime.datetime.now().strftime("%H:%M:%S"))
                reply = "\nData transmited successfully: " + data + "at " + datetime.datetime.now().strftime("%H:%M:%S")
                c.send(reply.encode('utf-8'))

            except KeyboardInterrupt:
                print ("Server stopped due to KeyboardInterrupt")
                break

            except UnicodeDecodeError as e:
                print (str(e))
                break

        c.close()
        s.shutdown(2)
        s.close()


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
