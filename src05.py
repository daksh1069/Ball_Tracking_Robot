# demo uart receive



import time
from bluetooth import ble

import util
from bleuartlib import BleUartDevice



def bleUartReceiveCallback(data):

	print('Received data = {}'.format(data))



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
		
		data = bleUartDevice1.enable_uart_receive(bleUartReceiveCallback)
		print('Receiving data...')

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
