# -*- coding: utf-8 -*-
"""udp_echo_client.ipynb

#UDP Echo Client
"""

import socket

#Define the Server Host (ip address) and Server Port Number(greater than 1024) of your Choice

srvr_host='client ip'
srvr_port=53135

#Create a Server Socket using socket() method and pass the IP Socket and the UDP socket inside the method as arguments

client_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#Now Send data to the Server

msg="Heyya! UDP Server Connected"
client_socket.sendto(msg.encode(),(srvr_host,srvr_port))

#Receive the data from the Server

rcvd_data, srvr_address=client_socket.recvfrom(1024)
print("Received:",rcvd_data.decode())

#Now Connection needs to be Closed by using close() method

client_socket.close()
