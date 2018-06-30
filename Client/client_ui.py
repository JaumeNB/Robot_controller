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
        self.connect_btn = QtGui.QPushButton(Form)
        self.connect_btn.setObjectName(_fromUtf8("connect_btn"))
        self.verticalLayout_2.addWidget(self.connect_btn)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.red_btn = QtGui.QPushButton(Form)
        self.red_btn.setObjectName(_fromUtf8("red_btn"))
        self.horizontalLayout_2.addWidget(self.red_btn)
        self.green_btn = QtGui.QPushButton(Form)
        self.green_btn.setObjectName(_fromUtf8("green_btn"))
        self.horizontalLayout_2.addWidget(self.green_btn)
        self.blue_btn = QtGui.QPushButton(Form)
        self.blue_btn.setObjectName(_fromUtf8("blue_btn"))
        self.horizontalLayout_2.addWidget(self.blue_btn)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.forward_btn = QtGui.QPushButton(Form)
        self.forward_btn.setObjectName(_fromUtf8("forward_btn"))
        self.verticalLayout_2.addWidget(self.forward_btn)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.left_btn = QtGui.QPushButton(Form)
        self.left_btn.setObjectName(_fromUtf8("left_btn"))
        self.horizontalLayout.addWidget(self.left_btn)
        self.right_btn = QtGui.QPushButton(Form)
        self.right_btn.setObjectName(_fromUtf8("right_btn"))
        self.horizontalLayout.addWidget(self.right_btn)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.backwards_btn = QtGui.QPushButton(Form)
        self.backwards_btn.setObjectName(_fromUtf8("backwards_btn"))
        self.verticalLayout_2.addWidget(self.backwards_btn)
        self.verticalLayout.addLayout(self.verticalLayout_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "TCP Client", None))
        self.connect_btn.setText(_translate("Form", "Start TCP Client", None))
        self.red_btn.setText(_translate("Form", "Red LED", None))
        self.green_btn.setText(_translate("Form", "Green Led", None))
        self.blue_btn.setText(_translate("Form", "Blue LED", None))
        self.forward_btn.setText(_translate("Form", "Forward", None))
        self.left_btn.setText(_translate("Form", "Left", None))
        self.right_btn.setText(_translate("Form", "Right", None))
        self.backwards_btn.setText(_translate("Form", "Go Backwards", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

