#this script will be used for the display and what the OLED would display
#this script will only handle the graphics and the text, not the actual data
#the data will be handled by another script and then passed to this script for display

#ir is the variable that will hold the data from the IR sensor,
#the data will be passed to this script from the main script and then this script 
#will use the data to determine what to display on the OLED
from pickletools import dis

from machine import Pin, SoftI2C
import ssd1306

#define the variable for the ir sensor and define the measurements of the oled display 
#such that the width and height of the display are defined and can be used

dTolerance = 10000 #this variable will hold the tolerance value for the IR sensor, it will be used to determine if the finger is detected or not

# ---------------------------------- #
## Finger Detection ##
# ---------------------------------- #

if ir < dTolerance:
    print(oled.display("finger not detected"))
else:
    print(oled.display("finger detected"))
    time.sleep(3)
    oled.clear()
if ir >= 10000:
    print(oled.display("Good Reading"))
    time.sleep(3)
    oled.clear()
    print(oled.display("loading."))
    time.sleep(1)
    print(oled.display("loading.."))
    time.sleep(1)
    print(oled.display("loading..."))
    oled.clear()
else:
    print(oled.display("Bad Reading. Place finger closer to sensor"))

# ---------------------------------- #
## Heart Rate Detection graph ##
# ---------------------------------- #

# implementation of the live graph and the heart rate detection through
# the oled display and proper graphs and little heart symbol

#printing of the live graph of the heart rate detection.
