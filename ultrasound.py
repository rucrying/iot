import time
import grovepi

echo = 15
trig = 14
grovepi.pinMode(trig,'OUTPUT')
grovepi.pinMode(echo,'INPUT')
def send_pulse():
    grovepi.digitalWrite(trig,1)
    time.sleep(0.001)
    grovepi.digitalWrite(trig,0)
def wait_echo(boolean):
    while grovepi.digitalRead(echo) != boolean:
        continue
def get_dis():
    send_pulse()
    wait_echo(1)
    start = time.time()
    wait_echo(0)
    finish = time.time()
    return 170*(finish-start)*100
while True:
    print get_dis()
    time.sleep(0.5)
