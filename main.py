"""
Coyt Barringer - 2020

Test program demonstrating data transmission between Adafruit Bluefruit BLE libraries running 
on nrf52840 and Python

This uses the Nordic Uart Service (NUS) and should work concurrently with other BLE services such as HID

On the python side, the Bluetooth Low Energy platform Agnostic Klient for Python (Bleak) project
is used for Cross Platform Support and has been tested with windows 10

"""

import platform
import logging
import asyncio
from bleak import BleakClient
from bleak import BleakClient
from bleak import _logger as logger
from bleak.uuids import uuid16_dict


UART_TX_UUID = "6e400002-b5a3-f393-e0a9-e50e24dcca9e" #Nordic NUS characteristic for TX
UART_RX_UUID = "6e400003-b5a3-f393-e0a9-e50e24dcca9e" #Nordic NUS characteristic for RX

dataFlag = False #global flag to check for new data


def notification_handler(sender, data):
    """Simple notification handler which prints the data received."""
    print("{0}: {1}".format(sender, data))
    global dataFlag
    dataFlag = True


async def run(address, loop):

    async with BleakClient(address, loop=loop) as client:

        #wait for BLE client to be connected
        x = await client.is_connected()
        print("Connected: {0}".format(x))

        #wait for data to be sent from client
        await client.start_notify(UART_RX_UUID, notification_handler)


        while True : 

            #give some time to do other tasks
            await asyncio.sleep(0.01)

            #check if we received data
            global dataFlag
            if dataFlag :
                dataFlag = False

                #echo our received data back to the BLE device
                data = await client.read_gatt_char(UART_RX_UUID)
                await client.write_gatt_char(UART_TX_UUID,data)


if __name__ == "__main__":

    #this is MAC of our BLE device
    address = (
        "E6:8C:5E:4D:AC:99"
    )

    loop = asyncio.get_event_loop()
    loop.run_until_complete(run(address, loop))