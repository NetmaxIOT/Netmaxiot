#!/usr/bin/env python

# ____________________________________________________
# :) My  Single Analog Sensor  Netmaxiot Sensor  interfacing 
# Analog Example By NetmaxIOT  & Rohitkhosla
# OpenSource MIT licence by Netmax IOT Shield And Rohitkhosla
# :)
#----------------------------------------------------------------
import time
import Netmaxiot
#Analog Sensor connected to A0 Port of Netmax iot Shield :) 
sensor = 0		# Pin 0 is A0 Port.
while True:
	try:	
		sensor_value = Netmaxiot.analogRead(sensor)
		a=sensor_value*4.88
		b=a/1000
		print ("sensor_value = %0.2f volts "  %b)
		time.sleep(.5)
	except IOError:
		print ("Error")



