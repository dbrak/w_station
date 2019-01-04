#!/usr/bin/env python

import pigpio 
import sys
sys.path.append('/home/pi/PIGPIO')
import DHT22

#instantiate pi and sensor objects
pi = pigpio.pi()
s = DHT22.sensor(pi,4)

#Take reading and write values to variable
for x in range (0,1000):
	s.trigger()
	h = s.humidity()
	t = s.temperature()
	print(h)
	print(t)
