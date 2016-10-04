#!/usr/bin/env python
import time
import serial
import threading
# open UART port 
port = serial.Serial(
               port='/dev/ttyS0',
               baudrate = 9600,
               parity=serial.PARITY_NONE,
               stopbits=serial.STOPBITS_ONE,
               bytesize=serial.EIGHTBITS,
               timeout=1
           )



# Uart Read from port method
def uartRead(port,runEvent):
	print "Uart Read Thread running"
	while runEvent.is_set(): 
		x = readlineCR(port)	
		if(x):
			print x

# Uart Write method
def uartWrite(String):
	if (String):
		port.write(String)


# Support read function  
def readlineCR(port):
	rv = ""
	while True:
		ch = port.read()
		rv += ch
		if ch=='\r' or ch=='':
			return rv

def main():
	runEvent = threading.Event()
	runEvent.set()

	readThread= threading.Thread(target=uartRead, args=(port,runEvent))
	readThread.start()

	try:
		while 1:
			time.sleep(.1)
	except KeyboardInterrupt:
		print " Attemping to close main threads and others."
		runEvent.clear()
		readThread.join()
		print "Threads sucessfully closed"


if __name__== '__main__':
	main()
