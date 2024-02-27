#UDP Server

import socket

#Define the Server Host (ip address) and Server Port Number(greater than 1024) of your Choice

srvr_host='10.114.27.246'
srvr_port=53135

#Create a Server Socket using socket() method and pass the IP Socket and the UDP socket inside the method as arguments

srvr_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#Now we need to Bind the Socket to the address and port by using bind() method
srvr_socket.bind((srvr_host,srvr_port))
print("[*] Listening on ",srvr_host,":",srvr_port)

while True:
    # Start Receiving Data and Address from the client
    data, address=srvr_socket.recvfrom(1024)
    
    if data.decode()=='end':
        print("Connection Ended")
        break
    
    print("Received:",data.decode())
    
    reply=input()
    srvr_socket.sendto(reply.encode(), address)

   
   

      

