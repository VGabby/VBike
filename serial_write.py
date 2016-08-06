#!/usr/bin/env python
import time
import serial
port = serial.Serial(
               port='/dev/ttyS0',
               baudrate = 9600,
               parity=serial.PARITY_NONE,
               stopbits=serial.STOPBITS_ONE,
               bytesize=serial.EIGHTBITS,
               timeout=1
           )
raw_input('Enter your message:')
while True: 
#	port.write("\r\nSay something")
#	rcv = port.read(10)
#	port.write("\r\nYou sent:" + repr(rcv))
	x = raw_input()
	if( x ):
		port.write("send:" + repr(x))
