# -*- coding: utf-8 -*-
"""
Created on Tue Feb  5 16:38:36 2019

@author: ggebr
"""

import socket
target_host ="www.google.com"
 
target_port = 80
#create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# connect to the client
client.connect((target_host, target_port))
#send data
#client.send("GET / HTTP/1.1\r\n\Host:google.com\r\n\r\n")
#c= b'GET / HTTP/1.1\r\n\Host:google.com\r\n\r\n'
c= b'GET / HTTP/1.1\r\n\Host:google.com\r\n\r\n'
client.send(c)
#receive some data
response = client.recv(4096)
print(response)