import RPi.GPIO as GPIO

outputPinRight = 14
outputPinLeft = 15
outputPinEnable = 18

GPIO.setmode(GPIO.BCM)

GPIO.setup(outputPinRight, GPIO.OUT)
GPIO.setup(outputPinLeft, GPIO.OUT)
GPIO.setup(outputPinEnable, GPIO.OUT)

GPIO.output(outputPinRight, GPIO.LOW)
GPIO.output(outputPinLeft, GPIO.LOW)
GPIO.output(outputPinEnable, GPIO.LOW)

while True:
	user_input = str(raw_input("l, r, f, s, q: "))
	if "l" in user_input:
		GPIO.output(outputPinLeft, GPIO.HIGH)
		GPIO.output(outputPinRight, GPIO.LOW)
		GPIO.output(outputPinEnable, GPIO.HIGH)

	elif "r" in user_input:
		GPIO.output(outputPinRight, GPIO.HIGH)
		GPIO.output(outputPinLeft, GPIO.LOW)
		GPIO.output(outputPinEnable, GPIO.HIGH)
        elif "f" in user_input:
                GPIO.output(outputPinLeft, GPIO.HIGH)
                GPIO.output(outputPinRight, GPIO.HIGH)
                GPIO.output(outputPinEnable, GPIO.HIGH)

        elif "s" in user_input:
                GPIO.output(outputPinRight, GPIO.LOW)
                GPIO.output(outputPinLeft, GPIO.LOW)
                GPIO.output(outputPinEnable, GPIO.LOW)
	else:
		break

GPIO.cleanup()
