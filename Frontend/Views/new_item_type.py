# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'NewItemType.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from shelvingManager.Backend.Controller.database_controller import DatabaseController
from shelvingManager.Backend.Controller.item_type_controller import ItemTypeController
from shelvingManager.Models.item_type import ItemType

class Ui_Dialog(object):

    MAX_DESCRIPTION_CHARACTERS = 255
    dbc = DatabaseController()
    it = ItemTypeController(dbc.conn)
    item_types = []

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(693, 369)
        self.item_types = self.it.get_all_item_types()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(90, 10, 521, 334))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(15)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_8 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_4.addWidget(self.label_8)
        self.textName_2 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.textName_2.setMaxLength(20)
        self.textName_2.setCursorPosition(0)
        self.textName_2.setAlignment(QtCore.Qt.AlignCenter)
        self.textName_2.setObjectName("textName_2")
        self.horizontalLayout_4.addWidget(self.textName_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_9 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_5.addWidget(self.label_9)
        self.spinMeters1_2 = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.spinMeters1_2.setKeyboardTracking(False)
        self.spinMeters1_2.setProperty("showGroupSeparator", False)
        self.spinMeters1_2.setMinimum(10)
        self.spinMeters1_2.setMaximum(100)
        self.spinMeters1_2.setSingleStep(10)
        self.spinMeters1_2.setObjectName("spinMeters1_2")
        self.horizontalLayout_5.addWidget(self.spinMeters1_2)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_13 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_6.addWidget(self.label_13)
        self.etDescription_2 = QtWidgets.QPlainTextEdit(self.verticalLayoutWidget)
        self.etDescription_2.setMaximumSize(QtCore.QSize(16777215, 100))
        self.etDescription_2.setObjectName("etDescription_2")
        self.horizontalLayout_6.addWidget(self.etDescription_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.label_14 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setText("")
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label_14.setObjectName("label_14")
        self.verticalLayout_2.addWidget(self.label_14)
        self.buttonBox_3 = QtWidgets.QDialogButtonBox(self.verticalLayoutWidget)
        self.buttonBox_3.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox_3.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Save)
        self.buttonBox_3.setCenterButtons(True)
        self.buttonBox_3.setObjectName("buttonBox_3")
        self.buttonBox_3.accepted.connect(Dialog.accept)
        self.buttonBox_3.rejected.connect(Dialog.reject)
        self.buttonBox_3.accepted.connect(self.create_item_type)
        self.textName_2.textChanged.connect(self.control_item_type_name)
        self.verticalLayout_2.addWidget(self.buttonBox_3)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_8.setText(_translate("Dialog", "Nombre:"))
        self.textName_2.setPlaceholderText(_translate("Dialog", "Max. 20 caracteres"))
        self.label_9.setText(_translate("Dialog", "Tamaño:"))
        self.spinMeters1_2.setSuffix(_translate("Dialog", "cm"))
        self.label_13.setText(_translate("Dialog", "Descripción:"))
        self.etDescription_2.setPlaceholderText(_translate("Dialog", "Max. 255 caracteres"))

    def create_item_type(self):
        name = self.textName_2.text()
        description = self.etDescription_2.toPlainText()
        size = self.spinMeters1_2.value()
        if name is not None and name != "" and size is not None and size > 0:
            item_type = ItemType(name, description, size)
            self.it.insert_item_type(item_type)

    def limit_text(self):
        text = self.etDescription_2.toPlainText()
        if text is not None:
            if len(text) > self.MAX_DESCRIPTION_CHARACTERS:
                self.label_14.setText(
                    "<font color='red'>Max. 255 caracteres</font>")
                self.etDescription_2.setPlainText(text[:255])
            elif len(text) == self.MAX_DESCRIPTION_CHARACTERS - 1:
                self.label_14.setText("")

    def control_item_type_name(self):
        for item_type in self.item_types:
            if item_type.name == self.textName_2.text():
                self.label_14.setText("<font color='red'>Nombre repetido</font>")
                self.buttonBox_3.setEnabled(False)
                return
            else:
                self.label_14.setText("")
                self.buttonBox_3.setEnabled(True)

    def item_type_window(self):
        Dialog = QtWidgets.QDialog()
        ui = Ui_Dialog()
        ui.setupUi(Dialog)
        Dialog.show()
        Dialog.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)
        Dialog.exec_()