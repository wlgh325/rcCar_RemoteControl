from Raspi_MotorHAT import Raspi_MotorHAT, Raspi_DCMotor

class Car():
    def __init__(self):
        # 모터 ?�정
        self.mh = Raspi_MotorHAT(addr=0x6f)
        self.dcMotor = self.mh.getMotor(3)    # M3?�자??모터 ?�결
        self.speed = 125 # 기본 ?�도 0~255
        self.dcMotor.setSpeed(self.speed)
        # ?�보 ?�정
        self.servo = self.mh._pwm
        self.servo.setPWMFreq(60)
        print("car init")

    # ?�으�?    
    def go(self):
        self.dcMotor.run(Raspi_MotorHAT.FORWARD)
        print("gogo")

    # ?�로
    def back(self):
        self.dcMotor.run(Raspi_MotorHAT.BACKWARD)
        print("back")

    # 모터 ?�동 중�?
    def stop(self):
        self.dcMotor.run(Raspi_MotorHAT.RELEASE)
        print("stop")

    # 빠르�?    
    def speedUp(self):
        self.speed = 255 if self.speed >= 235 else self.speed+20 #최�?255, 20?�위�?증감
        self.dcMotor.setSpeed(self.speed)
        print("speedUp")

    # ?�리�?    
    def speedDown(self):
        self.speed=0 if self.speed <= 20  else self.speed-20  # 최하 0
        self.dcMotor.setSpeed(self.speed)
        print("speedDown")

    # 각도만큼 ?�들 ?��?    
    def steer(self, angle=0): # 각도 -90?~ +90?
        if angle <= -60: # ?�보???�동범위??좌우 ??극단??30?까�???가지 ?�는??
            angle = -60 
        if angle >= 60:
            angle = 60 
        pulse_time = 200+(614-200)//180*(angle+90)  # 200:-90? ~ 614:+90? 비율???�라 맵핑
    
        self.servo.setPWM(0,0,pulse_time)

    # ?�회??    
    def steer_right(self):
        self.servo.setPWM(0,0,300)
        print("steer_right")

    # 좌회??    
    def steer_left(self):
        self.servo.setPWM(0,0,530)
        print("steer_left")

    # ?�들 중앙
    def steer_center(self):
        self.servo.setPWM(0,0,415)
        print("steer_center")

#mh.getMotor(1).run(Raspi_MotorHAT.RELEASE)
#mh.getMotor(2).run(Raspi_MotorHAT.RELEASE)
#mh.getMotor(3).run(Raspi_MotorHAT.RELEASE)
#mh.getMotor(4).run(Raspi_MotorHAT.RELEASE)
