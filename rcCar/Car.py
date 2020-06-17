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
        self.servo.setPWMFreq(50)

        # init constant
        self.MIDPWM = 375
        self.MINPWM = 140
        self.MAXPWM = 450
        self.MAXANGLE = 60

        # angle
        self.angle = 0
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

    '''
    # 좌회전
    def steer_left(self, angle):
        if angle > self.MAXANGLE:
            angle = self.MAXANGLE
        pulse_time = self.MIDPWM - (self.MIDPWM-self.MINPWM)/self.MAXANGLE*angle
        self.servo.setPWM(0,0,int(pulse_time))
        print("steer_left")
    '''

    def steer_left(self):
        if self.angle >= self.MAXANGLE:
            self.angle = self.MAXANGLE
        else:
            self.angle+=1
        pulse_time = self.MIDPWM - (self.MIDPWM-self.MINPWM)/self.MAXANGLE*self.angle
        self.servo.setPWM(0,0,int(pulse_time))
        print("steer_left")
        print(self.angle)
    # 우회전
    def steer_right(self):
        if self.angle >= self.MAXANGLE:
            self.angle = self.MAXANGLE
        pulse_time = self.MIDPWM + (self.MAXPWM - self.MIDPWM)/self.MAXANGLE*self.angle
        self.servo.setPWM(0,0,int(pulse_time))
        print("steer_right")
        print(self.angle)
    # 핸들 중앙
    def steer_center(self):
        self.servo.setPWM(0,0,375)
        print("steer_center")

#mh.getMotor(1).run(Raspi_MotorHAT.RELEASE)
#mh.getMotor(2).run(Raspi_MotorHAT.RELEASE)
#mh.getMotor(3).run(Raspi_MotorHAT.RELEASE)
#mh.getMotor(4).run(Raspi_MotorHAT.RELEASE)
