#!/usr/bin/env python
# :) my Analog Sensor 
# Analog Sensor Example By NetmaxIOT  & Rohitkhosla
# OpenSource MIT licence by Netmax IOT Shield And Rohitkhosla
# :)
import time
import Netmaxiot
from time import sleep
#Sensor connected to A0,A1,A2 Port 
sensor0 = 0		 
sensor1 = 1		 
sensor2 = 2		 

while True:
    try:
        sensor_value0 = Netmaxiot.analogRead(sensor0)
        sensor_value1 = Netmaxiot.analogRead(sensor1)
        sensor_value2 = Netmaxiot.analogRead(sensor2)
        sleep (3.0)
        print (" ")
        print ("Analog Channel(1) ==%d"%(sensor_value0 ))
        print ("Analog Channel(2) ==%d"%(sensor_value1 ))
        print ("Analog Channel(3) ==%d"%(sensor_value2 ))
        print (" ")
        print ("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    except IOError:
        print ("Error please check you Netmax IOT Shiled and Sensors ")
