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


import Adafruit_SSD1306

import smbus
import time

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


if __name__ == '__main__':
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
 
    i1 = 5

    # endless loop 
    print "(CTRL+C to quit)"
    while (True):
        if (i1 < 2):
            i1 = i1 + 1
        else:
            i1 = 0
            
        
        if (i1 == 0):	
            print "show an image"
			
            # Clear display.
            disp.clear()

            # Load image 128x64 
            image = Image.open('RasPiBox.ppm').convert('1')

            # Display image.
            disp.image(image)
            disp.display()
            
	    
        elif (i1 == 1):	
            print "demo of text output"

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
            print "drawing some shapes"             
 
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
            
        
        time.sleep(2)
