# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'server_GUI.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.thread_btn = QtGui.QPushButton(Form)
        self.thread_btn.setObjectName(_fromUtf8("thread_btn"))
        self.horizontalLayout_2.addWidget(self.thread_btn)
        self.threads_text = QtGui.QLabel(Form)
        self.threads_text.setObjectName(_fromUtf8("threads_text"))
        self.horizontalLayout_2.addWidget(self.threads_text)
        self.threads_lcd = QtGui.QLCDNumber(Form)
        self.threads_lcd.setObjectName(_fromUtf8("threads_lcd"))
        self.horizontalLayout_2.addWidget(self.threads_lcd)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_3.addWidget(self.label_2)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_4 = QtGui.QLabel(Form)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_4.addWidget(self.label_4)
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_4.addWidget(self.label_3)
        self.label_5 = QtGui.QLabel(Form)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_4.addWidget(self.label_5)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label = QtGui.QLabel(Form)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_2.addWidget(self.label)
        self.ultrasonic_lcd = QtGui.QLCDNumber(Form)
        self.ultrasonic_lcd.setObjectName(_fromUtf8("ultrasonic_lcd"))
        self.verticalLayout_2.addWidget(self.ultrasonic_lcd)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSpacing(45)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.start_server_btn = QtGui.QPushButton(Form)
        self.start_server_btn.setObjectName(_fromUtf8("start_server_btn"))
        self.horizontalLayout.addWidget(self.start_server_btn)
        self.arduino_btn = QtGui.QPushButton(Form)
        self.arduino_btn.setObjectName(_fromUtf8("arduino_btn"))
        self.horizontalLayout.addWidget(self.arduino_btn)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "TCP Server", None))
        self.thread_btn.setText(_translate("Form", "See active threads", None))
        self.threads_text.setText(_translate("Form", "TextLabel", None))
        self.label_2.setText(_translate("Form", "Led Status", None))
        self.label_4.setText(_translate("Form", "RED", None))
        self.label_3.setText(_translate("Form", "GREEN", None))
        self.label_5.setText(_translate("Form", "BLUE", None))
        self.label.setText(_translate("Form", "Ultrasonic sensor", None))
        self.start_server_btn.setText(_translate("Form", "Start TCP Server Thread", None))
        self.arduino_btn.setText(_translate("Form", "Start Arduino Thread", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

