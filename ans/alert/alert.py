import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN)
GPIO.setup(26, GPIO.OUT)

try:
  while True:
    print(GPIO.input(17))

    if GPIO.input(17) == 1:
      GPIO.output(26, GPIO.HIGH)
      time.sleep(0.005)
      
      GPIO.output(26, GPIO.LOW)
      time.sleep(0.005)

    time.sleep(1)
    
except KeyboardInterrupt:
  pass

GPIO.cleanup()

