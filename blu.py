from bluetooth import *
port = 1
bd_addr= "98:D3:31:30:76:01"
datatemp = 'C'
ip = "192.168.6.26"

import requests


while(1):

	try:
		sock = BluetoothSocket(RFCOMM)
		sock.connect((bd_addr, port))
		print("init")
		conn = 1
	except BluetoothError as bt:
		print('cannot connect to host' + str(bt))
		exit(0)
	while(1):	
		try:
			buf = sock.recv(1)
		except BluetoothError as err:
			print("Blu err on rec")
			break
		if len(buf) > 0:
			if datatemp != str(buf):
			request.get('http://' + ip + ':8085/door?status='+buf)					
		
			datatemp = str(buf)
			print(datatemp)
