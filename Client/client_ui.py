# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'client_GUI.ui'
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
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem)
        self.connect_btn = QtGui.QPushButton(Form)
        self.connect_btn.setObjectName(_fromUtf8("connect_btn"))
        self.horizontalLayout_7.addWidget(self.connect_btn)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.red_btn = QtGui.QPushButton(Form)
        self.red_btn.setObjectName(_fromUtf8("red_btn"))
        self.horizontalLayout_2.addWidget(self.red_btn)
        self.green_btn = QtGui.QPushButton(Form)
        self.green_btn.setObjectName(_fromUtf8("green_btn"))
        self.horizontalLayout_2.addWidget(self.green_btn)
        self.blue_btn = QtGui.QPushButton(Form)
        self.blue_btn.setObjectName(_fromUtf8("blue_btn"))
        self.horizontalLayout_2.addWidget(self.blue_btn)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.label = QtGui.QLabel(Form)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_5.addWidget(self.label)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem4)
        self.forward_btn = QtGui.QPushButton(Form)
        self.forward_btn.setObjectName(_fromUtf8("forward_btn"))
        self.horizontalLayout_4.addWidget(self.forward_btn)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem5)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem6)
        self.left_btn = QtGui.QPushButton(Form)
        self.left_btn.setObjectName(_fromUtf8("left_btn"))
        self.horizontalLayout.addWidget(self.left_btn)
        self.right_btn = QtGui.QPushButton(Form)
        self.right_btn.setObjectName(_fromUtf8("right_btn"))
        self.horizontalLayout.addWidget(self.right_btn)
        spacerItem7 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem7)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        spacerItem8 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem8)
        self.backwards_btn = QtGui.QPushButton(Form)
        self.backwards_btn.setObjectName(_fromUtf8("backwards_btn"))
        self.horizontalLayout_3.addWidget(self.backwards_btn)
        spacerItem9 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem9)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_2.addWidget(self.label_2)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        spacerItem10 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem10)
        self.ultrasonic_left_btn = QtGui.QPushButton(Form)
        self.ultrasonic_left_btn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.ultrasonic_left_btn.setObjectName(_fromUtf8("ultrasonic_left_btn"))
        self.horizontalLayout_6.addWidget(self.ultrasonic_left_btn)
        self.ultrasonic_right_btn = QtGui.QPushButton(Form)
        self.ultrasonic_right_btn.setObjectName(_fromUtf8("ultrasonic_right_btn"))
        self.horizontalLayout_6.addWidget(self.ultrasonic_right_btn)
        spacerItem11 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem11)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.verticalLayout.addLayout(self.verticalLayout_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "TCP Client", None))
        self.connect_btn.setText(_translate("Form", "Connect", None))
        self.red_btn.setText(_translate("Form", "Red LED", None))
        self.green_btn.setText(_translate("Form", "Green Led", None))
        self.blue_btn.setText(_translate("Form", "Blue LED", None))
        self.label.setText(_translate("Form", "Car controller", None))
        self.forward_btn.setText(_translate("Form", "Forward", None))
        self.left_btn.setText(_translate("Form", "Left", None))
        self.right_btn.setText(_translate("Form", "Right", None))
        self.backwards_btn.setText(_translate("Form", "Go Backwards", None))
        self.label_2.setText(_translate("Form", "Ultrasonic sensor controller", None))
        self.ultrasonic_left_btn.setText(_translate("Form", "Left", None))
        self.ultrasonic_right_btn.setText(_translate("Form", "Right", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

