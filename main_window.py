from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import QTableWidgetItem

import sqlitedb
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.sdb = sqlitedb.Sqlite_DB()
        self.index_row = None
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(542, 412)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
    ### tab_1 ###
        self.tab_1 = QtWidgets.QWidget()
        self.tab_1.setObjectName("tab_1")
        self.comboBox = QtWidgets.QComboBox(self.tab_1)
        self.comboBox.setGeometry(QtCore.QRect(120, 40, 78, 22))
        self.comboBox.setObjectName("comboBox")
        self.label_2 = QtWidgets.QLabel(self.tab_1)
        self.label_2.setGeometry(QtCore.QRect(20, 40, 71, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.tab_1)
        self.label_3.setGeometry(QtCore.QRect(20, 70, 55, 16))
        self.label_3.setObjectName("label_3")
        self.comboBox_2 = QtWidgets.QComboBox(self.tab_1)
        self.comboBox_2.setGeometry(QtCore.QRect(120, 70, 78, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.label_4 = QtWidgets.QLabel(self.tab_1)
        self.label_4.setGeometry(QtCore.QRect(20, 130, 85, 16))
        self.label_4.setObjectName("label_4")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.tab_1)
        self.lineEdit_3.setGeometry(QtCore.QRect(120, 130, 113, 22))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_comment = QtWidgets.QLabel(self.tab_1)
        self.label_comment.setGeometry(QtCore.QRect(20, 150, 85, 16))
        self.label_comment.setObjectName("label_comment")
        self.lineEdit_comment = QtWidgets.QLineEdit(self.tab_1)
        self.lineEdit_comment.setGeometry(QtCore.QRect(120, 150, 113, 22))
        self.lineEdit_comment.setObjectName("lineEdit_comment")
        self.pushButton_6 = QtWidgets.QPushButton(self.tab_1)
        self.pushButton_6.setGeometry(QtCore.QRect(20, 210, 93, 28))
        self.pushButton_6.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.tab_1)
        self.pushButton_4.setGeometry(QtCore.QRect(120, 210, 93, 28))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.tab_1)
        self.pushButton_5.setGeometry(QtCore.QRect(220, 210, 93, 28))
        self.pushButton_5.setObjectName("pushButton_5")
        self.label_5 = QtWidgets.QLabel(self.tab_1)
        self.label_5.setGeometry(QtCore.QRect(10, 10, 101, 20))
        self.label_5.setObjectName("label_5")
        self.comboBox_3 = QtWidgets.QComboBox(self.tab_1)
        self.comboBox_3.setGeometry(QtCore.QRect(120, 10, 78, 22))
        self.comboBox_3.setObjectName("comboBox_3")
        self.draw_cmb_User()
        self.draw_cmb_Category()
        self.draw_cmb_Good()
        self.tabWidget.addTab(self.tab_1, "")

    ### tab_2 ###
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.pushButton = QtWidgets.QPushButton(self.tab_2)
        self.pushButton.setGeometry(QtCore.QRect(410, 300, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_2.setGeometry(QtCore.QRect(310, 300, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_3.setGeometry(QtCore.QRect(210, 300, 93, 28))
        self.pushButton_3.setObjectName("pushButton_3")
        self.lineEdit = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit.setGeometry(QtCore.QRect(10, 20, 113, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(10, 50, 113, 22))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.radioButton = QtWidgets.QRadioButton(self.tab_2)
        self.radioButton.setGeometry(QtCore.QRect(10, 90, 95, 21))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.tab_2)
        self.radioButton_2.setGeometry(QtCore.QRect(10, 110, 95, 21))
        self.radioButton_2.setObjectName("radioButton_2")
        self.label = QtWidgets.QLabel(self.tab_2)
        self.label.setGeometry(QtCore.QRect(250, 20, 201, 111))
        self.label.setText("")
        self.label.setObjectName("label")
        self.tableWidget = QtWidgets.QTableWidget(self.tab_2)
        self.tableWidget.setGeometry(QtCore.QRect(10, 150, 491, 121))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        #self.tableWidget.setRowCount(0)
        self.tableWidget.setHorizontalHeaderLabels(["FIO", "AGE", "GENDER"])
        self.tabWidget.addTab(self.tab_2, "")
        self.verticalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.pushButton.clicked.connect(self.on_click_1)
        self.pushButton_2.clicked.connect(self.table_show)
        self.tableWidget.cellClicked.connect(self.on_click_2)
        self.pushButton_3.clicked.connect(self.delete_user)
        self.comboBox.currentIndexChanged.connect(self.draw_cmb_Good)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Категория"))
        self.label_3.setText(_translate("MainWindow", "Товар"))
        self.label_4.setText(_translate("MainWindow", "Сумма"))
        self.label_comment.setText(_translate("MainWindow", "Комментарий"))
        self.pushButton_6.setText(_translate("MainWindow", "Добавить"))
        self.pushButton_4.setText(_translate("MainWindow", "Отчет_1"))
        self.pushButton_5.setText(_translate("MainWindow", "Отчет_2"))
        self.label_5.setText(_translate("MainWindow", "Пользователь"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), _translate("MainWindow", "Бюджет"))
        self.pushButton.setText(_translate("MainWindow", "Добавить"))
        self.pushButton_2.setText(_translate("MainWindow", "Обновить"))
        self.pushButton_3.setText(_translate("MainWindow", "Удалить"))
        self.radioButton.setText(_translate("MainWindow", "муж"))
        self.radioButton_2.setText(_translate("MainWindow", "жен"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Пользователи"))

    def on_click_1(self):
        print("Click! 1")
        gen = None
        fio = self.lineEdit.text()
        onlyInt = QIntValidator()
        self.lineEdit_2.setValidator(onlyInt)
        age = self.lineEdit_2.text()
        if self.radioButton.isChecked():
            gen = 'male'
        if self.radioButton_2.isChecked():
            gen = 'female'
        sdb = sqlitedb.Sqlite_DB()
        if fio != '' and age != '' and gen is not None:
            user = {'full_name': fio, 'age': int(age), 'gender': gen}
            sdb.add_user(user)
        else:
            print('not numeric')
        print("Click!")

    def table_show(self):
        self.index_row = None
        res = self.sdb.get_all_users()
        print('>>>',res)
        self.tableWidget.setRowCount(len(res))
        for i, it in enumerate(res):
            print(i, it)
            self.tableWidget.setItem(i, 0, QTableWidgetItem(str(it[1])))
            self.tableWidget.setItem(i, 1, QTableWidgetItem(str(it[2])))
            self.tableWidget.setItem(i, 2, QTableWidgetItem(str(it[3])))
        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.show()

    def on_click_2(self):
        for cur_item in self.tableWidget.selectedItems():
            self.index_row = cur_item.row()
            print(self.index_row)

    def delete_user(self):
        #if self.index_row is not None:n
        self.sdb.delete_user(self.index_row + 1)

    def draw_cmb_User(self):
        res = self.sdb.get_all_users()
        self.comboBox_3.clear()
        for i in res:
            self.comboBox_3.addItem(i[1], i[0])

    def draw_cmb_Category(self):
        res = self.sdb.get_all_cat()
        self.comboBox.clear()
        for i in res:
            self.comboBox.addItem(i[1], i[0])

    def draw_cmb_Good(self):
        idx_cat = self.comboBox.currentData()
        res = self.sdb.get_all_goods_in_cat(idx_cat)
        self.comboBox_2.clear()
        for i in res:
            self.comboBox_2.addItem(i[2], i[0])