import time
import RPi.GPIO as GPIO          
from time import sleep
mtc1 = 7
mtc2 = 32
enar = 29
in1r = 31
in2r = 33
enal = 11
in1l = 12
in2l = 13
temp1=1
GPIO.setmode(GPIO.BOARD)
GPIO.setup(mtc1, GPIO.IN)
GPIO.setup(mtc2, GPIO.IN)
GPIO.setup(in1r,GPIO.OUT)
GPIO.setup(in2r,GPIO.OUT)
GPIO.setup(enar,GPIO.OUT)
GPIO.setup(in1l,GPIO.OUT)
GPIO.setup(in2l,GPIO.OUT)
GPIO.setup(enal,GPIO.OUT)
GPIO.output(in1r,GPIO.LOW)
GPIO.output(in2r,GPIO.LOW)
GPIO.output(in1l,GPIO.LOW)
GPIO.output(in2l,GPIO.LOW)
p=GPIO.PWM(enar,1000)
p.start(100)
p1=GPIO.PWM(enal,1000)
p1.start(100)
try:
    time.sleep(2) # to stabilize sensor
    while True:
        if GPIO.input(mtc1):
            print("Motion Detected...")
            print("run")
            GPIO.output(in2r,GPIO.HIGH)
            GPIO.output(in1r,GPIO.LOW)
            GPIO.output(in2l,GPIO.HIGH)
            GPIO.output(in1l,GPIO.LOW)
            time.sleep(1.5)
            GPIO.output(in2r,GPIO.LOW)
            GPIO.output(in1r,GPIO.HIGH)
            GPIO.output(in2l,GPIO.HIGH)
            GPIO.output(in1l,GPIO.LOW)
            print("forward")
            time.sleep(5)
            GPIO.output(in2r,GPIO.LOW)
            GPIO.output(in1r,GPIO.HIGH)
            GPIO.output(in2l,GPIO.LOW)
            GPIO.output(in1l,GPIO.HIGH)
            time.sleep(1.5)
        if GPIO.input(mtc2):
            print("Motion Detected...")
            time.sleep(5)
            print("run")
            GPIO.output(in2r,GPIO.LOW)
            GPIO.output(in1r,GPIO.HIGH)
            GPIO.output(in2l,GPIO.LOW)
            GPIO.output(in1l,GPIO.HIGH)
            time.sleep(1.5)
            GPIO.output(in2r,GPIO.HIGH)
            GPIO.output(in1r,GPIO.LOW)
            GPIO.output(in1l,GPIO.HIGH)
            GPIO.output(in2l,GPIO.LOW)
            print("Back")
            GPIO.output(in2r,GPIO.HIGH)
            GPIO.output(in1r,GPIO.LOW)
            GPIO.output(in2l,GPIO.HIGH)
            GPIO.output(in1l,GPIO.LOW)
            time.sleep(1.5)
        
        time.sleep(0.1)
except:
    print("END...")
    GPIO.cleanup()