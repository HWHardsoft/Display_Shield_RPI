#!/usr/bin/python Copyright 2020 Zihatec GmbH, www.zihatec.de
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions: The above copyright notice and this
# permission notice shall be included in all copies or substantial
# portions of the Software. THE SOFTWARE IS PROVIDED "AS IS", WITHOUT
# WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO
# THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE
# AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
# HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
# IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR
# IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


from luma.core.interface.serial import i2c, spi
from luma.core.render import canvas
from luma.oled.device import sh1106
from PIL import Image, ImageFont

import smbus
import sys
import time
#import os.path


#*********************************************************************
# Configuration MCP23008
#*********************************************************************
bus = smbus.SMBus(1) # For revision 1 Raspberry Pi, change to bus = smbus.SMBus$
bus.write_byte_data(0x20,0x00,0x0F) # Set all port directions
bus.write_byte_data(0x20,0x06,0x0F) # Set pull-ups for button inputs


#*********************************************************************
# Configuration SH1106
#*********************************************************************
serial = i2c(port=1, address=0x3C)
device = sh1106(serial)

# Load image 128x64
image = Image.open('RasPiBox.ppm').convert('1') 


# print intro text
with canvas(device) as draw:
    draw.text((10, 5), "Display Shield", fill="white")
    draw.text((10, 28), "www.zihatec.de", fill="white")
    draw.text((10, 48), "Press a key!", fill="white")

def main():
    # read the status of the 3 buttons
    button_state = bus.read_byte_data(0x20,0x09)

    if ((button_state & 0x01) == 0): # S1 pressed?
        print ("S1 pressed")
        bus.write_byte_data(0x20,0x09,0x90) # set  LED D1 and beeper on

        # shows RasPiBox logo
        device.display(image)

        time.sleep(1)


    if ((button_state & 0x02) == 0): # S2 pressed?
        print ("S2 pressed")
        bus.write_byte_data(0x20,0x09,0x20) # set  LED D2 on

        with canvas(device) as draw:
            # show different polygons
            # Draw an ellipse.
            draw.ellipse((2, 15, 35, 45), outline=255, fill=255)

            # Draw a rectangle.
            draw.rectangle((50, 2, 90, 62), outline=255, fill=0)

            # Draw a triangle.
            draw.polygon([(100, 62), (110, 2), (120, 62)], outline=255, fill=64)

        time.sleep(1)




    if ((button_state & 0x04) == 0): # S3 pressed?
        print ("S3 pressed")
        bus.write_byte_data(0x20,0x09,0x40) # set  LED D3 on

        with canvas(device) as draw:
            # Load default font.
            font = ImageFont.load_default()

            # Write 3 lines of text.
            draw.text((5, 2), 'The quick brown fox', font=font, fill=255)
            draw.text((5, 22), 'jumps over the lazy', font=font, fill=255)
            draw.text((5, 42), 'dog.  1234567890', font=font, fill=255)

        time.sleep(1)
 

    bus.write_byte_data(0x20,0x09,0x00) # set  LEDs & beeper off





# endless loop
if __name__ == '__main__':
    while (True):
        main()


