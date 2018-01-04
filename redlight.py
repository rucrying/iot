import grovepi
import time

pin = 14
grovepi.pinMode(pin,"INPUT")

while True:
    value = grovepi.analogRead(pin)
    print value
    time.sleep(0.1)
