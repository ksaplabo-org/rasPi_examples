# インポート
import RPi.GPIO as GPIO
import time

#ポート番号の定義
SW_PIN = 4

#GPIOの設定
GPIO.setmode(GPIO.BCM)
GPIO.setup(SW_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

try:
  while True:
    print(GPIO.input(SW_PIN))   #ONで"1" OFFで"0"
    time.sleep(1)             #待つ

except KeyboardInterrupt:
  GPIO.cleanup()
