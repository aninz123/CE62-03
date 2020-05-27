
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer
from getpass import getpass
import subprocess
import pyqrcode
#import crc16
import cv2
import time
import os
import pymysql.cursors


class Ui_MainWindow(object):
    total=0
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1024, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        ################# hide tiele bar #################
        MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        MainWindow.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        #MainWindow.showFullScreen()
        ##############################################
        self.centralwidget.setObjectName("centralwidget")
        self.btnhome = QtWidgets.QPushButton(self.centralwidget)
        self.btnhome.setGeometry(QtCore.QRect(0, 0, 1024, 600))
        self.btnhome.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("pic/home.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnhome.setIcon(icon)
        self.btnhome.setIconSize(QtCore.QSize(1024, 600))
        self.btnhome.setObjectName("home")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1024, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        ########### function+ #########
        self.btnhome.clicked.connect(self.warnUi)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.show()

    def homeUi(self):
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btnhome = QtWidgets.QPushButton(self.centralwidget)
        self.btnhome.setGeometry(QtCore.QRect(0, 0, 1024, 600))
        self.btnhome.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("pic/home.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnhome.setIcon(icon)
        self.btnhome.setIconSize(QtCore.QSize(1024, 600))
        self.btnhome.setObjectName("home")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1024, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        ########### function+ #########
        self.btnhome.clicked.connect(self.warnUi)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def warnUi(self):
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.warn = QtWidgets.QLabel(self.centralwidget)
        self.warn.setGeometry(QtCore.QRect(0, 0, 1024, 600))
        self.warn.setText("")
        self.warn.setPixmap(QtGui.QPixmap("pic/warn.png"))
        self.warn.setObjectName("warn")
        self.btnScan = QtWidgets.QPushButton(self.centralwidget)
        self.btnScan.setGeometry(QtCore.QRect(855, 502, 129, 59))
        self.btnScan.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("pic/Component 7 – 2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnScan.setIcon(icon)
        self.btnScan.setIconSize(QtCore.QSize(129, 59))
        self.btnScan.setObjectName("btnScan")
        self.btnCancel = QtWidgets.QPushButton(self.centralwidget)
        self.btnCancel.setGeometry(QtCore.QRect(550, 502, 160, 59))
        self.btnCancel.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("pic/Component 8 – 2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnCancel.setIcon(icon1)
        self.btnCancel.setIconSize(QtCore.QSize(160, 59))
        self.btnCancel.setObjectName("btnBack")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1024, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        ########### function+ #########
        self.btnScan.clicked.connect(self.loadUi)
        self.btnCancel.clicked.connect(self.homeUi)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def loadUi(self):
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.bg = QtWidgets.QLabel(self.centralwidget)
        self.bg.setGeometry(QtCore.QRect(0, 0, 1024, 600))
        self.bg.setText("")
        self.bg.setPixmap(QtGui.QPixmap("pic/loading.png"))
        self.bg.setObjectName("bg")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1071, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        ########### function+ #########
        #self.cap()
        subprocess.Popen(['python', 'cap.py'])
        #self.scan()
        ######  read file in list #######
        self.scan()
        #######################################################

        #########################################


        self.timer=QTimer()
        self.timer.singleShot(2000,self.listUi)


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def scan(self):
        import subprocess
        import os
        os.chdir('./darknet-master')
        command = "./darknet detector test obj.data yolov3-tiny-obj.cfg yolov3-tiny-obj_5000.weights cap.jpg -dont_show" 
        proc = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
        output = proc.stdout.read()
        x = output.decode("utf-8").split('\n')
        del x[0:5]
        if(len(x)>0):
        	del x[-1]
        self.listitem = [0] * len(x)
        j = 0
        for i in x:
        	cs = i.split(':')[0]
        	self.listitem[j] = cs
        	j = j + 1

        os.chdir('..')

    def listUi(self):
        self.total=0
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.bgList = QtWidgets.QLabel(self.centralwidget)
        self.bgList.setGeometry(QtCore.QRect(0, 0, 1024, 600))
        self.bgList.setText("")
        self.bgList.setPixmap(QtGui.QPixmap("pic/List.png"))
        self.bgList.setObjectName("bgList")
        font = QtGui.QFont()
        font.setPointSize(15)
        ############################  TABLE LIST ###############################

        self.tlist=QtWidgets.QTableWidget(self.centralwidget)
        self.tlist.setGeometry(QtCore.QRect(255, 145, 700, 325))
        self.tlist.setColumnCount(2)
        self.tlist.setRowCount(len(self.listitem))
        self.tlist.setShowGrid(False)
        header = ['Name', 'Price']
        self.tlist.setHorizontalHeaderLabels(header)
        self.tlist.verticalHeader().setVisible(False)
        item = QtWidgets.QTableWidgetItem()
        self.tlist.setColumnWidth(0, 570)
        self.tlist.setColumnWidth(1, 125)


        #########################################################################

        self.btnNext = QtWidgets.QPushButton(self.centralwidget)
        self.btnNext.setGeometry(QtCore.QRect(833, 516, 144, 59))
        self.btnNext.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("pic/Component 6 – 2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnNext.setIcon(icon)
        self.btnNext.setIconSize(QtCore.QSize(144, 59))
        self.btnNext.setObjectName("btnNext")
        self.btnCancel = QtWidgets.QPushButton(self.centralwidget)
        self.btnCancel.setGeometry(QtCore.QRect(605, 516, 160, 59))
        self.btnCancel.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("pic/Component 8 – 2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnCancel.setIcon(icon1)
        self.btnCancel.setIconSize(QtCore.QSize(160, 59))
        self.btnCancel.setObjectName("btnCancel")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1024, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        ########### function+ #########
        if(len(self.listitem)==0):
        	self.homeUi()



        db = pymysql.connect('db4free.net', 'sqlce2020', 'vzqrvzqr', 'item2020')
        cursor = db.cursor()
        cursor.execute("SELECT * FROM `products` WHERE 1 ")
        data = cursor.fetchall()

        for i in range(len(self.listitem)):
            for row in data:
                if (self.listitem[i]==str(row[1])):
                    self.tlist.setItem(i,0,QtWidgets.QTableWidgetItem(str(row[1])))
                    self.tlist.setItem(i,1,QtWidgets.QTableWidgetItem(str(row[3]).rjust(10,' ')+'Bath'.rjust(10,' ')))
                    self.total=self.total+row[3]
        #print(self.total)
        self.tlist.setItem(len(self.listitem), 0, QtWidgets.QTableWidgetItem("Total"))
        self.tlist.setItem(len(self.listitem), 1, QtWidgets.QTableWidgetItem(str(self.total).rjust(10, ' ') + 'Bath'.rjust(10, ' ')))

        cursor.close()



        self.btnCancel.clicked.connect(self.homeUi)
        self.btnNext.clicked.connect(self.paymentUi)
        #self.readCapresult()



        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def readCapresult(self):
        list = [line.rstrip('\n') for line in open("Data/Capresult.txt")]
        for i in list:
            self.listWidget.addItem(str(i))

    def paymentUi(self):
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1024, 600))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("pic/payment.png"))
        self.label.setObjectName("label")
        self.btnPP = QtWidgets.QPushButton(self.centralwidget)
        self.btnPP.setGeometry(QtCore.QRect(259, 219, 202, 121))
        self.btnPP.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("pic/promptpayLogo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnPP.setIcon(icon)
        self.btnPP.setIconSize(QtCore.QSize(202, 121))
        self.btnPP.setObjectName("btnPP")
        self.btnCancel = QtWidgets.QPushButton(self.centralwidget)
        self.btnCancel.setGeometry(QtCore.QRect(432, 479, 160, 59))
        self.btnCancel.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("pic/Component 8 – 2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnCancel.setIcon(icon1)
        self.btnCancel.setIconSize(QtCore.QSize(160, 59))
        self.btnCancel.setObjectName("btnCancel")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1053, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        ########### function+ #########
        self.btnCancel.clicked.connect(self.homeUi)
        self.btnPP.clicked.connect(self.loadGenQRUi)
    def loadGenQRUi(self):
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.bg = QtWidgets.QLabel(self.centralwidget)
        self.bg.setGeometry(QtCore.QRect(0, 0, 1024, 600))
        self.bg.setText("")
        self.bg.setPixmap(QtGui.QPixmap("pic/loading.png"))
        self.bg.setObjectName("bg")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1071, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        ########### function+ #########

        self.timer=QTimer()


        self.genqr()
        self.timer.singleShot(2000,self.qrUi)

    def qrUi(self):
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1024, 600))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("pic/qr.png"))
        self.label.setObjectName("label")
        self.qr = QtWidgets.QLabel(self.centralwidget)
        self.qr.setGeometry(QtCore.QRect(423, 210, 245,245))
        self.qr.setPixmap(QtGui.QPixmap("Data/QR.png"))
        self.qr.setObjectName("qr")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1024, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        ########### function+ #########

        #self.checkBlance()
        #oldblance=self.current


        self.timer = QTimer()
        self.timer.singleShot(2000, self.qrUi2)


        self.genqr()
    def qrUi2(self):
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1024, 600))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("pic/qr.png"))
        self.label.setObjectName("label")
        self.qr = QtWidgets.QLabel(self.centralwidget)
        self.qr.setGeometry(QtCore.QRect(423, 210, 245,245))
        self.qr.setPixmap(QtGui.QPixmap("Data/QR.png"))
        self.qr.setObjectName("qr")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1024, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        ########### function+ #########
        ######################################################################################
        ######################################################################################
        self.checkBlance()
        print(self.current)
        oldblance=self.current
        self.timer = QTimer()
        #self.genqr()
        #self.timer.singleShot(1000, self.paySucUi)
        print('old = '+str(oldblance))
        countBal=0
        while(countBal<7):
            self.checkBlance()
            newblance=self.current
            print('new'+str(newblance))
            #if(newblance-oldblance==self.total):
            if (int(newblance) - int(oldblance) == self.total):
                self.paySucUi()
                break

            countBal=countBal+1
            #print(countBal)
        #self.timer = QTimer()
        self.timer.singleShot(1000, self.homeUi)
    ######################################################################################
#############################################################################################

    def paySucUi(self):
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.bgSuc = QtWidgets.QLabel(self.centralwidget)
        self.bgSuc.setGeometry(QtCore.QRect(0, 0, 1024, 600))
        self.bgSuc.setText("")
        self.bgSuc.setPixmap(QtGui.QPixmap("pic/sucess.png"))
        self.bgSuc.setObjectName("bgSuc")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1024, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        ########### function+ #########
        self.timer = QTimer()
        self.timer.setSingleShot(True)
        self.timer.timeout.connect(self.Home)
        self.timer.start(100)



    def paySucUi2(self):
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.bgSuc = QtWidgets.QLabel(self.centralwidget)
        self.bgSuc.setGeometry(QtCore.QRect(0, 0, 1024, 600))
        self.bgSuc.setText("")
        self.bgSuc.setPixmap(QtGui.QPixmap("pic/sucess.png"))
        self.bgSuc.setObjectName("bgSuc")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1024, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        ########### function+ #########
        self.timer = QTimer()
        self.timer.setSingleShot(True)
        self.timer.timeout.connect(self.homeUi)
        self.timer.start(10000)
        

        Date = QtWidgets.QLabel(self.centralwidget)
        db = pymysql.connect('db4free.net', 'sqlce2020', 'vzqrvzqr', 'item2020')

        Ddate = QtCore.QDate.currentDate()
        Ddate1 = Ddate.toString('yyyy/MM/dd')
        Date.setText(Ddate1)
        Date=Date.text()
        ############ รับค่าไอดีบิล ######################
        cursor = db.cursor()
        cursor.execute("SELECT MAX(Id_bill) FROM `payment`")
        data = cursor.fetchone()
        for row in data:
            Id_bill=row
        cursor.close()

        cursor = db.cursor()
        #cursor.execute("INSERT INTO `payment` (`ID`, `Id_bill`, `Name`, `Date`, `Profit`, `Total`) VALUES (NULL, "+str(Id_bill)+" >, '"+str(self.listitem[i])+"', '"+Date+"', <sale-cos>, <sale>);")
        for i in range(len(self.listitem)):
             db = pymysql.connect('db4free.net', 'sqlce2020', 'vzqrvzqr', 'item2020')
             cursor1=db.cursor()
             cursor1.execute("SELECT * FROM `products` WHERE Name LIKE '"+str(self.listitem[i])+"'")
             data = cursor1.fetchall()
             for row in data:
                profit=int(row[3])-int(row[2])
                sale=int(row[3])
             cursor.close()
             cursor = db.cursor()
             cursor.execute("INSERT INTO `payment` (`ID`, `Id_bill`, `Name`, `Date`, `Profit`, `Total`) VALUES (NULL, '"+str(Id_bill)+"' , '"+str(self.listitem[i])+"', '"+Date+"', '"+str(profit)+"', '"+str(sale)+"');")
             db.commit()
             cursor.close()

        print("sucessful")
        




    def checkBlance(self):
    	command = "python3 c.py"
    	proc = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    	output2 = proc.stdout.read()
    	x2 = output2.decode("utf-8").split('\n')
    	#print(x2[0])
    	self.current=x2[0]
    	time.sleep(3)
    	'''
        db = pymysql.connect('db4free.net', 'sqlce2020', 'vzqrvzqr', 'item2020')
        cursor = db.cursor()
        rows = cursor.execute("SELECT Balance FROM `balance` WHERE ID LIKE '1' ")
        data = cursor.fetchone()
        for row in data:
           self.current=row
        cursor.close()
        '''
        #print(self.current)

    def text_qr(self,account, one_time=True, country="TH", money="", currency="THB"):
        """
        text_qr(account,one_time=True,country="TH",money="",currency="THB")
        account is phone number or  identification number.
        one_time : if you use once than it's True.
        country : TH
        money : money (if have)
        currency : THB
        """
        Version = "0002" + "01"  # เวชั่นของ  PromptPay
        if one_time == True:  # one_time คือ ต้องการให้โค้ดนี้ครั้งเดียวหรือไม่
            one_time = "010212"  # 12 ใช้ครั้งเดียว
        else:
            one_time = "010211"  # 11 ใช้ได้้หลายครั้ง
        merchant_account_information = "2937"  # ข้อมูลผู้ขาย
        merchant_account_information += "0016" + "A000000677010111"  # หมายเลขแอปพลิเคชั่น PromptPay
        if len(account) != 13:  # ใช้บัญชีใช้เป็นเบอร์มือถือหรือไม่ ถ้าใช่ จำนวนจะไม่เท่ากับ 13
            account = list(account)
            merchant_account_information += "011300"  # 01 หมายเลขโทรศัพท์ ความยาว 13 ขึ้นต้น 00
            if country == "TH":
                merchant_account_information += "66"  # รหัสประเทศ 66 คือประเทศไทย
            del account[0]  # ตัดเลข 0 หน้าเบอร์ออก
            merchant_account_information += ''.join(account)
        else:
            merchant_account_information += "02" + account.replace('-',
                                                                   '')  # กรณีที่ไม่รับมือถือ แสดงว่าเป็นเลขบัตรประชาชน
        country = "5802" + country  # ประเทศ
        if currency == "THB":
            currency = "5303" + "764"  # "764"  คือเงินบาทไทย ตาม https://en.wikipedia.org/wiki/ISO_4217
        if money != "":  # กรณีกำหนดเงิน
            check_money = money.split('.')  # แยกจาก .
            if len(check_money) == 1 or len(check_money[1]) == 1:  # กรณีที่ไม่มี . หรือ มีทศนิยมแค่หลักเดียว
                money = "54" + "0" + str(len(str(float(money))) + 1) + str(float(money)) + "0"
            else:
                money = "54" + "0" + str(len(str(float(money)))) + str(float(money))  # กรณีที่มีทศนิยมครบ
        check_sum = Version + one_time + merchant_account_information + country + currency + money + "6304"  # เช็คค่า check sum
        crc = hex(crc16.crc16xmodem(check_sum.encode(), 0xffff)).replace('0x', '')
        if (len(crc) ==3):
            crc = '0' + str(crc)
        check_sum += crc
        return check_sum.upper()

    def genqr(self):
        PrompayCode=self.text_qr("0990528939",one_time=True,money=str(self.total))
        print(PrompayCode)
        print('---gen--')
        pyqrcode.create(str(PrompayCode)).png("Data/QR.png", scale=5)



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.showFullScreen()
    sys.exit(app.exec_())
