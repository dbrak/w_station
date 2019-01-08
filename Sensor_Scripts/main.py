import time
from gc_CRUD import gcWrite
from schedule import every
import json
import pigpio
import DHT22

def main():
    with open('config.json','r') as f:
        config = json.load(f)

    pi = pigpio.pi()
    s = DHT22.sensor(pi, 4)

    t = time.gmtime()
    ts = int(time.strftime('%S', t))
    tm = int(time.strftime('%M', t))

    if (tm % 5 == 0) and (ts == 0):
        s.trigger()
        time.sleep(0.03)
        t = s.temperature()
        h = s.humidity()

        i = time.strftime("%y:%m:%d %H:%M")

        gcWrite(config['location'], t, h, i)
        print(tm, ts, "|", i, "|", time.strftime("%H:%M:%S"))

while True:
    every(5).minutes.do(main())
