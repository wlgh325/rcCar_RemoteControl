from PyQt5 import QtSql
from PyQt5.QtWidgets import *
from PyQt5.uic import *
from PyQt5.QtCore import *
from time import sleep

class MyApp(QMainWindow):
	def __init__(self):
		super().__init__()
		loadUi("hi.ui", self)

		# connect db
		self.db = QtSql.QSqlDatabase.addDatabase('QMYSQL')
		self.db.setHostName("3.34.124.67")
		self.db.setDatabaseName("16_1")
		self.db.setUserName("16_1")
		self.db.setPassword("1234")

		while True:
			ok = self.db.open()
			print(ok)
			sleep(1)
			if ok == True : break
	
		self.query = QtSql.QSqlQuery()

		# update data using timer
		self.timer = QTimer()
		self.timer.setInterval(100)
		self.timer.timeout.connect(self.pollingQuery)
		self.timer.start()

	def pressedRight(self):
		self.commandQuery("right", "pressed")
		print("press right")

	def releasedRight(self):
		self.commandQuery("right", "released")
		print("release right")

	def pressedLeft(self):
		self.commandQuery("left", "pressed")
	def releasedLeft(self):
		self.commandQuery("left", "released")
		print("release left")

	def clickedRight(self):
		self.commandQuery("right", "1 sec")
	
	def clickedLeft(self):
		self.commandQuery("left", "1 sec")
	'''	
	def clickedGo(self):
		self.commandQuery("go", "1 sec")
	
	def clickedBack(self):
		self.commandQuery("back", "1 sec")
	'''
	# go
	def pressedGo(self):
		self.commandQuery("go", "pressed")
	def releasedGo(self):
		self.commandQuery("go", "released")
	# back
	def pressedBack(self):
		self.commandQuery("back", "pressed")
	def releasedBack(self):
		self.commandQuery("back", "released")

	def clickedMid(self):
		self.commandQuery("mid", "1 sec")
	
	def pollingQuery(self):
		# command log
		self.query = QtSql.QSqlQuery("select * from command1 order by time desc limit 10")
		str = ""
		while(self.query.next()):
			self.record = self.query.record()
			str = "%s | %10s | %10s | %4d" % (self.record.value(0).toString(), self.record.value(1), self.record.value(2), self.record.value(3))
		
		self.text.setPlainText(str)
		
		# sensing
		self.query = QtSql.QSqlQuery("select * from sensing1 order by time desc limit 15")
		str = ""
		while (self.query.next()):
			self.record = self.query.record()
			str += "%s | %10s | %10s | %10s\n" % (self.record.value(0).toString(), self.record.value(1), self.record.value(2), self.record.value(3))

		self.text2.setPlainText(str)
		
	def commandQuery(self, cmd, arg):
		self.query.prepare("insert into command1 (time, cmd_string, arg_string, is_finish) values (:time, :cmd, :arg, :finish)");
		time = QDateTime().currentDateTime()
		self.query.bindValue(":time", time)
		self.query.bindValue(":cmd",  cmd)
		self.query.bindValue(":arg", arg)
		self.query.bindValue(":finish", 0)
		self.query.exec()
	
app = QApplication([])
win = MyApp()
win.show()
app.exec()
