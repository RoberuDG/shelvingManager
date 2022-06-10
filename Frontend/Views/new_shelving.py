# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'NewShelving.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    MAX_DESCRIPTION_CHARACTERS = 255

    def setupUi(self, Dialog, tableWidget, room_id):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1284, 590)
        Dialog.setInputMethodHints(QtCore.Qt.ImhFormattedNumbersOnly)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(40, 10, 1201, 541))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_2.setSpacing(15)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(50, 0))
        self.label.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.textName = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textName.sizePolicy().hasHeightForWidth())
        self.textName.setSizePolicy(sizePolicy)
        self.textName.setMaximumSize(QtCore.QSize(150, 16777215))
        self.textName.setInputMethodHints(QtCore.Qt.ImhNone)
        self.textName.setMaxLength(3)
        self.textName.setCursorPosition(0)
        self.textName.setObjectName("textName")
        self.horizontalLayout.addWidget(self.textName)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_2.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.label_6 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_6.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_2.addWidget(self.label_6)
        self.spinMeters1 = QtWidgets.QSpinBox(self.horizontalLayoutWidget)
        self.spinMeters1.setKeyboardTracking(False)
        self.spinMeters1.setProperty("showGroupSeparator", False)
        self.spinMeters1.setMinimum(2)
        self.spinMeters1.setMaximum(100)
        self.spinMeters1.setObjectName("spinMeters1")
        self.horizontalLayout_2.addWidget(self.spinMeters1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.etDescription = QtWidgets.QPlainTextEdit(self.horizontalLayoutWidget)
        self.etDescription.setMaximumSize(QtCore.QSize(16777215, 100))
        self.etDescription.setObjectName("etDescription")
        self.horizontalLayout_3.addWidget(self.etDescription)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.label_5 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setText("")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.line = QtWidgets.QFrame(self.horizontalLayoutWidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_2.addWidget(self.line)
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.radioButton_2 = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.radioButton_2.setObjectName("radioButton_2")
        self.horizontalLayout_10.addWidget(self.radioButton_2)
        self.radioButton = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.radioButton.setObjectName("radioButton")
        self.horizontalLayout_10.addWidget(self.radioButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_9 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_12.addWidget(self.label_9)
        self.spinBox_3 = QtWidgets.QSpinBox(self.horizontalLayoutWidget)
        self.spinBox_3.setObjectName("spinBox_3")
        self.horizontalLayout_12.addWidget(self.spinBox_3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_7 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_9.addWidget(self.label_7)
        self.spinBox_2 = QtWidgets.QSpinBox(self.horizontalLayoutWidget)
        self.spinBox_2.setObjectName("spinBox_2")
        self.horizontalLayout_9.addWidget(self.spinBox_2)
        self.label_8 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_9.addWidget(self.label_8)
        self.spinBox = QtWidgets.QSpinBox(self.horizontalLayoutWidget)
        self.spinBox.setObjectName("spinBox")
        self.horizontalLayout_9.addWidget(self.spinBox)
        self.verticalLayout_2.addLayout(self.horizontalLayout_9)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.horizontalLayoutWidget)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Save)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_2.addWidget(self.buttonBox)
        self.horizontalLayout_4.addLayout(self.verticalLayout_2)
        spacerItem3 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.tableWidget = QtWidgets.QTableWidget(self.horizontalLayoutWidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(tableWidget.columnCount())
        self.tableWidget.setRowCount(tableWidget.rowCount())
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        h_header = self.tableWidget.horizontalHeader()
        h_header.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        v_header = self.tableWidget.verticalHeader()
        v_header.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.horizontalLayout_4.addWidget(self.tableWidget)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Código:"))
        self.textName.setPlaceholderText(_translate("Dialog", "Max. 3 caracteres"))
        self.label_2.setText(_translate("Dialog", "Tamaño:"))
        self.label_6.setText(_translate("Dialog", "Largo"))
        self.spinMeters1.setSuffix(_translate("Dialog", "m"))
        self.label_4.setText(_translate("Dialog", "Descripción:"))
        self.etDescription.setPlaceholderText(_translate("Dialog", "Max. 255 caracteres"))
        self.label_3.setText(_translate("Dialog", "Posición"))
        self.radioButton_2.setText(_translate("Dialog", "Horizontal"))
        self.radioButton.setText(_translate("Dialog", "Vertical"))
        self.label_9.setText(_translate("Dialog", "Fila / Columna"))
        self.label_7.setText(_translate("Dialog", "Inicio"))
        self.label_8.setText(_translate("Dialog", "Fin"))


    def limit_text(self):
            text = self.etDescription.toPlainText()
            if text is not None:
                if len(text) > self.MAX_DESCRIPTION_CHARACTERS:
                    self.label_5.setText("<font color='red'>Max. 255 caracteres</font>")
                    self.etDescription.setPlainText(text[:255])
                elif len(text) == self.MAX_DESCRIPTION_CHARACTERS - 1:
                    self.label_5.setText("")

    def create_shelf(self):
        name = self.textName.text()
        size_y = self.spinMeters1.value()
        description = self.etDescription.toPlainText()
        if name is not None and name != '' and size_y > 0:
            self.name = name
            self.size_y = size_y
            self.description = description
        return self.name, self.size_y, self.description

    def shelving_window(self, tableWidget, room_id):
        Dialog = QtWidgets.QDialog()
        ui = Ui_Dialog()
        ui.setupUi(Dialog, tableWidget, room_id)
        ui.tableWidget = tableWidget
        Dialog.show()
        Dialog.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)
        Dialog.exec_()