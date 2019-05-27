#!/usr/bin/env python
import Netmaxiot
try:
    print("Netmaxiot has firmware version: 2019.%s" %Netmaxiot.version())

except KeyboardInterrupt:
    print ("KeyboardInterrupt")
except IOError:
   print ("Error")

