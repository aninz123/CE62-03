from PyQt5 import QtCore, QtGui, QtWidgets,QtChart
import ast
import pymysql.cursors
import sys
import time
from matplotlib.backends.qt_compat import  is_pyqt5
if is_pyqt5():
    from matplotlib.backends.backend_qt5agg import (
        FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
else:
    from matplotlib.backends.backend_qt4agg import (
        FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
from matplotlib.figure import Figure

def Myconverter(mydata):
    def cvt(data):
        try:
            return ast.literal_eval(data)
        except Exception:
            return str(data)

    return tuple(map(cvt, mydata))

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1024, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.bgHome = QtWidgets.QLabel(self.centralwidget)
        self.bgHome.setGeometry(QtCore.QRect(0, 0, 1024, 600))
        self.bgHome.setText("")
        self.bgHome.setPixmap(QtGui.QPixmap("pic/homeAdminUi.png"))
        self.bgHome.setObjectName("bgHome")
        self.btnStore = QtWidgets.QPushButton(self.centralwidget)
        self.btnStore.setGeometry(QtCore.QRect(440, 170, 186, 59))
        self.btnStore.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("pic/btnStore.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnStore.setIcon(icon)
        self.btnStore.setIconSize(QtCore.QSize(186, 59))
        self.btnStore.setObjectName("btnStore")
        self.btnStat = QtWidgets.QPushButton(self.centralwidget)
        self.btnStat.setGeometry(QtCore.QRect(440, 270, 186, 59))
        self.btnStat.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("pic/stat.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnStat.setIcon(icon1)
        self.btnStat.setIconSize(QtCore.QSize(186, 59))
        self.btnStat.setObjectName("btnStat")
        self.btnExit = QtWidgets.QPushButton(self.centralwidget)
        self.btnExit.setGeometry(QtCore.QRect(440, 370, 186, 59))
        self.btnExit.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("pic/btnExit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnExit.setIcon(icon2)
        self.btnExit.setIconSize(QtCore.QSize(186, 59))
        self.btnExit.setObjectName("btnExit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1024, 21))

        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        ########### function+ #########
        self.btnStore.clicked.connect(self.StoreUi)
        self.btnStat.clicked.connect(self.StatUi)
        self.btnExit.clicked.connect(self.exit)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def exit(self):
        sys.exit()

    def HomeUi(self):
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.bgHome = QtWidgets.QLabel(self.centralwidget)
        self.bgHome.setGeometry(QtCore.QRect(0, 0, 1024, 600))
        self.bgHome.setText("")
        self.bgHome.setPixmap(QtGui.QPixmap("pic/homeAdminUi.png"))
        self.bgHome.setObjectName("bgHome")
        self.btnStore = QtWidgets.QPushButton(self.centralwidget)
        self.btnStore.setGeometry(QtCore.QRect(440, 170, 186, 59))
        self.btnStore.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("pic/btnStore.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnStore.setIcon(icon)
        self.btnStore.setIconSize(QtCore.QSize(186, 59))
        self.btnStore.setObjectName("btnStore")
        self.btnStat = QtWidgets.QPushButton(self.centralwidget)
        self.btnStat.setGeometry(QtCore.QRect(440, 270, 186, 59))
        self.btnStat.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("pic/stat.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnStat.setIcon(icon1)
        self.btnStat.setIconSize(QtCore.QSize(186, 59))
        self.btnStat.setObjectName("btnStat")
        self.btnExit = QtWidgets.QPushButton(self.centralwidget)
        self.btnExit.setGeometry(QtCore.QRect(440, 370, 186, 59))
        self.btnExit.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("pic/btnExit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnExit.setIcon(icon2)
        self.btnExit.setIconSize(QtCore.QSize(186, 59))
        self.btnExit.setObjectName("btnExit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1024, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        ########### function+ #########
        self.btnStore.clicked.connect(self.StoreUi)
        self.btnStat.clicked.connect(self.StatUi)
        self.btnExit.clicked.connect(self.exit)


    def StoreUi(self,):
            self.centralwidget = QtWidgets.QWidget(MainWindow)
            self.centralwidget.setObjectName("centralwidget")
            self.bgHome = QtWidgets.QLabel(self.centralwidget)
            self.bgHome.setGeometry(QtCore.QRect(0, 0, 1024, 600))
            self.bgHome.setText("")
            self.bgHome.setPixmap(QtGui.QPixmap("pic/bg.png"))
            self.bgHome.setObjectName("bgHome")
            self.header = QtWidgets.QLabel(self.centralwidget)
            self.header.setGeometry(QtCore.QRect(240, 60, 186, 59))
            self.header.setText("")
            self.header.setPixmap(QtGui.QPixmap("pic/btnStore.png"))
            self.header.setObjectName("header")
            font = QtGui.QFont()
            font.setPointSize(20)
            font.setBold(False)
            font.setWeight(50)

            #################table  store #########################
            self.tStore = QtWidgets.QTableWidget(self.centralwidget)
            self.tStore.setGeometry(QtCore.QRect(230, 160, 479, 331))
            self.tStore.setObjectName("tStore")
            self.tStore.setColumnCount(5)
            self.tStore.setRowCount(0)
            ############### set hader ##############
            header = ['ID', 'Name', 'Cost', 'Sale', 'Store']
            self.tStore.setHorizontalHeaderLabels(header)
            self.tStore.verticalHeader().setVisible(False)
            item=QtWidgets.QTableWidgetItem()
            self.tStore.setColumnWidth(0,25)
            self.tStore.setColumnWidth(1,300)
            self.tStore.setColumnWidth(2,25)
            self.tStore.setColumnWidth(3,25)
            self.tStore.setColumnWidth(4,25)
            ##################################

            self.btnEdit = QtWidgets.QPushButton(self.centralwidget)
            self.btnEdit.setGeometry(QtCore.QRect(740, 250, 264, 59))
            self.btnEdit.setText("")
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("pic/btnEdit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.btnEdit.setIcon(icon)
            self.btnEdit.setIconSize(QtCore.QSize(264, 59))
            self.btnEdit.setObjectName("btnEdit")
            self.btnAnR = QtWidgets.QPushButton(self.centralwidget)
            self.btnAnR.setGeometry(QtCore.QRect(740, 350, 264, 59))
            self.btnAnR.setText("")
            icon1 = QtGui.QIcon()
            icon1.addPixmap(QtGui.QPixmap("pic/btnAnR.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.btnAnR.setIcon(icon1)
            self.btnAnR.setIconSize(QtCore.QSize(264, 59))
            self.btnAnR.setObjectName("btnAnR")
            self.btnBack = QtWidgets.QPushButton(self.centralwidget)
            self.btnBack.setGeometry(QtCore.QRect(20, 520, 186, 59))
            self.btnBack.setText("")
            icon2 = QtGui.QIcon()
            icon2.addPixmap(QtGui.QPixmap("pic/btnBack.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.btnBack.setIcon(icon2)
            self.btnBack.setIconSize(QtCore.QSize(186, 59))
            self.btnBack.setObjectName("btnBack")
            MainWindow.setCentralWidget(self.centralwidget)
            self.menubar = QtWidgets.QMenuBar(MainWindow)
            self.menubar.setGeometry(QtCore.QRect(0, 0, 1024, 21))
            self.menubar.setObjectName("menubar")
            MainWindow.setMenuBar(self.menubar)



            ########### function+ #########
            self.btnBack.clicked.connect(self.HomeUi)
            self.btnEdit.clicked.connect(self.EditUi)
            self.btnAnR.clicked.connect(self.AnRUi)
            self.LoadDataStore()
            ############  print table ########

    def StatUi(self):

            self.centralwidget = QtWidgets.QWidget(MainWindow)
            self.centralwidget.setObjectName("centralwidget")
            self.bgHome = QtWidgets.QLabel(self.centralwidget)
            self.bgHome.setGeometry(QtCore.QRect(0, 0, 1024, 600))
            self.bgHome.setText("")
            self.bgHome.setPixmap(QtGui.QPixmap("pic/bg.png"))
            self.bgHome.setObjectName("bgHome")
            self.header = QtWidgets.QLabel(self.centralwidget)
            self.header.setGeometry(QtCore.QRect(240, 60, 186, 59))
            self.header.setText("")
            self.header.setPixmap(QtGui.QPixmap("pic/stat.png"))
            self.header.setWordWrap(False)
            self.header.setObjectName("header")
            self.btnBack = QtWidgets.QPushButton(self.centralwidget)
            self.btnBack.setGeometry(QtCore.QRect(20, 520, 186, 59))
            self.btnBack.setText("")
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("pic/btnBack.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.btnBack.setIcon(icon)
            self.btnBack.setIconSize(QtCore.QSize(186, 59))
            self.btnBack.setObjectName("btnBack")
            self.thot = QtWidgets.QTableWidget(self.centralwidget)
            self.thot.setGeometry(QtCore.QRect(700, 150, 260, 220))
            self.thot.setObjectName("tableWidget")

            self.thot.setColumnCount(2)
            self.thot.setRowCount(0)
            header = ['Name', 'pieces']
            self.thot.setHorizontalHeaderLabels(header)
            self.thot.verticalHeader().setVisible(False)
            item = QtWidgets.QTableWidgetItem()
            self.thot.setColumnWidth(0, 200)
            self.thot.setColumnWidth(1, 20)

            font = QtGui.QFont()
            font.setPointSize(15)
            self.Bprofit = QtWidgets.QLabel(self.centralwidget)
            self.Bprofit.setText('Profit ')
            self.Bprofit.setFont(font)
            self.Bprofit.setGeometry(QtCore.QRect(520, 50, 175, 30))
            self.profit = QtWidgets.QLabel(self.centralwidget)
            self.profit.setFont(font)
            self.profit.setGeometry(QtCore.QRect(530, 90, 175, 30))

            self.Bath1 = QtWidgets.QLabel(self.centralwidget)
            self.Bath1.setText('Bath')
            self.Bath1.setFont(font)
            self.Bath1.setGeometry(QtCore.QRect(580, 90, 175, 30))

            self.Btotal = QtWidgets.QLabel(self.centralwidget)
            self.Btotal.setText('Total ')
            self.Btotal.setFont(font)
            self.Btotal.setGeometry(QtCore.QRect(700, 50, 175, 30))

            self.total = QtWidgets.QLabel(self.centralwidget)
            self.total.setFont(font)
            self.total.setGeometry(QtCore.QRect(720, 90, 175, 30))


            self.Bath2 = QtWidgets.QLabel(self.centralwidget)
            self.Bath2.setText('Bath')
            self.Bath2.setFont(font)
            self.Bath2.setGeometry(QtCore.QRect(770, 90, 175, 30))

            MainWindow.setCentralWidget(self.centralwidget)
            #################################################
            self.starDate = QtWidgets.QLabel(self.centralwidget)
            self.endDate = QtWidgets.QLabel(self.centralwidget)
            self.t1 = QtWidgets.QLabel(self.centralwidget)
            self.t1.setText('Start Date')
            self.t1.setFont(font)
            self.t1.setGeometry(QtCore.QRect(350, 400, 100, 20))

            self.C1 = QtWidgets.QCalendarWidget(self.centralwidget)
            self.C1.setGeometry(QtCore.QRect(350,420, 271, 161))
            self.C1.setSelectionMode(QtWidgets.QCalendarWidget.SingleSelection)
            self.C1.setHorizontalHeaderFormat(QtWidgets.QCalendarWidget.NoHorizontalHeader)
            self.C1.setVerticalHeaderFormat(QtWidgets.QCalendarWidget.NoVerticalHeader)

            self.C1.setSelectedDate(QtCore.QDate.currentDate().addDays(-6))
            self.C1.selectionChanged.connect(self.c1select)

            self.t1 = QtWidgets.QLabel(self.centralwidget)
            self.t1.setText('END Date')
            self.t1.setFont(font)
            self.t1.setGeometry(QtCore.QRect(700, 400, 100, 20))

            self.C2 = QtWidgets.QCalendarWidget(self.centralwidget)
            self.C2.setGeometry(QtCore.QRect(700, 420, 271, 161))
            self.C2.setSelectionMode(QtWidgets.QCalendarWidget.SingleSelection)
            self.C2.setHorizontalHeaderFormat(QtWidgets.QCalendarWidget.NoHorizontalHeader)
            self.C2.setVerticalHeaderFormat(QtWidgets.QCalendarWidget.NoVerticalHeader)
            self.C2.selectionChanged.connect(self.c2select)
            self.C2.setObjectName("Ydate")

            self.Sdate = self.C1.selectedDate()
            self.starDate0 = self.Sdate.toString('yyyy/MM/dd')
            self.Edate = self.C2.selectedDate()
            self.endDate0 = self.Edate.toString('yyyy/MM/dd')
            self.starDate.setText(self.starDate0)
            self.endDate.setText(self.endDate0)

            self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
            self.verticalLayoutWidget.setGeometry(QtCore.QRect(200, 50, 400, 300))
            self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
            static_canvas = FigureCanvas(Figure())
            self.verticalLayout.setContentsMargins(50, 100, 10, 0)
            self.verticalLayout.addWidget(static_canvas)
            self._static_ax = static_canvas.figure.subplots()

            self.LoadDataStat()
            self.btnBack.clicked.connect(self.HomeUi)


    def c1select(self):
        self.Sdate = self.C1.selectedDate()
        self.starDate0 = self.Sdate.toString('yyyy/MM/dd')
        self.starDate.setText(self.starDate0)
        self.LoadDataStat()
    def c2select(self):
        self.Edate = self.C2.selectedDate()
        self.endDate0 = self.Edate.toString('yyyy/MM/dd')
        self.endDate.setText(self.endDate0)
        self.LoadDataStat()

    def create_pie(self):
        pie=QtChart.QPieSeries()
        pie.append('1',10)
        pie.append('2',20)

        chart=QtChart.QChart()
        chart.addSeries(pie)
        #chart.setAnimationOptions(QtChart.SeriesAnimation)
        chartview=QtChart.QChartView(chart)
        #chartview.setRenderHint(QtP)

    def EditUi(self):
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.bgHome = QtWidgets.QLabel(self.centralwidget)
        self.bgHome.setGeometry(QtCore.QRect(0, 0, 1024, 600))
        self.bgHome.setText("")
        self.bgHome.setPixmap(QtGui.QPixmap("pic/bg.png"))
        self.bgHome.setObjectName("bgHome")
        self.header = QtWidgets.QLabel(self.centralwidget)
        self.header.setGeometry(QtCore.QRect(240, 60, 186, 59))
        self.header.setText("")
        self.header.setPixmap(QtGui.QPixmap("pic/btnEdits.png"))
        self.header.setWordWrap(False)
        self.header.setObjectName("header")
        self.btnBack = QtWidgets.QPushButton(self.centralwidget)
        self.btnBack.setGeometry(QtCore.QRect(20, 520, 186, 59))
        self.btnBack.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("pic/btnBack.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnBack.setIcon(icon)
        self.btnBack.setIconSize(QtCore.QSize(186, 59))
        self.btnBack.setObjectName("btnBack")
        self.btnUpdate = QtWidgets.QPushButton(self.centralwidget)
        self.btnUpdate.setGeometry(QtCore.QRect(790, 510, 199, 59))
        self.btnUpdate.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("pic/update.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnUpdate.setIcon(icon1)
        self.btnUpdate.setIconSize(QtCore.QSize(199, 59))
        self.btnUpdate.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)

        self.tEdit = QtWidgets.QTableWidget(self.centralwidget)
        self.tEdit.setGeometry(QtCore.QRect(240, 160, 500, 201))
        self.tEdit.setObjectName("tEdit")
        self.tEdit.setColumnCount(3)
        self.tEdit.setRowCount(0)
        ############### set hader ##############
        header = ['Name', 'Cost', 'Sale' ]
        self.tEdit.setHorizontalHeaderLabels(header)
        self.tEdit.verticalHeader().setVisible(False)
        item = QtWidgets.QTableWidgetItem()
        self.tEdit.setColumnWidth(0, 380)
        self.tEdit.setColumnWidth(1,50)
        self.tEdit.setColumnWidth(2, 50)
        ##################################
        #####################  Edit  input  #
        self.isale =QtWidgets.QLineEdit(self.centralwidget)
        self.isale.setPlaceholderText("sale")
        self.isale.setGeometry(QtCore.QRect(689, 380, 50, 20))

        self.icost = QtWidgets.QLineEdit(self.centralwidget)
        self.icost.setPlaceholderText("cost")
        self.icost.setGeometry(QtCore.QRect(639, 380, 50, 20))

        self.seminput = QtWidgets.QComboBox(self.centralwidget)
        self.seminput.setGeometry(QtCore.QRect(240, 380, 395, 20))
        self.seminput.addItem("Mama Cup Pork Flavour")
        self.seminput.addItem("Mama Pork Flavour 60g")
        self.seminput.addItem("Koko Krunch 25g")
        self.seminput.addItem("Kato Mango Stickky Rice")
        self.seminput.addItem("Kato Lychee")
        self.seminput.addItem("Nut Natur Roasted Alm. 35g")
        self.seminput.addItem("Breeze Excewl Green 30ml *4 ")
        self.seminput.addItem("Breeze Excel Pink 30ml *4")
        self.seminput.addItem("Minere Water 500ml")
        self.seminput.addItem("Quick Cup Tom Klong flavour")
        self.seminput.addItem("Quick Tom Klong 60g")
        self.seminput.addItem("Nut Natur Roasted Cashew. 35g")
        self.seminput.addItem("Purra Water 750 ml")
        self.seminput.addItem("Lay Nori Seaweed 75g")
        self.seminput.addItem("Lay Original 75g")


        ########### function+ #########
        self.btnBack.clicked.connect(self.StoreUi)
        self.btnUpdate.clicked.connect(self.updateEdit)

        self.LoadDataEdit()
        #############  btn update

    def AnRUi(self):
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.bgHome = QtWidgets.QLabel(self.centralwidget)
        self.bgHome.setGeometry(QtCore.QRect(0, 0, 1024, 600))
        self.bgHome.setText("")
        self.bgHome.setPixmap(QtGui.QPixmap("pic/bg.png"))
        self.bgHome.setObjectName("bgHome")
        self.header = QtWidgets.QLabel(self.centralwidget)
        self.header.setGeometry(QtCore.QRect(240, 60, 264, 59))
        self.header.setText("")
        self.header.setPixmap(QtGui.QPixmap("pic/btnAnR.png"))
        self.header.setWordWrap(False)
        self.header.setObjectName("header")
        self.btnBack = QtWidgets.QPushButton(self.centralwidget)
        self.btnBack.setGeometry(QtCore.QRect(20, 520, 186, 59))
        self.btnBack.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("pic/btnBack.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnBack.setIcon(icon)
        self.btnBack.setIconSize(QtCore.QSize(186, 59))
        self.btnBack.setObjectName("btnBack")
        self.tAnR = QtWidgets.QTableWidget(self.centralwidget)

        self.tAnR.setGeometry(QtCore.QRect(240, 160, 470, 200))
        self.tAnR.setObjectName("tAnR")
        self.tAnR.setColumnCount(2)
        self.tAnR.setRowCount(0)
        ############### set hader ##############
        header = ['Name',  'Store']
        self.tAnR.setHorizontalHeaderLabels(header)
        self.tAnR.verticalHeader().setVisible(False)
        item = QtWidgets.QTableWidgetItem()
        self.tAnR.setColumnWidth(0, 410)
        self.tAnR.setColumnWidth(1,40)
        ##################################
        self.btnAdd = QtWidgets.QPushButton(self.centralwidget)
        self.btnAdd.setGeometry(QtCore.QRect(780, 420, 179, 59))
        self.btnAdd.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("pic/btnAdd.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnAdd.setIcon(icon1)
        self.btnAdd.setIconSize(QtCore.QSize(179, 59))
        self.btnAdd.setObjectName("btnAdd")
        self.btnRemove = QtWidgets.QPushButton(self.centralwidget)
        self.btnRemove.setGeometry(QtCore.QRect(780, 520, 179, 59))
        self.btnRemove.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("pic/btnRemove.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnRemove.setIcon(icon2)
        self.btnRemove.setIconSize(QtCore.QSize(179, 59))
        self.btnRemove.setObjectName("btnRemove")
        MainWindow.setCentralWidget(self.centralwidget)
        self.ARinput = QtWidgets.QComboBox(self.centralwidget)
        self.ARinput.setGeometry(QtCore.QRect(240, 380, 420, 20))
        self.ARinput = QtWidgets.QComboBox(self.centralwidget)
        self.ARinput.setGeometry(QtCore.QRect(240, 380, 395, 20))
        self.ARinput.addItem("Mama Cup Pork Flavour")
        self.ARinput.addItem("Mama Pork Flavour 60g")
        self.ARinput.addItem("Koko Krunch 25g")
        self.ARinput.addItem("Kato Mango Stickky Rice")
        self.ARinput.addItem("Kato Lychee")
        self.ARinput.addItem("Nut Natur Roasted Alm. 35g")
        self.ARinput.addItem("Breeze Excewl Green 30ml *4 ")
        self.ARinput.addItem("Breeze Excel Pink 30ml *4")
        self.ARinput.addItem("Minere Water 500ml")
        self.ARinput.addItem("Quick Cup Tom Klong flavour")
        self.ARinput.addItem("Quick Tom Klong 60g")
        self.ARinput.addItem("Nut Natur Roasted Cashew. 35g")
        self.ARinput.addItem("Purra Water 750 ml")
        self.ARinput.addItem("Lay Nori Seaweed 75g")
        self.ARinput.addItem("Lay Original 75g")

        self.inum = QtWidgets.QLineEdit(self.centralwidget)
        self.inum.setPlaceholderText("Number")
        self.inum.setGeometry(QtCore.QRect(660, 380, 50, 20))



        ########### function+ #########
        self.btnBack.clicked.connect(self.StoreUi)
        self.btnAdd.clicked.connect(self.addNum)
        self.btnRemove.clicked.connect(self.removeNum)
        self.LoadDataAnR()

    def LoadDataStore(self):
        db = pymysql.connect('db4free.net', 'sqlce2020', 'vzqrvzqr', 'item2020')

        cursor=db.cursor()
        cursor.execute("SELECT * FROM `products` ")
        data = cursor.fetchall()
        for row in data:
            self.addTableStore(Myconverter(row))
        cursor.close()

    def LoadDataEdit(self):
        db = pymysql.connect('db4free.net', 'sqlce2020', 'vzqrvzqr', 'item2020')

        cursor=db.cursor()
        cursor.execute("SELECT `name`, `cost`, `sale` FROM `products` ")
        data = cursor.fetchall()
        for row in data:
            self.addTableEdit(Myconverter(row))
        cursor.close()

    def LoadDataAnR(self):
        db = pymysql.connect('db4free.net', 'sqlce2020', 'vzqrvzqr', 'item2020')

        cursor=db.cursor()
        cursor.execute("SELECT `name`, `Store` FROM `products` ")
        data = cursor.fetchall()
        for row in data:
            self.addTableAnR(Myconverter(row))
        cursor.close()

    def LoadDataStat(self):

        sDate=''
        eDate=''
        sDate=self.starDate.text()
        eDate=self.endDate.text()

        db = pymysql.connect('db4free.net', 'sqlce2020', 'vzqrvzqr', 'item2020')

        while(self.thot.rowCount()>0):
            self.thot.removeRow(0)


        cursor = db.cursor()
        rows = cursor.execute("SELECT Name,COUNT(Name) FROM `payment` WHERE Date BETWEEN '"+sDate+"' AND '"+eDate+"'GROUP BY Name ORDER BY COUNT(Name)DESC ")
        data = cursor.fetchall()
        for row in data:
            self.addTableStat(Myconverter(row))
        cursor.close()

        cursor = db.cursor()
        rows = cursor.execute("SELECT SUM(Profit) FROM `payment` WHERE Date BETWEEN '"+sDate+"' AND '"+eDate+"'  ")
        data = cursor.fetchone()
        for row in data:
            self.profit.setText(str(row))
        cursor.close()

        cursor = db.cursor()
        rows = cursor.execute("SELECT SUM(Total) FROM `payment` WHERE Date BETWEEN '"+sDate+"' AND '"+eDate+"'  ")
        data = cursor.fetchone()
        for row in data:
            self.total.setText(str(row))
        cursor.close()

        self.Bdate=self.Sdate.daysTo(self.Edate)
        listProfit = [0] * (int(self.Bdate) + 1)
        for i in range(len(listProfit)):
            listProfit[i] = 0

        cursor = db.cursor()
        rows = cursor.execute(
            "SELECT SUM(Profit),Date FROM `payment` WHERE Date BETWEEN '"+sDate+"' AND '"+eDate+"' GROUP BY Date")
        data = cursor.fetchall()
        self.i=0
        for row in data:

            listProfit[self.i]=int(row[0])
            self.i=self.i+1
        cursor.close()
        static_canvas = FigureCanvas(Figure())
        self.updateplot()
        self._static_ax.plot(listProfit)
        self._static_ax.figure.canvas.draw()


    def updateplot(self):
        self._static_ax.clear()


    def addTableStore(self,columns):
        rowPosition=self.tStore.rowCount()
        self.tStore.insertRow(rowPosition)

        for i,column in enumerate(columns):
            self.tStore.setItem(rowPosition,i,QtWidgets.QTableWidgetItem(str(column)))

    def addTableEdit(self,columns):
        rowPosition=self.tEdit.rowCount()
        self.tEdit.insertRow(rowPosition)

        for i,column in enumerate(columns):
            self.tEdit.setItem(rowPosition,i,QtWidgets.QTableWidgetItem(str(column)))

    def addTableAnR(self,columns):
        rowPosition=self.tAnR.rowCount()
        self.tAnR.insertRow(rowPosition)

        for i,column in enumerate(columns):
            self.tAnR.setItem(rowPosition,i,QtWidgets.QTableWidgetItem(str(column)))

    def addTableStat(self,columns):
        rowPosition = self.thot.rowCount()
        self.thot.insertRow(rowPosition)

        for i, column in enumerate(columns):
            self.thot.setItem(rowPosition, i, QtWidgets.QTableWidgetItem(str(column)))

    def updateEdit(self):
        name=''
        cost=''
        sale=''
        name=self.seminput.itemText(self.seminput.currentIndex())
        cost=self.icost.text()
        sale=self.isale.text()
        db = pymysql.connect('db4free.net', 'sqlce2020', 'vzqrvzqr', 'item2020')

        cursor = db.cursor()
        if (cost == '' and sale != ''):
            cursor.execute("UPDATE products SET  Sale = '"+sale+"' WHERE Name = '"+name+"'")
        elif (cost != '' and sale == ''):
            cursor.execute("UPDATE products SET Cost = '"+cost+"'  WHERE Name = '"+name+"'")
        elif (sale != '' and cost != ''):
            cursor.execute("UPDATE products SET Cost = '"+cost+"', Sale = '"+sale+"' WHERE Name = '"+name+"'")
            #print("UPDATE products SET Cost = '"+cost+"', Sale = '"+sale+"' WHERE Name = '"+name+"'")
        db.commit()
        cursor.close()
        self.EditUi()

    def addNum(self):
        name=''
        num=''
        name=self.ARinput.itemText(self.ARinput.currentIndex())
        num=self.inum.text()
        db = pymysql.connect('db4free.net', 'sqlce2020', 'vzqrvzqr', 'item2020')

        cursor = db.cursor()
        cursor.execute("SELECT `name`, `Store` FROM `products` ")
        data = cursor.fetchall()
        for row in data:
            if(row[0]==name):
                oldnum=row[1]
                cursor.close()

        Newnum=oldnum+int(num)
        Newnum=str(Newnum)
        cursor = db.cursor()
        cursor.execute("UPDATE products SET  Store = '" + Newnum + "' WHERE Name = '" + name + "'")
        db.commit()
        cursor.close()
        self.AnRUi()

    def removeNum(self):
        name = ''
        num = ''
        name = self.ARinput.itemText(self.ARinput.currentIndex())
        num = self.inum.text()
        db = pymysql.connect('db4free.net', 'sqlce2020', 'vzqrvzqr', 'item2020')

        cursor = db.cursor()
        cursor.execute("SELECT `name`, `Store` FROM `products` ")
        data = cursor.fetchall()
        for row in data:
            if (row[0] == name):
                oldnum = row[1]
                cursor.close()

        Newnum = oldnum - int(num)
        Newnum = str(Newnum)
        cursor = db.cursor()
        cursor.execute("UPDATE products SET  Store = '" + Newnum + "' WHERE Name = '" + name + "'")
        db.commit()
        cursor.close()
        self.AnRUi()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
