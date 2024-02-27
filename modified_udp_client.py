#UDP Client

import socket

#Define the Server Host (ip address) and Server Port Number(greater than 1024) of your Choice

srvr_host='10.114.27.246'
srvr_port=53135

#Create a Server Socket using socket() method and pass the IP Socket and the UDP socket inside the method as arguments

client_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

while True:
    #Now Send data to the Server

    msg=input("Me:")
    client_socket.sendto(msg.encode(),(srvr_host,srvr_port))
    
    if msg=='end':
        print("Connection Ended by You")
        break

    #Receive the data from the Server
    rcvd_data, srvr_address=client_socket.recvfrom(1024)
    print("Received:",rcvd_data.decode())

#Now Connection needs to be Closed by using close() method

client_socket.close()