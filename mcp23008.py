#! /usr/bin/python

# A simple Python command line tool to control an MCP23017 I2C IO Expander
# By Nathan Chantrell http://nathan.chantrell.net
# GNU GPL V3 

import smbus
import sys
import time

 
bus = smbus.SMBus(1) # For revision 1 Raspberry Pi, change to bus = smbus.SMBus(1) for revision 2.

#address = 0x20 # I2C address of MCP23017
bus.write_byte_data(0x20,0x00,0x07) # Set all port directions



def main():
    bus.write_byte_data(0x20,0x09,0x10)
    time.sleep(1)
    bus.write_byte_data(0x20,0x09,0x00)
    time.sleep(1)

# endless loop
# print "(CTRL+C to quit)"
while (True):
    main()



