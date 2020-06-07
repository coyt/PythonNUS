# PythonNUS
Example of cross platform data transmission between Nordic UART Service (NUS) and Python using the Bleak Project and Adafruit nrf52 Libraries

Unlike the [Adafruit BLE Desktop application](https://github.com/adafruit/adafruit-bluefruit-le-desktop) which is limited on windows to certain hardware BLE adapters, the use of [Bleak](https://github.com/hbldh/bleak) allows improved connectivity by supporting "Windows 10, version 16299 (Fall Creators Update) or greater"

#### Overview

Quick Test program demonstrating data transmission between Adafruit Bluefruit BLE libraries running on a nrf52840 development board and Python running on a Windows 10 PC

The Python program simply awaits a BLE connection from a hardware device, and echoes back any received data. 

This uses the Nordic Uart Service (NUS) and should work concurrently with other BLE services such as HID allowing cool features for devices such as BLE keyboards to communicate data over an additional channel - possibly to update configs during runtime, etc...

On the nrf52840 side - run this [Adafruit example code](https://github.com/adafruit/Adafruit_nRF52_Arduino/blob/master/libraries/Bluefruit52Lib/examples/Peripheral/bleuart/bleuart.ino)

On the python side, the Bluetooth Low Energy platform Agnostic Klient for Python (Bleak) project is used for Cross Platform Support and has been tested with windows 10

