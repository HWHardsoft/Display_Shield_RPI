# Display_Shield_RPI
This smart OLED shield will extend your Raspberry Pi or Arduino with a grafic OLED display, 3 buttons und 3 additional LEDs. The shape fits exactely in our RasPiBox Open, RasPiBox Zero and ArduiBox Open din rail enclosure sets, but you can use it without these enclosure kits too. 

![My image](https://user-images.githubusercontent.com/3049858/93102304-9ea9f380-f6ab-11ea-8c89-3532b11c871a.jpg)

## Website
You will find more information about the Shield and the latest version of the code at
https://www.hwhardsoft.de/english/projects/display-shield/


# Electrical connection to Raspberry Pi

![My image](https://user-images.githubusercontent.com/3049858/93103461-f2690c80-f6ac-11ea-835f-230cc05cce68.png)


# Installation
Before using the library you will need to make sure you have a few dependencies installed. Connect to your device using SSH and follow the steps below.

## I2C
First you have to enable the I2C port of the Raspberry PI:

```bash
sudo raspi-config
--> 5 Interfacing Options
--> P5 I2C
--> Would you like the ARM I2C interface to be enabled? --> Yes
sudo reboot
``` 

Now you have to install the I2C tools:
```bash
sudo apt-get install i2c-tools -y
``` 

Now you can test the I2C interface:
```bash
i2cdetect -y 1
``` 
![My image]()

0x3C is the address of the SH1106 controller and 0x20 is the address of the MCP23008


## Install Python3, PIP3 ...
Now you have to install Python3, PIP3, some dependencies and the luma library for SH1106 display controller:
```bash
sudo apt install python3-dev python3-pip libfreetype6-dev libjpeg-dev buildessential libopenjp2-7 libtiff5
sudo -H pip3 install --upgrade luma.oled
``` 

## MCP23008
For the MCP23008 we have to install the smbus library too:
```bash
sudo pip3 install smbus
``` 

## Install the demo code from GITHUB
Now to download and install the demo code for the display shield, execute the following commands:
```bash
cd ..
git clone https://github.com/hwhardsoft/Display_Shield_RPI.git
cd Display_Shield_RPI
``` 

to run the demo enter for the standard version:
sudo python3 display_shield.py

Press the 3 buttons to view different screens!


# License

This library is free software; you can redistribute it and/or
modify it under the terms of the GNU Lesser General Public
License as published by the Free Software Foundation; either
version 2.1 of the License, or (at your option) any later version.

This library is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
Lesser General Public License for more details.

