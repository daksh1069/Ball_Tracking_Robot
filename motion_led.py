import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(16, GPIO.IN) #PIR
GPIO.setup(18, GPIO.OUT) #BUzzer

try:
    time.sleep(2) # to stabilize sensor
    while True:
        if GPIO.input(16):
            GPIO.output(18, True)
            print("Motion Detected...")
            time.sleep(5) #to avoid multiple detection
            GPIO.output(18, False)
        time.sleep(0.1) #loop delay, should be less than detection delay

except:
    GPIO.cleanup()