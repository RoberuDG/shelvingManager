# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\NewRoom.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from sqlite3 import Connection, Cursor
from PyQt5 import QtCore, QtGui, QtWidgets
from shelvingManager.Backend.Controller.database_controller import DatabaseController
from shelvingManager.Backend.Controller.room_controller import RoomController
from shelvingManager.Models.room import Room
import sys


class Ui_Dialog(object):

    MAX_DESCRIPTION_CHARACTERS = 255
    dbc = DatabaseController()
    rc = RoomController(dbc.conn)

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setEnabled(True)
        Dialog.resize(666, 293)
        Dialog.setLayoutDirection(QtCore.Qt.LeftToRight)
        Dialog.setAutoFillBackground(False)
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(80, 16, 521, 271))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.textName = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.textName.setMaxLength(20)
        self.textName.setCursorPosition(0)
        self.textName.setObjectName("textName")
        self.horizontalLayout.addWidget(self.textName)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.spinMeters1 = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.spinMeters1.setKeyboardTracking(False)
        self.spinMeters1.setProperty("showGroupSeparator", False)
        self.spinMeters1.setMinimum(1)
        self.spinMeters1.setMaximum(100)
        self.spinMeters1.setObjectName("spinMeters1")
        self.horizontalLayout_2.addWidget(self.spinMeters1)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.spinMeters2 = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.spinMeters2.setMinimum(1)
        self.spinMeters2.setMaximum(100)
        self.spinMeters2.setObjectName("spinMeters2")
        self.horizontalLayout_2.addWidget(self.spinMeters2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.etDescription = QtWidgets.QPlainTextEdit(self.verticalLayoutWidget)
        self.etDescription.setObjectName("etDescription")
        self.horizontalLayout_3.addWidget(self.etDescription)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setText("")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.verticalLayoutWidget)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Save)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.buttonBox.accepted.connect(self.create_room)
        self.verticalLayout.addWidget(self.buttonBox)
        self.etDescription.textChanged.connect(self.limit_text)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Crear nueva habitación"))
        self.label.setText(_translate("Dialog", "Nombre:"))
        self.textName.setPlaceholderText(_translate("Dialog", "Max. 20 caracteres"))
        self.label_2.setText(_translate("Dialog", "Tamaño:"))
        self.spinMeters1.setSuffix(_translate("Dialog", "m"))
        self.label_3.setText(_translate("Dialog", "x"))
        self.spinMeters2.setSuffix(_translate("Dialog", "m"))
        self.label_4.setText(_translate("Dialog", "Descripción:"))
        self.etDescription.setPlaceholderText(_translate("Dialog", "Max. 255 caracteres"))

    def limit_text(self):
        text = self.etDescription.toPlainText()
        if text is not None:
            if len(text) > self.MAX_DESCRIPTION_CHARACTERS:
                self.label_5.setText("<font color='red'>Max. 255 caracteres</font>")
                self.etDescription.setPlainText(text[:255])
            elif len(text) == self.MAX_DESCRIPTION_CHARACTERS - 1:
                self.label_5.setText("")

    def create_room(self):
        name = self.textName.text()
        size_x = self.spinMeters1.value()
        size_y = self.spinMeters2.value()
        description = self.etDescription.toPlainText()
        if name is not None and name != '' and size_x > 0 and size_y > 0:
            self.rc.insert_room(name, size_x, size_y, description)

    def room_window(self):
        Dialog = QtWidgets.QDialog()
        ui = Ui_Dialog()
        ui.setupUi(Dialog)
        Dialog.show()
        Dialog.exec_()
