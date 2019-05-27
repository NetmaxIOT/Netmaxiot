#!/usr/bin/env python
#
# :) my Digital Sensor Test 
# Digital Sensor Example By NetmaxIOT  & Rohitkhosla
# OpenSource MIT licence by Netmax IOT Shield And Rohitkhosla
# :)

import time
import Netmaxiot

button2 = 2
button3 = 3
button4 = 4

Netmaxiot.pinMode(button2,"INPUT")
Netmaxiot.pinMode(button3,"INPUT")
Netmaxiot.pinMode(button4,"INPUT")
while True:
	try:
		d2=Netmaxiot.digitalRead(button2)
		d3=Netmaxiot.digitalRead(button3)
		d4=Netmaxiot.digitalRead(button4)
		print ("%d,%d,%d" %(d2,d3,d4))
	except IOError:
		print ("Error")
