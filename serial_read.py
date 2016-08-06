#!/usr/bin/env python
import time
import serial

def readlineCR(port):
	rv = ""
	while True:
		ch = port.read()
		rv += ch
		if ch=='\r' or ch=='':
			return rv

port = serial.Serial(
               port='/dev/ttyS0',
               baudrate = 9600,
               parity=serial.PARITY_NONE,
               stopbits=serial.STOPBITS_ONE,
               bytesize=serial.EIGHTBITS,
               timeout=1
           )

while True: 
#	x = port.readline()
	x = readlineCR(port)	
	if(x):
		print x

