from Raspi_MotorHAT import Raspi_MotorHAT, Raspi_DCMotor

class Car():
    def __init__(self):
        # 모터 설정
        self.mh = Raspi_MotorHAT(addr=0x6f)
        self.dcMotor = self.mh.getMotor(3)    # M3단자에 모터 연결
        self.speed = 125 # 기본 속도 0~255
        self.dcMotor.setSpeed(self.speed)
        # 서보 설정
        self.servo = self.mh._pwm
        self.servo.setPWMFreq(60)
        print("car init")

    # 앞으로
    def go(self):
        self.dcMotor.run(Raspi_MotorHAT.FORWARD)
        print("gogo")

    # 뒤로
    def back(self):
        self.dcMotor.run(Raspi_MotorHAT.BACKWARD)
        print("back")

    # 모터 작동 중지
    def stop(self):
        self.dcMotor.run(Raspi_MotorHAT.RELEASE)
        print("stop")

    # 빠르게
    def speedUp(self):
        self.speed = 255 if self.speed >= 235 else self.speed+20 #최대255, 20단위로 증감
        self.dcMotor.setSpeed(self.speed)
        print("speedUp")

    # 느리게
    def speedDown(self):
        self.speed=0 if speed <= 20  else speed-20  # 최하 0
        self.dcMotor.setSpeed(speed)
        print("speedDown")

    # 각도만큼 핸들 틀기
    def steer(self, angle=0): # 각도 -90˚~ +90˚
        if angle <= -60: # 서보의 작동범위는 좌우 양 극단의 30˚까지는 가지 않는다.
            angle = -60 
        if angle >= 60:
            angle = 60 
        pulse_time = 200+(614-200)//180*(angle+90)  # 200:-90˚ ~ 614:+90˚ 비율에 따라 맵핑
    
        self.servo.setPWM(0,0,pulse_time)

    # 우회전
    def steer_right(self, angle):
        self.steer(angle)
        print("steer_right")

    # 좌회전
    def steer_left(self, angle):
        self.steer(-angle)
        print("steer_left")

    # 핸들 중앙
    def steer_center(self):
        self.steer(0)
        print("steer_center")

#mh.getMotor(1).run(Raspi_MotorHAT.RELEASE)
#mh.getMotor(2).run(Raspi_MotorHAT.RELEASE)
#mh.getMotor(3).run(Raspi_MotorHAT.RELEASE)
#mh.getMotor(4).run(Raspi_MotorHAT.RELEASE)
