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
        self.forward_btn = QtGui.QPushButton(Form)
        self.forward_btn.setObjectName(_fromUtf8("forward_btn"))
        self.verticalLayout_2.addWidget(self.forward_btn)
        self.backward_btn = QtGui.QPushButton(Form)
        self.backward_btn.setObjectName(_fromUtf8("backward_btn"))
        self.verticalLayout_2.addWidget(self.backward_btn)
        self.verticalLayout.addLayout(self.verticalLayout_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "TCP Client", None))
        self.connect_btn.setText(_translate("Form", "Start TCP Client", None))
        self.forward_btn.setText(_translate("Form", "Go Forward", None))
        self.backward_btn.setText(_translate("Form", "Go Backward", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
