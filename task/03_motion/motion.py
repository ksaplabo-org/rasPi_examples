import RPi.GPIO as GPIO
import time

PIN_IN = 19
PIN_OUT = 26

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN_IN, GPIO.IN)
GPIO.setup(PIN_OUT, GPIO.OUT)

#メイン
try:
  #繰り返す
  while True:
    #現在のPIN状態を標準出力
    print(GPIO.input(PIN_IN))

    if GPIO.input(PIN_IN) == 1:
      GPIO.output(PIN_OUT, GPIO.HIGH)
    else:
      GPIO.output(PIN_OUT, GPIO.LOW)

    time.sleep(0.1)

# 終了時
except KeyboardInterrupt:
  GPIO.cleanup()
