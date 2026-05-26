#this script will be used for the display and what the OLED would display
#this script will only handle the graphics and the text, not the actual data
#the data will be handled by another script and then passed to this script for display

#ir is the variable that will hold the data from the IR sensor,
#the data will be passed to this script from the main script and then this script 
#will use the data to determine what to display on the OLED
from pickletools import dis

import oled #this will work as the library for the OLED display, it will have functions to display text and graphics on the OLED
import ir #this will work as the library for the IR sensor, it will have functions to read data from the IR sensor

#define the variable for the ir sensor and define the measurements of the oled display 
#such that the width and height of the display are defined and can be used

dTolerance = 10000 #this variable will hold the tolerance value for the IR sensor, it will be used to determine if the finger is detected or not

if ir < dTolerance:
    print(oled.display("finger not detected"))
else:
    print(oled.display("finger detected"))

