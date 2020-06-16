from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtSql
from Car import Car
from Raspi_PWM_Servo_Driver import PWM 
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
        self.pwm = PWM(0x6F)
        self.pwm.setPWMFreq(60)
        self.car = Car()
        self.getQuery()

    def getQuery(self):
        while True:
            time.sleep(0.1)
            query = QtSql.QSqlQuery("select * from command2 order by time desc limit 1")
            query.next()
            cmdTime = query.record().value(0)
            cmdType = query.record().value(1)
            cmdArg = query.record().value(2)
            is_finish = query.record().value(3)

            if is_finish == 0:
                query = QtSql.QSqlQuery("update command2 set is_finish=1 where is_finish=0")
                print(cmdTime, cmdType, cmdArg)

                if cmdType == "go":
                    self.car.go()

                if cmdType == "back":
                    self.car.back()
                    
                if cmdType == "stop":
                    self.car.stop()
                    
                if cmdType == "move":
                    self.car.move()
                
                if cmdType == "left":
                    self.car.steer_left()
                
                if cmdType == "right":
                    self.car.steer_right()
                    
                if cmdType == "center":
                    self.car.steer_center()
                    
                if cmdType == "slow":
                    self.car.speedDown()
                    
                if cmdType == "fast":
                    self.car.speedUp()
    def go(self):
        print("MOTOR GOGOGO")
        self.pwm.setPWM(0,0,415);

    def back(self):
        print("MOTOR BACKBACK")
        
    def stop(self):
        print("MOTOR STOP")
    
    def move(self):
        print("MOTOR MOVE")

    def left(self):
        print("MOTOR LEFT")
        self.pwm.setPWM(0,0,300);

    def right(self):
        print("MOTOR RIGHT")
        self.pwm.setPWM(0,0,530);

th = pollingThread()
th.start()

app = QApplication([])

while True:
    pass
