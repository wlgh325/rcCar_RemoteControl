from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtSql
from Car import Car 
from sense_hat import SenseHat
from SenseImage import SenseImage
import time

class pollingThread(QThread):
    def __init__(self):
        super().__init__()
        self.left_pressed = False
        self.right_pressed = False
        self.image = SenseImage()

    def run(self):
        self.db = QtSql.QSqlDatabase.addDatabase('QMYSQL')
        self.db.setHostName("3.34.124.67")
        self.db.setDatabaseName("16_1")
        self.db.setUserName("16_1")
        self.db.setPassword("1234")
        ok = self.db.open()
        print(ok)

        self.car = Car()
        self.start=0
        self.sense = SenseHat()
        while True:
            time.sleep(0.1)
            self.getQuery()
            self.setQuery()
            self.showStatus()

    def setQuery(self):
        pressure = self.sense.get_pressure()
        temp = self.sense.get_temperature()
        humidity = self.sense.get_humidity()
    
        p = round((pressure - 1000) / 100, 3)
        t = round(temp / 100, 3)
        h = round(humidity / 100, 3)
    
        #msg = "Press : " + str(p) + "  Temp : " + str(t) + "  Humid : " + str(h)
        #print(msg)    
        self.query = QtSql.QSqlQuery();
        self.query.prepare("insert into sensing1 (time, num1, num2, num3, meta_string, is_finish) values (:time, :num1, :num2, :num3, :meta, :finish)");
        time = QDateTime().currentDateTime()
        self.query.bindValue(":time", time)
        self.query.bindValue(":num1", p)
        self.query.bindValue(":num2", t)
        self.query.bindValue(":num3", h)
        self.query.bindValue(":meta", "")
        self.query.bindValue(":finish", 0)
        self.query.exec()
       
        '''
        a = int((p * 1271) % 256)
        b = int((t * 1271) % 256)
        c = int((h * 1271) % 256)
        self.sensing.sense.clear(a, b, c)
        '''

    def getQuery(self):
        
        query = QtSql.QSqlQuery("select * from command1 order by time desc limit 1")
        query.next()
        cmdTime = query.record().value(0)
        cmdType = query.record().value(1)
        cmdArg = query.record().value(2)
        is_finish = query.record().value(3)
        
        
        if is_finish == 0:
            query = QtSql.QSqlQuery("update command1 set is_finish=1 where is_finish=0")
            print(cmdTime, cmdType, cmdArg)
            '''
            # 초 만큼 움직이기
            if cmdType == "go":
                self.car.go()
                input_time = self.getTime(cmdArg)
                self.start = time.time()
                while True:
                    if time.time() - self.start > input_time:
                        self.car.stop()
                        break
                
            if cmdType == "back":
                self.car.back()
                input_time = self.getTime(cmdArg)
                self.start = time.time()
                while True:
                    if time.time() - self.start > input_time:
                        self.car.stop()
                        break
            '''
            # go and Back move
            if cmdType == "go":
                self.car.go()

            if cmdType == "back":
                self.car.back()

            # control speed
            if cmdType == "accel":
                self.car.speedUp()
            if cmdType == "break":
                self.car.speedDown()

            if cmdType == "move":
                self.car.move()
            
            # left button
            if cmdType == "left" and cmdArg == "pressed":
                self.left_pressed = True

            if cmdType == "left" and cmdArg == "released":
                self.left_pressed = False

            # right button
            if cmdType == "right" and cmdArg == "pressed":
                self.right_pressed = True

            if cmdType == "right" and cmdArg == "released":
                self.right_pressed = False
            
            # mid
            if cmdType == "mid":
                self.car.steer_center()
                   
        if self.left_pressed == True:
            self.car.steer_left()
        if self.right_pressed == True:
            self.car.steer_right()

    def getTime(self, cmdArg):
        return int(cmdArg.split(' ')[0])
    
    def getAngle(self, cmdArg):
        return int(cmdArg.split(' ')[0])

    # show image
    def showStatus(self):
        status = self.car.status
        if status == "stop":
            self.showStop()
        elif status == "left":
            self.showLeft()
        elif status == "right":
            self.showRight()
        elif status == "go":
            self.showGo()
        elif status == "back":
            self.showBack()

    def showStop(self):
        self.sense.set_pixels(self.image.stopImage)
    def showGo(self):
        self.sense.set_pixels(self.image.goImage)
    def showBack(self):
        self.sense.set_pixels(self.image.backImage)
    def showLeft(self):
        self.sense.set_pixels(self.image.leftImage)
    def showRight(self):
        self.sense.set_pixels(self.image.rightImage)

th = pollingThread()
th.start()
app = QApplication([])

while True:
    pass
