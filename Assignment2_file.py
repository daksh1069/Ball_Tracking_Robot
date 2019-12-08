# demo uart receive
import time
from bluetooth import ble

import util
from bleuartlib import BleUartDevice
count = 0
def bleUartReceiveCallback(data):
        if count%2==0:
            print('Received temp = {}'.format(data))
        if count%2!=0:
            print('Received lightlevel = {}'.format(data))
        count=count+1

def saveData(data1,data2)
        

try:

	bleUartDevice1 = None
	found_microbit = False

	service = ble.DiscoveryService()
	devices = service.discover(2)

	print('********** Initiating device discovery......')

	for address,name in devices.items():

		found_microbit = False

		if address == 'FC:B3:99:C7:0D:E9':

			print('Found BBC micro:bit [pegig]: {}'.format(address))
			found_microbit = True
			break

	if found_microbit:

		bleUartDevice1 = BleUartDevice(address)
		bleUartDevice1.connect()
		print('Connected to micro:bit device')
		data1 = bleUartDevice1.enable_uart_receive(bleUartReceiveCallback)
		print('Receiving temp...')
		data2 = bleUartDevice1.enable_uart_receive(bleUartReceiveCallback)
		print('Receiving lightlevel...')
		if aqString.Compare(data1,"fire",False):
                    count=0
		if aqString.Compare(data2,"fire",False):
                    count=1
		saveData(data1,data2)
		while True:
                    time.sleep(0.1)

except KeyboardInterrupt:
	
	print('********** END')
	
except Error as err:

	print('********** ERROR: {}'.format(err))

finally:

	if bleUartDevice1 != None:
		bleUartDevice1.disconnect()
		bleUartDevice1 = None
		print('Disconnected from micro:bit device')

