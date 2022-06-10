# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Main.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

from shelvingManager.Backend.Controller.database_controller import DatabaseController
from shelvingManager.Backend.Controller.item_controller import ItemController
from shelvingManager.Backend.Controller.item_type_controller import ItemTypeController
from shelvingManager.Backend.Controller.room_controller import RoomController
from shelvingManager.Backend.Controller.shelving_controller import ShelvingController
from shelvingManager.Backend.Controller.shelf_controller import ShelfController
from shelvingManager.Models.room import Room
from shelvingManager.Models.shelf import Shelf
from shelvingManager.Models.shelving import Shelving


class Ui_MainWindow(object):

    dbc = DatabaseController()
    conn = dbc.connect_to_database()
    rc = RoomController(conn)
    sc = ShelvingController(conn)
    sfc = ShelfController(conn)
    ic = ItemController(conn)
    itc = ItemTypeController(conn)
    rooms = rc.get_all_rooms()
    shelvings = []
    shelves = []
    items = []
    item_types = []
    selected_room = None
    selected_shelf = None
    selected_shelving = None
    selected_item = None

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1024, 768)
        MainWindow.setMaximumSize(QtCore.QSize(1920, 1080))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMaximumSize(QtCore.QSize(1920, 1080))
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.itemsWidget = QtWidgets.QTreeWidget(self.centralwidget)
        self.itemsWidget.setMaximumSize(QtCore.QSize(500, 16777215))
        self.itemsWidget.setObjectName("itemsWidget")
        self.itemsWidget.itemDoubleClicked.connect(self.draw)
        self.itemsWidget.itemDoubleClicked.connect(self.controll_buttons)
        self.horizontalLayout.addWidget(self.itemsWidget)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.horizontalLayout.addWidget(self.tableWidget)
        self.line = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.line.sizePolicy().hasHeightForWidth())
        self.line.setSizePolicy(sizePolicy)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout.addWidget(self.line)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1447, 21))
        self.menubar.setObjectName("menubar")
        self.menuEditar = QtWidgets.QMenu(self.menubar)
        self.menuEditar.setObjectName("menuEditar")
        self.menuRoom = QtWidgets.QMenu(self.menuEditar)
        self.menuRoom.setEnabled(True)
        self.menuRoom.setObjectName("menuRoom")
        self.menuShelving = QtWidgets.QMenu(self.menuEditar)
        self.menuShelving.setEnabled(False)
        self.menuShelving.setObjectName("menuShelving")
        self.menuShelf = QtWidgets.QMenu(self.menuEditar)
        self.menuShelf.setEnabled(False)
        self.menuShelf.setObjectName("menuShelf")
        self.menuObjectTypes = QtWidgets.QMenu(self.menubar)
        self.menuObjectTypes.setObjectName("menuObjectTypes")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNewRoom = QtWidgets.QAction(MainWindow)
        self.actionNewRoom.setObjectName("actionNewRoom")
        self.actionNewRoom.triggered.connect(self.new_room_window)
        self.actionDeleteRoom = QtWidgets.QAction(MainWindow)
        self.actionDeleteRoom.setObjectName("actionDeleteRoom")
        self.actionDeleteRoom.setEnabled(False)
        self.actionEditRoom = QtWidgets.QAction(MainWindow)
        self.actionEditRoom.setObjectName("actionEditRoom")
        self.actionEditRoom.setEnabled(False)
        self.actionCreateShelving = QtWidgets.QAction(MainWindow)
        self.actionCreateShelving.setObjectName("actionCreateShelving")
        self.actionCreateShelving.triggered.connect(self.new_shelving_window)
        self.actionEditShelving = QtWidgets.QAction(MainWindow)
        self.actionEditShelving.setObjectName("actionEditShelving")
        self.actionRemoveShelving = QtWidgets.QAction(MainWindow)
        self.actionRemoveShelving.setObjectName(
            "actionRemoveShelving")
        self.actionAddShelf = QtWidgets.QAction(MainWindow)
        self.actionAddShelf.setObjectName("actionAddShelf")
        self.actionRemoveShelf = QtWidgets.QAction(MainWindow)
        self.actionRemoveShelf.setObjectName("actionRemoveShelf")
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.actionVer = QtWidgets.QAction(MainWindow)
        self.actionVer.setObjectName("actionVer")
        self.actionCrear = QtWidgets.QAction(MainWindow)
        self.actionCrear.setObjectName("actionCrear")
        self.menuRoom.addAction(self.actionNewRoom)
        self.menuRoom.addAction(self.actionEditRoom)
        self.menuRoom.addSeparator()
        self.menuRoom.addAction(self.actionDeleteRoom)
        self.menuShelving.addAction(self.actionCreateShelving)
        self.menuShelving.addAction(self.actionEditShelving)
        self.menuShelving.addSeparator()
        self.menuShelving.addAction(self.actionRemoveShelving)
        self.menuShelf.addAction(self.actionAddShelf)
        self.menuShelf.addSeparator()
        self.menuShelf.addAction(self.actionRemoveShelf)
        self.menuEditar.addAction(self.menuRoom.menuAction())
        self.menuEditar.addAction(self.menuShelving.menuAction())
        self.menuEditar.addAction(self.menuShelf.menuAction())
        self.menuObjectTypes.addAction(self.actionVer)
        self.menuObjectTypes.addAction(self.actionCrear)
        self.menubar.addAction(self.menuEditar.menuAction())
        self.menubar.addAction(self.menuObjectTypes.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.itemsWidget.headerItem().setText(
            0, _translate("MainWindow", "Habitaciones"))
        self.itemsWidget.headerItem().setText(1, _translate("MainWindow", "Estanterías"))
        self.itemsWidget.headerItem().setText(2, _translate("MainWindow", "Baldas"))
        self.itemsWidget.headerItem().setText(3, _translate("MainWindow", "Objetos"))
        self.menuEditar.setTitle(_translate("MainWindow", "Entidades"))
        self.menuRoom.setTitle(_translate("MainWindow", "Habitación"))
        self.menuShelving.setTitle(_translate("MainWindow", "Estantería"))
        self.menuShelf.setTitle(_translate("MainWindow", "Balda"))
        self.menuObjectTypes.setTitle(
            _translate("MainWindow", "Tipos de objeto"))
        self.actionNewRoom.setText(_translate(
            "MainWindow", "Crear nueva habitación"))
        self.actionDeleteRoom.setText(_translate(
            "MainWindow", "Eliminar habitación"))
        self.actionEditRoom.setText(_translate(
            "MainWindow", "Editar habitación"))
        self.actionCreateShelving.setText(
            _translate("MainWindow", "Añadir estantería"))
        self.actionEditShelving.setText(
            _translate("MainWindow", "Editar estantería"))
        self.actionRemoveShelving.setText(
            _translate("MainWindow", "Eliminar estantería"))
        self.actionAddShelf.setText(
            _translate("MainWindow", "Añadir balda"))
        self.actionRemoveShelf.setText(
            _translate("MainWindow", "Eliminar balda"))
        self.action.setText(_translate("MainWindow", "Tipos de objetos"))
        self.actionVer.setText(_translate("MainWindow", "Ver"))
        self.actionCrear.setText(_translate("MainWindow", "Crear"))

 # *Método para cargar la vista de árbol de los objetos

    def populate_templates(self):
        for room in self.rooms:
            child = QtWidgets.QTreeWidgetItem(self.itemsWidget)
            child.setText(0, room.name)
            child.setData(0, QtCore.Qt.UserRole, room)
            self.itemsWidget.addTopLevelItem(child)
            shelvings = self.sc.get_shelvings_by_room_id(room.id)
            for shelving in shelvings:
                self.shelvings.append(shelving)
                child2 = QtWidgets.QTreeWidgetItem(child)
                child2.setText(1, shelving.code)
                child2.setData(1, QtCore.Qt.UserRole, shelving)
                child.addChild(child2)
                shelves = self.sfc.get_shelf_by_shelving_id(
                    shelving.id)
                for shelf in shelves:
                    self.shelvings.append(shelf)
                    child3 = QtWidgets.QTreeWidgetItem(child2)
                    child3.setText(2, shelf.code)
                    child2.addChild(child3)
                    items = self.ic.get_items_by_shelf_id(
                        shelf.id)
                    for item in items:
                        self.items.append(item)
                        child4 = QtWidgets.QTreeWidgetItem(child3)
                        child4.setText(3, item.name)
                        child3.addChild(child4)

    def new_room_window(self):
        from new_room import Ui_Dialog as NewRoomDialog
        NewRoomDialog.room_window(self)
        self.itemsWidget.clear()
        self.rooms = self.rc.get_all_rooms()
        self.populate_templates()

    def new_shelving_window(self):
        from new_shelving import Ui_Dialog as NewShelvingDialog
        NewShelvingDialog.shelving_window(self, self.tableWidget, self.selected_room.id)
        #TODO: Método para crear estantería
        self.itemsWidget.clear()
        self.populate_templates()

    def draw_room(self, room_id):
        size = self.rc.get_room_size(room_id)
        height = size[0]
        width = size[1]
        self.tableWidget.setColumnCount(width)
        self.tableWidget.setRowCount(height)
        h_header = self.tableWidget.horizontalHeader()
        h_header.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        v_header = self.tableWidget.verticalHeader()
        v_header.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

    def draw_shelving(self, shelving_id):
        size = self.sfc.get_shelf_size(shelving_id)
        height = size[0]
        width = size[1]
        self.tableWidget.setColumnCount(width)
        self.tableWidget.setRowCount(height)
        h_header = self.tableWidget.horizontalHeader()
        h_header.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        v_header = self.tableWidget.verticalHeader()
        v_header.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

    def draw(self, item):
        index = item.data(0, QtCore.Qt.UserRole)
        if isinstance(index, Room):
            self.selected_room = index
            self.draw_room(index.id)
            pass
        elif isinstance(index, Shelving):
            self.selected_shelving = index
            self.draw_shelving(index.id)
            pass
        elif isinstance(index, Shelf):
            self.selected_shelf = index
            self.draw_shelf(index.id)
            pass

    def controll_buttons(self, item):
        index = item.data(0, QtCore.Qt.UserRole)
        if isinstance(index, Room):
            self.actionDeleteRoom.setEnabled(True)
            self.actionNewRoom.setEnabled(True)
            self.actionEditRoom.setEnabled(True)
            self.menuShelving.setEnabled(True)
            self.actionCreateShelving.setEnabled(True)
            self.actionEditShelving.setEnabled(False)
            self.actionRemoveShelving.setEnabled(False)
            self.actionAddShelf.setEnabled(False)
            self.actionRemoveShelf.setEnabled(False)
            self.action.setEnabled(True)
            self.actionVer.setEnabled(True)
            self.actionCrear.setEnabled(True)
            pass
        elif isinstance(index, Shelving):
            self.actionDeleteRoom.setEnabled(False)
            self.actionNewRoom.setEnabled(True)
            self.actionEditRoom.setEnabled(False)
            self.actionCreateShelving.setEnabled(True)
            self.actionRemoveShelving.setEnabled(True)
            self.actionAddShelf.setEnabled(True)
            self.actionRemoveShelf.setEnabled(False)
            self.action.setEnabled(True)
            self.actionVer.setEnabled(True)
            self.actionCrear.setEnabled(True)
            pass
        elif isinstance(index, Shelf):
            self.actionDeleteRoom.setEnabled(False)
            self.actionNewRoom.setEnabled(True)
            self.actionEditRoom.setEnabled(False)
            self.actionCreateShelving.setEnabled(True)
            self.actionRemoveShelving.setEnabled(True)
            self.actionAddShelf.setEnabled(True)
            self.actionRemoveShelf.setEnabled(False)
            self.action.setEnabled(True)
            self.actionVer.setEnabled(True)
            self.actionCrear.setEnabled(True)
            # TODO: Hacer que se puedan añadir objetos y sus botones
            pass


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.setWindowFlags(MainWindow.windowFlags() | QtCore.Qt.CustomizeWindowHint |
                              QtCore.Qt.WindowMinimizeButtonHint |
                              QtCore.Qt.WindowMaximizeButtonHint |
                              QtCore.Qt.WindowCloseButtonHint)
    ui.populate_templates()
    MainWindow.show()
    app.exec_()
