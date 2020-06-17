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
        # jahong
        self.MIDPWM = 375
        self.MINPWM = 140
        self.MAXPWM = 450
        #self.MAXANGLE = 60

        # angle
        self.cur_pwm = self.MIDPWM
        self.servo.setPWM(0,0,self.MIDPWM)
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

    def steer_left(self):
        self.cur_pwm -= 30
        if self.cur_pwm > self.MAXPWM:
            self.cur_pwm = self.MAXPWM
        elif self.cur_pwm < self.MINPWM:
            self.cur_pwm = self.MINPWM
        self.servo.setPWM(0,0,self.cur_pwm)
        print("steer_left")
        #pulse_time = self.MIDPWM - (self.MIDPWM-self.MINPWM)/self.MAXANGLE*self.angle

    # 우회전
    def steer_right(self):
        self.cur_pwm += 30
        if self.cur_pwm > self.MAXPWM:
            self.cur_pwm = self.MAXPWM
        elif self.cur_pwm < self.MINPWM:
            self.cur_pwm = self.MINPWM
        self.servo.setPWM(0,0,self.cur_pwm)
        print("steer_right")

    # 핸들 중앙
    def steer_center(self):
        self.servo.setPWM(0,0,375)
        print("steer_center")

#mh.getMotor(1).run(Raspi_MotorHAT.RELEASE)
#mh.getMotor(2).run(Raspi_MotorHAT.RELEASE)
#mh.getMotor(3).run(Raspi_MotorHAT.RELEASE)
#mh.getMotor(4).run(Raspi_MotorHAT.RELEASE)
