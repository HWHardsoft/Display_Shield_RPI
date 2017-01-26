#!/usr/bin/python

# Copyright 2017 Hartmut Wendt, www.hwhardsoft.de
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of
# this software and associated documentation files (the "Software"), to deal in
# the Software without restriction, including without limitation the rights to
# use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
# of the Software, and to permit persons to whom the Software is furnished to do
# so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import Adafruit_GPIO as GPIO
import Adafruit_GPIO.I2C as I2C
import Adafruit_GPIO.MCP230xx as MCP
import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306

import smbus
import time

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


if __name__ == '__main__':
    # ***************************************************
    # Set i2c parameters for MCP23008
    # ***************************************************
    mcp = MCP.MCP23008(address = 0x20, busnum = 1) # MCP23008

    # Set pins 0, 1 and 2 to input (pull up enabled) for push buttons
    mcp.setup(0, GPIO.IN)
    mcp.setup(1, GPIO.IN)
    mcp.setup(2, GPIO.IN)
    mcp.pullup(0, 1)
    mcp.pullup(1, 1)
    mcp.pullup(2, 1)	

    # Set pins 4, 5 and 6 to output for leds
    mcp.setup(4, GPIO.OUT)
    mcp.setup(5, GPIO.OUT)
    mcp.setup(6, GPIO.OUT)	

    # ***************************************************
    # Initialisation of the OLED Display
    # ***************************************************

    # Raspberry Pi pin configuration:
    RST = 24 
    
    # 128x64 display with hardware I2C:
    disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST)

    # Initialize library.
    disp.begin()

    # Clear display.
    disp.clear()
    disp.display()
 
    # endless loop 
    print "(CTRL+C to quit)"
    while (True):
        if (mcp.input(0) == GPIO.LOW):	# S1 pressed?
            print "S1 pressed"
            print "show an image"
            mcp.output(4, 1) # set LED D1 on
			
            # Clear display.
            disp.clear()

            # Load image 128x64 
            image = Image.open('RasPiBox.ppm').convert('1')

            # Display image.
            disp.image(image)
            disp.display()
            
			
        else:
            mcp.output(4, 0) # set LED D1 off
	    
        if (mcp.input(1) == GPIO.LOW):	# S2 pressed?
            print "S2 pressed"
            print "demo of text output"
            mcp.output(5, 1) # set LED D2 on

            # Clear display.
            disp.clear()

            # Create blank image for drawing.
            # Make sure to create image with mode '1' for 1-bit color.
            width = disp.width
            height = disp.height
            image = Image.new('1', (width, height))

            # Get drawing object to draw on image.
            draw = ImageDraw.Draw(image)             
            
            # Load default font.
            font = ImageFont.load_default()

            # Alternatively load a TTF font.  Make sure the .ttf font file is in the same directory as the python script!
            # Some other nice fonts to try: http://www.dafont.com/bitmap.php
            #font = ImageFont.truetype('Minecraftia.ttf', 8)

            # Write 3 lines of text.
            draw.text((5, 2),  'The quick brown fox',  font=font, fill=255)
            draw.text((5, 22), 'jumps over the lazy', font=font, fill=255)
            draw.text((5, 42), 'dog.     1234567890',  font=font, fill=255)

            # Display image.
            disp.image(image)
            disp.display()
			
        else:
            mcp.output(5, 0) # set LED D2 off
	
        if (mcp.input(2) == GPIO.LOW):	# S3 pressed?
            print "S3 pressed"
            print "drawing some shapes" 
            mcp.output(6, 1) # set LED D3 on
 
            # Clear display.
            disp.clear()

            # Create blank image for drawing.
            # Make sure to create image with mode '1' for 1-bit color.
            width = disp.width
            height = disp.height
            image = Image.new('1', (width, height))

            # Get drawing object to draw on image.
            draw = ImageDraw.Draw(image)             
            x = 2
            # Draw an ellipse.
            draw.ellipse((x, 2, x+40, 62), outline=255, fill=0)
            x = 50
            # Draw a rectangle.
            draw.rectangle((x, 2, x+40, 62), outline=255, fill=0)
            x = 100
            # Draw a triangle.
            draw.polygon([(x, 62), (x+10, 2), (x+20, 62)], outline=255, fill=0)
            
            # Display image.
            disp.image(image)
            disp.display()
            
        else:
            mcp.output(6, 0) # set LED D3 off
        
        # time.sleep(1)
