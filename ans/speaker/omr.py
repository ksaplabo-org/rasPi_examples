# only my railgun

import RPi.GPIO as GPIO
import time

speaker = 21

def alert(pin, hz, sleep):
  alert = GPIO.PWM(pin, hz)
  alert.start(50)
  time.sleep(sleep)
  alert.stop()

GPIO.setmode(GPIO.BCM)
GPIO.setup(speaker, GPIO.OUT)

code = [
  [1975.533, 0.2],
  [1760.000, 0.15],
  [1396.913, 0.15],
  [1396.913, 0.2],
  [1567.982, 0.15],
  [1567.982, 0.2],
  [1567.982, 0.2],
  [1396.913, 0.15],
  [1396.913, 0.2],
  [1567.982, 0.15],
  [1567.982, 0.2],
  [1567.982, 0.2],
  [1396.913, 0.15],
  [1396.913, 0.2],
  [1567.982, 0.15],
  [1567.982, 0.2],
  [1567.982, 0.15],
  [1567.982, 0.15],
  [1567.982, 0.2],
  [1760.000, 0.2],
  [1975.533, 0.2],
  [2093.005, 0.3],
  [1760.000, 0.4],
  [1396.913, 0.4],
  [2637.020, 0.4],
  [2093.005, 0.4],
  [2093.005, 0.3],
  [2093.005, 0.2],
  [2349.318, 0.8]
]

try:
  for audio in code:
    alert(speaker, audio[0], audio[1])
    time.sleep(0.02)

except KeyboardInterrupt:
  GPIO.cleanup()
