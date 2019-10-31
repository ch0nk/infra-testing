#!/usr/bin/env python

import socket
import sys

def check_server(address, port):
	# Create a socket
	s = socket.socket()
	print("Attempting to connect to ", address, "on port ", port)
	try:
		s.connect((address, port))
		print("Connected to ", address, "on port ", port)
		return True
	except socket.error as e:
		print("Connection to ", address, "on port ", port, "failed: ", e)
		return False

if __name__ == '__main__':
	from optparse import OptionParser
	parser = OptionParser()

	parser.add_option("-a", "--address", dest="address", default='localhost', help="ADDRESS for server", metavar="ADDRESS")

	parser.add_option("-p", "--port", dest="port", type="int", default=80, help="PORT for server", metavar="PORT")

	(options, args) = parser.parse_args()
	print('options: ', options, 'args: ', args)
	check = check_server(options.address, options.port)
	print('check_server returned ', check)

	sys.exit(not check)