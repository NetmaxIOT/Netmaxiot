#!/usr/bin/env python

import time
import Netmaxiot

button2 = 2
button3 = 3
button4 = 4
sensor0 = 0		 
sensor1 = 1		 
sensor2 = 2	

Netmaxiot.pinMode(button2,"INPUT")
Netmaxiot.pinMode(button3,"INPUT")
Netmaxiot.pinMode(button4,"INPUT")

while True:
	try:
		print time.time(),
		d2=Netmaxiot.digitalRead(button2)
		d3=Netmaxiot.digitalRead(button3)
		d4=Netmaxiot.digitalRead(button4)
		sensor_value0 = Netmaxiot.analogRead(sensor0)
		sensor_value1 = Netmaxiot.analogRead(sensor1)
		sensor_value2 = Netmaxiot.analogRead(sensor2)
		print ("%d,%d,%d" %(d2,d3,d4)),
		print ("%d,%d,%d" %(sensor_value0,sensor_value1,sensor_value2))
	except IOError:
		print ("Error")
