import time
import RPi.GPIO as GPIO          
from time import sleep
mtc = 32
in1 = 31
in2 = 33
in3 = 22
in4 = 31
ena = 11
enb = 18
temp1=1
GPIO.setmode(GPIO.BOARD)
GPIO.setup(mtc, GPIO.IN)
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(in3,GPIO.OUT)
GPIO.setup(in4,GPIO.OUT)
GPIO.setup(ena,GPIO.OUT)
GPIO.setup(enb,GPIO.OUT)
GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)
GPIO.output(in3,GPIO.LOW)
GPIO.output(in4,GPIO.LOW)
p=GPIO.PWM(ena,1000)
p.start(25)
p=GPIO.PWM(enb,1000)
p.start(25)
print("\n")
print("The default speed & direction of motor is LOW & Forward.....")
print("r-run s-stop f-forward b-backward l-low m-medium h-high e-exit")
print("\n")    
try:
    time.sleep(2) # to stabilize sensor
    while True:
        if GPIO.input(mtc):
            print("Motion Detected...")
            time.sleep(5)
            x='r'
            if x=='r':
                    print("run")
                    if(temp1==1):
                        GPIO.output(in1,GPIO.HIGH)
                        GPIO.output(in2,GPIO.LOW)
                        GPIO.output(in3,GPIO.HIGH)
                        GPIO.output(in4,GPIO.LOW)
                        print("forward")
                        x='z'
                    else:
                        GPIO.output(in1,GPIO.LOW)
                        GPIO.output(in2,GPIO.HIGH)
                        GPIO.output(in3,GPIO.LOW)
                        GPIO.output(in4,GPIO.HIGH)
                        print("backward")
                        x='z'


            elif x=='s':
                        print("stop")
                        GPIO.output(in1,GPIO.LOW)
                        GPIO.output(in2,GPIO.LOW)
                        GPIO.output(in3,GPIO.LOW)
                        GPIO.output(in4,GPIO.LOW)
                        x='z'

            elif x=='f':
                        print("forward")
                        GPIO.output(in1,GPIO.HIGH)
                        GPIO.output(in2,GPIO.LOW)
                        GPIO.output(in3,GPIO.HIGH)
                        GPIO.output(in4,GPIO.LOW)
                        temp1=1
                        x='z'

            elif x=='b':
                        print("backward")
                        GPIO.output(in1,GPIO.LOW)
                        GPIO.output(in2,GPIO.HIGH)
                        GPIO.output(in3,GPIO.LOW)
                        GPIO.output(in4,GPIO.HIGH)
                        temp1=0
                        x='z'

            elif x=='l':
                    print("low")
                    p.ChangeDutyCycle(25)
                    x='z'

            elif x=='m':
                    print("medium")
                    p.ChangeDutyCycle(50)
                    x='z'

            elif x=='h':
                    print("high")
                    p.ChangeDutyCycle(100)
                    x='z'

            ##    elif x=='v':
            ##        print("very high")
            ##        p.ChangeDutyCycle(100)
            ##        x='z'
            ##    
            elif x=='e':
                    GPIO.cleanup()
                    print("GPIO Clean up")
                    break
                
            else:
                    print("<<<  wrong data  >>>")
                    print("please enter the defined data to continue.....")
        time.sleep(0.1)
except:
    GPIO.cleanup()