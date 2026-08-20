from machine import Pin, SoftI2C
import ssd1306
from max30102 import MAX30102
import time

# Setup I2C (both share the same bus)
i2c = SoftI2C(scl=Pin(9), sda=Pin(8))

# Setup OLED
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

# Setup MAX30102
sensor = MAX30102(i2c=i2c)
sensor.setup_sensor()

