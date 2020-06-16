from Raspi_PWM_Servo_Driver import PWM

pwm = PWM(0x6F)
pwm.setPWMFreq(50)
pwm.setPWM(0,0,140)
