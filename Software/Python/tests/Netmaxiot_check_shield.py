#!/usr/bin/env python

#
# NOTE: If you get a version of 255.255.255, they try running the script again, 
#if the issue still persists then your Netmax iot shield ic is not working properly

import Netmaxiot

try:
    print " "
    print " "
    print " "
    print " "
    print " "
    print " "
    print "------------------------------------------------------------------"
    print("Netmaxiot Shield has firmware version:-==2.%s" %Netmaxiot.version())
    print " "
    print "--------------------------------------------------------------------"
    print "################################################################### "
    print " "
    print " "


except KeyboardInterrupt:
    print ("KeyboardInterrupt")
except IOError:
   print ("Error")
