import time
from gc_CRUD import gcWrite

import pigpio
import DHT22

pi = pigpio.pi()
s = DHT22.sensor(pi,4)


while True:

    if int(time.strftime("%M")) % 5 == 0 and int(time.strftime("%S")) == 0:

        s.trigger()
        time.sleep(0.05)
        t = s.temperature()
        h = s.humidity()

        i = time.strftime("%y:%m:%d %H:%M")

        gcWrite('Joe`s office ', t, h, i)
        print("Written to firebase")
