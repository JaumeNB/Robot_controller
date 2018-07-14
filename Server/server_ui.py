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
        Form.resize(529, 381)
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout.addWidget(self.label_3)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSpacing(45)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.start_server_btn = QtGui.QPushButton(Form)
        self.start_server_btn.setObjectName(_fromUtf8("start_server_btn"))
        self.horizontalLayout.addWidget(self.start_server_btn)
        self.auto_btn = QtGui.QPushButton(Form)
        self.auto_btn.setObjectName(_fromUtf8("auto_btn"))
        self.horizontalLayout.addWidget(self.auto_btn)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
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
        self.red_label.setAlignment(QtCore.Qt.AlignCenter)
        self.red_label.setObjectName(_fromUtf8("red_label"))
        self.horizontalLayout_4.addWidget(self.red_label)
        self.green_label = QtGui.QLabel(Form)
        self.green_label.setAlignment(QtCore.Qt.AlignCenter)
        self.green_label.setObjectName(_fromUtf8("green_label"))
        self.horizontalLayout_4.addWidget(self.green_label)
        self.blue_label = QtGui.QLabel(Form)
        self.blue_label.setAlignment(QtCore.Qt.AlignCenter)
        self.blue_label.setObjectName(_fromUtf8("blue_label"))
        self.horizontalLayout_4.addWidget(self.blue_label)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.label = QtGui.QLabel(Form)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_4.addWidget(self.label)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.wheel_orientation_label = QtGui.QLabel(Form)
        self.wheel_orientation_label.setAlignment(QtCore.Qt.AlignCenter)
        self.wheel_orientation_label.setObjectName(_fromUtf8("wheel_orientation_label"))
        self.horizontalLayout_7.addWidget(self.wheel_orientation_label)
        self.verticalLayout_4.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.wheel_orientation_lcd = QtGui.QLCDNumber(Form)
        self.wheel_orientation_lcd.setObjectName(_fromUtf8("wheel_orientation_lcd"))
        self.horizontalLayout_2.addWidget(self.wheel_orientation_lcd)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3.addLayout(self.verticalLayout_4)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.ultrasonic_sensor_label = QtGui.QLabel(Form)
        self.ultrasonic_sensor_label.setAlignment(QtCore.Qt.AlignCenter)
        self.ultrasonic_sensor_label.setObjectName(_fromUtf8("ultrasonic_sensor_label"))
        self.verticalLayout_2.addWidget(self.ultrasonic_sensor_label)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.ultrasonic_orientation_label = QtGui.QLabel(Form)
        self.ultrasonic_orientation_label.setAlignment(QtCore.Qt.AlignCenter)
        self.ultrasonic_orientation_label.setObjectName(_fromUtf8("ultrasonic_orientation_label"))
        self.horizontalLayout_6.addWidget(self.ultrasonic_orientation_label)
        self.distance_label = QtGui.QLabel(Form)
        self.distance_label.setAlignment(QtCore.Qt.AlignCenter)
        self.distance_label.setObjectName(_fromUtf8("distance_label"))
        self.horizontalLayout_6.addWidget(self.distance_label)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.ultrasonic_orientation_lcd = QtGui.QLCDNumber(Form)
        self.ultrasonic_orientation_lcd.setObjectName(_fromUtf8("ultrasonic_orientation_lcd"))
        self.horizontalLayout_5.addWidget(self.ultrasonic_orientation_lcd)
        self.ultrasonic_distance_lcd = QtGui.QLCDNumber(Form)
        self.ultrasonic_distance_lcd.setObjectName(_fromUtf8("ultrasonic_distance_lcd"))
        self.horizontalLayout_5.addWidget(self.ultrasonic_distance_lcd)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "TCP Server", None))
        self.label_3.setText(_translate("Form", "CAR MODES", None))
        self.start_server_btn.setText(_translate("Form", "Controller mode", None))
        self.auto_btn.setText(_translate("Form", "Autonomous mode", None))
        self.label_2.setText(_translate("Form", "DASHBOARD", None))
        self.led_status_label.setText(_translate("Form", "Led Status", None))
        self.red_label.setText(_translate("Form", "RED", None))
        self.green_label.setText(_translate("Form", "GREEN", None))
        self.blue_label.setText(_translate("Form", "BLUE", None))
        self.label.setText(_translate("Form", "Car", None))
        self.wheel_orientation_label.setText(_translate("Form", "Wheels orientation", None))
        self.ultrasonic_sensor_label.setText(_translate("Form", "Ultrasonic sensor", None))
        self.ultrasonic_orientation_label.setText(_translate("Form", "Orientation", None))
        self.distance_label.setText(_translate("Form", "Distance", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

