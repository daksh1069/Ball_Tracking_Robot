# import the GPIO and time package
import RPi.GPIO as GPIO
import time



# Pin  Definitions
ledPin1 = 7
butPin1 = 12
ledPin2 = 13
butPin2 = 16
ledPin3 = 15
butPin3 = 18



# Pin Setup
GPIO.setmode(GPIO.BOARD)
GPIO.setup(ledPin1, GPIO.OUT)
GPIO.setup(butPin1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(ledPin2, GPIO.OUT)
GPIO.setup(butPin2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(ledPin3, GPIO.OUT)
+
GPIO.setup(butPin3, GPIO.IN, pull_up_down=GPIO.PUD_UP)



print("Program running... Press CTRL+C to exit")
Bool1=False
Bool2=False
Bool3=False
try:
    while True:
        if GPIO.input(butPin1):
			# button is released
            GPIO.output(ledPin1, Bool1)			
        else:
            Bool1=True if (Bool1==False) else False		# button is pressed
            GPIO.output(ledPin1, Bool1)
        time.sleep(0.1)
        if GPIO.input(butPin2):
			# button is released
            GPIO.output(ledPin2, Bool2)			
        else:
            Bool2=True if (Bool2==False) else False		# button is pressed
            GPIO.output(ledPin2, Bool2)
        time.sleep(0.1)
        if GPIO.input(butPin3):
			# button is released
            GPIO.output(ledPin3, Bool3)			
        else:
            Bool3=True if (Bool3==False) else False		# button is pressed	
            GPIO.output(ledPin3, Bool3)
        time.sleep(0.1)
	
except KeyboardInterrupt:
    GPIO.cleanup()
    print("Program terminated!")

