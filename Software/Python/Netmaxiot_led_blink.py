#!/usr/bin/env python



import time
from Netmaxiot import *

# Connect the Netmaxiot LED to digital port D4
led = 4

pinMode(led,"OUTPUT")
time.sleep(1)

print ("This example will blink a Netmaxiot LED connected to the Netmaxiot Shield on the port labeled D4.")
print (" ")
print ("Connect the LED to the port labele D4!" )
print ("this is a Arduino stye Example by Rohit Khosla-----------------:)")
time.sleep(5.0)
print "starts now "
while True:
    try:
        #Blink the LED
        digitalWrite(led,1)		# Send HIGH to switch on LED
        print ("LED ON!-----:)")
        time.sleep(1)

        digitalWrite(led,0)		# Send LOW to switch off LED
        print ("LED OFF!------:(")
        time.sleep(1)

    except KeyboardInterrupt:	# Turn LED off before stopping
        digitalWrite(led,0)
        print "you pressed Control + C byeeeee --:) "
        break
    except IOError:				# Print "Error" if communication error encountered
        print ("Error check shiled Connections and power to shield")
