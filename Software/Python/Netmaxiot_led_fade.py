#!/usr/bin/env python


import time
import Netmaxiot
led = 5
Netmaxiot.pinMode(led,"OUTPUT")
time.sleep(1)
i = 0
while True:
    try:
        # Reset
        if i > 255:
            i = 0

        # Current brightness
        print (i)

        # Give PWM output to LED
        Netmaxiot.analogWrite(led,i)

        # Increment brightness for next iteration
        i = i + 10
        time.sleep(.2)

    except KeyboardInterrupt:
        Netmaxiot.analogWrite(led,0)
        break
    except IOError:
        print ("Error")