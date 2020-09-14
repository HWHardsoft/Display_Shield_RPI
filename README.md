# Display_Shield_RPI
This smart OLED shield will extend your Raspberry Pi or Arduino with a grafic OLED display, 3 buttons und 3 additional LEDs. The shape fits exactely in our RasPiBox Open, RasPiBox Zero and ArduiBox Open din rail enclosure sets, but you can use it without these enclosure kits too. 

![My image](https://user-images.githubusercontent.com/3049858/93102304-9ea9f380-f6ab-11ea-8c89-3532b11c871a.jpg)

## Website
You will find more information about the Shield and the latest version of the code at
https://www.hwhardsoft.de/english/projects/display-shield/


# Electrical connection to Raspberry Pi

![My image](https://user-images.githubusercontent.com/3049858/93103461-f2690c80-f6ac-11ea-835f-230cc05cce68.png)


1. Download the [latest release](https://drive.google.com/open?id=1mo6LHWPsm_JBmMwiMcn8H-1lESI1KIQK)
2. Unzip the downloaded file
3. Write the image to your SD card. See [here](https://www.raspberrypi.org/documentation/installation/installing-images/README.md) for details.
4. Boot your Raspberry Pi and wait for WeatherPi_TFT to start.

# Configuration

##  Wifi settings
You can follow this [tutorial](https://www.raspberrypi.org/documentation/configuration/wireless/headless.md) to setting the Wifi headless. 

or you can use a Raspberry Pi (2/3/4) connected to Ethernet via Putty and SSH:
```bash
sudo raspi-config
--> 2 Network Options
--> N2 Wi-fi
``` 

## Localisation
```bash
sudo raspi-config
--> 4 Localisation Options
--> I1 Change Locale 
--> change your language ISO-8859-1 locales
``` 
Please note you can choose under 4 Localisation Options your time zones too!

## Weatherbit.io account
get an api key from weatherbit.io:

* go to [weatherbit.io](https://www.weatherbit.io/account/create)
* and register to get an API key
* choose the free version of the API


## Edit config file
```bash
cd
cd WeatherPi_TFT
sudo nano config.json
```
* replace `xxxxxxxxxxxxxxxxxxxxxxxxx` in  `"WEATHERBIT_IO_KEY": "xxxxxxxxxxxxxxxxxxxxxxxxx"` with your own API key
* replace `de` in `"WEATHERBIT_COUNTRY": "de"` with your country code
* replace `en` in `"WEATHERBIT_LANGUAGE": "en"` with your preferred language
* replace `10178` in `"WEATHERBIT_POSTALCODE": "10178"` with the postal (zip) code of your city (default loaction is Berlin)
* for language-support, please refer to -> **[Weather.io API Docs](https://www.weatherbit.io/api)**

reboot your Pizero!
```bash
sudo reboot
```

# Notes about 
Because the wiring of the TFT is different to the overlay rpi-display it was needed to recompile the original rpi-display overlay. You will find the changed source and the new compiled file here.

# License

This library is free software; you can redistribute it and/or
modify it under the terms of the GNU Lesser General Public
License as published by the Free Software Foundation; either
version 2.1 of the License, or (at your option) any later version.

This library is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
Lesser General Public License for more details.

