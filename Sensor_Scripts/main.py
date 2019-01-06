import time
from gc_CRUD import gcWrite

import pigpio
import DHT22

pi = pigpio.pi()
s = DHT22.sensor(pi, 4)

while True:

    t = time.gmtime()
    ts = int(time.strftime('%S', t))
    tm = int(time.strftime('%M', t))

    if (tm % 5 == 0) and (ts == 0):
        s.trigger()
        time.sleep(0.03)
        t = s.temperature()
        h = s.humidity()

        i = time.strftime("%y:%m:%d %H:%M")

        gcWrite('Joe`s Office', t, h, i)
        print(tm, ts, "|", i, "|", time.strftime("%H:%M:%S"))
