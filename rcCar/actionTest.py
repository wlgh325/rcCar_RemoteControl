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

            if is_finish == 0:
                query = QtSql.QSqlQuery("update command1 set is_finish=1 where is_finish=0")
                print(cmdTime, cmdType, cmdArg)

                if cmdType == "go":
                    self.car.go()

                if cmdType == "back":
                    self.car.back()

                if cmdType == "move":
                    self.car.move()
                
                if cmdType == "left":
                    self.car.steer_left()
                
                if cmdType == "right":
                    self.car.steer_right()
    def go(self):
        print("MOTOR GOGOGO")

    def back(self):
        print("MOTOR BACKBACK")
    
    def move(self):
        print("MOTOR MOVE")

    def left(self):
        print("MOTOR LEFT")

    def right(self):
        print("MOTOR RIGHT")

th = pollingThread()
th.start()

app = QApplication([])

while True:
    pass
