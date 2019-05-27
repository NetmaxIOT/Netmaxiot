#!/usr/bin/env python


import time
import Netmaxiot

# Connect the Netmaxiot Light Sensor to analog port A0
# SIG,NC,VCC,GND
light_sensor = 0

# Connect the LED to digital port D4
# SIG,NC,VCC,GND
led = 4

# Turn on LED once sensor exceeds threshold resistance
threshold = 10

Netmaxiot.pinMode(light_sensor,"INPUT")
Netmaxiot.pinMode(led,"OUTPUT")

while True:
    try:
        # Get sensor value
        sensor_value = Netmaxiot.analogRead(light_sensor)

        # Calculate resistance of sensor in K
        resistance = (float)(1023 - sensor_value) * 10 / sensor_value

        if resistance > threshold:
            # Send HIGH to switch on LED
            Netmaxiot.digitalWrite(led,1)
        else:
            # Send LOW to switch off LED
            Netmaxiot.digitalWrite(led,0)

        print("sensor_value = %d resistance =%.2f" %(sensor_value,  resistance))
        time.sleep(.5)

    except IOError:
        print ("Error")
