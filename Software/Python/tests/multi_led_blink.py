#!/usr/bin/env python

# :) my Led Blink Test 
# Analog Sensor Example By NetmaxIOT  & Rohitkhosla
# OpenSource MIT licence by Netmax IOT Shield And Rohitkhosla
# :)

import time
from Netmaxiot import *

# Connect the Netmaxiot LED to digital port D4,D5,D6
led0 = 4
led1 = 5
led2 = 6

pinMode(led0,"OUTPUT")
pinMode(led1,"OUTPUT")
pinMode(led2,"OUTPUT")

while True:
    try:
        #Blink the LED
        digitalWrite(led0,1)		# Send HIGH to switch on LED
        digitalWrite(led1,1)		# Send HIGH to switch on LED
        digitalWrite(led2,1)		# Send HIGH to switch on LED
        print ("LED ON!")
        time.sleep(1)

        digitalWrite(led0,0)		# Send LOW to switch off LED
        digitalWrite(led1,0)		# Send LOW to switch off LED
        digitalWrite(led2,0)		# Send LOW to switch off LED
        print ("LED OFF!")
        time.sleep(1)

    except IOError:				# Print "Error" if communication error encountered
        print ("Error")
