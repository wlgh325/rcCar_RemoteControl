from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtSql
from Car import Car 
import time

class pollingThread(QThread):
    def __init__(self):
        super().__init__()

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
        self.left_pressed = False
        self.right_pressed = False
        self.getQuery()

    def getQuery(self):
        while True:
            time.sleep(0.1)
            query = QtSql.QSqlQuery("select * from command1 order by time desc limit 1")
            query.next()
            cmdTime = query.record().value(0)
            cmdType = query.record().value(1)
            cmdArg = query.record().value(2)
            is_finish = query.record().value(3)
            
            # 명령어 처리가 안된 경우 실행
            if is_finish == 0:
                query = QtSql.QSqlQuery("update command1 set is_finish=1 where is_finish=0")
                print(cmdTime, cmdType, cmdArg)

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

                if cmdType == "move":
                    self.car.move()
                
                # left button
                if cmdType == "left" and cmdArg == "pressed":
                    self.car.steer_left()
                    self.left_pressed = True
                if cmdType == "left" and cmdArg == "released":
                    self.left_pressed = False

                # right button
                if cmdType == "right" and cmdArg == "pressed":
                    self.car.steer_right()
                    self.right_pressed = True
                if cmdType == "right" and cmdArg == "released":
                    self.right_pressed = False

                if cmdType == "mid":
                    self.car.steer_center()

                if cmdType == "speedUp":
                    self.car.speedUp()

                if cmdType == "speedDown":
                    self.car.speedDown()
            
            if self.left_pressed == True:
                self.car.steer_left()
            if self.right_pressed == True:
                self.car.steer_right()

    def getTime(self, cmdArg):
         # 작동 시간
        return int(cmdArg.split(' ')[0])
    
    def getAngle(self, cmdArg):
        return int(cmdArg.split(' ')[0])

th = pollingThread()
th.start()

app = QApplication([])

while True:
    pass
