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
        Form.resize(407, 300)
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.start_server_btn = QtGui.QPushButton(Form)
        self.start_server_btn.setObjectName(_fromUtf8("start_server_btn"))
        self.horizontalLayout_2.addWidget(self.start_server_btn)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.led_status_label = QtGui.QLabel(Form)
        self.led_status_label.setAlignment(QtCore.Qt.AlignCenter)
        self.led_status_label.setObjectName(_fromUtf8("led_status_label"))
        self.verticalLayout_3.addWidget(self.led_status_label)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.red_label = QtGui.QLabel(Form)
        self.red_label.setObjectName(_fromUtf8("red_label"))
        self.horizontalLayout_4.addWidget(self.red_label)
        self.green_label = QtGui.QLabel(Form)
        self.green_label.setObjectName(_fromUtf8("green_label"))
        self.horizontalLayout_4.addWidget(self.green_label)
        self.blue_label = QtGui.QLabel(Form)
        self.blue_label.setObjectName(_fromUtf8("blue_label"))
        self.horizontalLayout_4.addWidget(self.blue_label)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.ultrasonic_sensor_label = QtGui.QLabel(Form)
        self.ultrasonic_sensor_label.setAlignment(QtCore.Qt.AlignCenter)
        self.ultrasonic_sensor_label.setObjectName(_fromUtf8("ultrasonic_sensor_label"))
        self.verticalLayout_2.addWidget(self.ultrasonic_sensor_label)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.orientation_label = QtGui.QLabel(Form)
        self.orientation_label.setObjectName(_fromUtf8("orientation_label"))
        self.horizontalLayout_6.addWidget(self.orientation_label)
        self.distance_label = QtGui.QLabel(Form)
        self.distance_label.setObjectName(_fromUtf8("distance_label"))
        self.horizontalLayout_6.addWidget(self.distance_label)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.orientation_lcd = QtGui.QLCDNumber(Form)
        self.orientation_lcd.setObjectName(_fromUtf8("orientation_lcd"))
        self.horizontalLayout_5.addWidget(self.orientation_lcd)
        self.distance_lcd = QtGui.QLCDNumber(Form)
        self.distance_lcd.setObjectName(_fromUtf8("distance_lcd"))
        self.horizontalLayout_5.addWidget(self.distance_lcd)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSpacing(45)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.arduino_btn = QtGui.QPushButton(Form)
        self.arduino_btn.setObjectName(_fromUtf8("arduino_btn"))
        self.horizontalLayout.addWidget(self.arduino_btn)
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "TCP Server", None))
        self.start_server_btn.setText(_translate("Form", "Start TCP Server Thread", None))
        self.led_status_label.setText(_translate("Form", "Led Status", None))
        self.red_label.setText(_translate("Form", "RED", None))
        self.green_label.setText(_translate("Form", "GREEN", None))
        self.blue_label.setText(_translate("Form", "BLUE", None))
        self.ultrasonic_sensor_label.setText(_translate("Form", "Ultrasonic sensor", None))
        self.orientation_label.setText(_translate("Form", "Orientation (degrees)", None))
        self.distance_label.setText(_translate("Form", "Distance (mm)", None))
        self.arduino_btn.setText(_translate("Form", "Start-up Arduino", None))
        self.pushButton.setText(_translate("Form", "Autonomous mode", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

