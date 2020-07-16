#!/bin/python3

import sys
import socket
from datetime import datetime as dt


#Defining our target

if len(sys.argv) == 2:
	target = socket.gethostbyname(sys.argv[1]) #translate hostname to ipv4
else: 
	print("Invalid number of arguments.")
	print("Syntax: python3 scanner.py <ip>")
	sys.exit

#adding a cool banner
print("-" * 50)
#format to insert the ip
print("Scanning target {}    <--".format(target))
#print("Scanning target " + target )
print("Time started : " + str(dt.now()))
print("-" * 50)

try :
	for port in range(50,85):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#af_inet is ipv4 stream is port
		socket.setdefaulttimeout(1) #should be a float
		result = s.connect_ex((target, port)) #return error indicator (0 is no error)
		print("chekcing port")
		if result == 0: #if we got no error we print the port 
			print("Port {} is open".format(port))
		s.close()


#all exception that can occur : ctrl + c / ip / socket error
except KeyboardInterrupt :
	print("\n Exiting program.")
	sys.exit()
except socket.gaierror :
	print("Hostname could not be resolved.")
	sys.exit()
except socket.error :
	print("Couldn't connect to server")
	sys.exit()

