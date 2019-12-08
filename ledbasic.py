import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(16, GPIO.IN) #PIR
GPIO.setup(18, GPIO.OUT) #BUzzer

while True:
    GPIO.output(18, True)