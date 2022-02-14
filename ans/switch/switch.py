import RPi.GPIO as GPIO
import time
import sys

#ポート番号の定義
Sw_pin = 4

#GPIOの設定
GPIO.setmode(GPIO.BCM)
GPIO.setup(Sw_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

while True:
    try:
        print(GPIO.input(Sw_pin))           #ONで"1" OFFで"0"
        time.sleep(1)                       #待つ
    except KeyboardInterrupt:
        GPIO.cleanup()
        sys.exit()
