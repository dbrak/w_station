import time
from gc_CRUD import gcWrite
import schedule
import json
import pigpio
import DHT22

ti = time.gmtime()
ts = int(time.strftime('%S', ti))
tm = int(time.strftime('%M', ti))


def main():
    with open('config.json', 'r') as f:
        config = json.load(f)

    pi = pigpio.pi()
    s = DHT22.sensor(pi, 4)

    s.trigger()
    time.sleep(0.03)
    t = s.temperature()
    h = s.humidity()

    i = time.strftime("%y:%m:%d %H:%M")

    gcWrite(config['location'], t, h, i)
    print(tm, ts, "|", i, "|", time.strftime("%H:%M:%S"))

t = ["5","10","15","20","25","30","35","40","45","50","55","60"]

while True:
    schedule.every().mhours.at(t).do(main())
