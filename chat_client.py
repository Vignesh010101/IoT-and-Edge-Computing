#Chat_client

import socket

#Define the Server Host (ip address) and Server Port Number(greater than 1024) of your Choice

srvr_host='client ip'
srvr_port=35791

#Create a Socket boject using socket() method and pass the ip Socket and the tcp socket inside the method as arguments

client_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#Now Initiate the Connection (Connect to the server) by using connect() method and pass the srvr_host, srvr_port as parameters to this method

client_socket.connect((srvr_host,srvr_port))

#Now We need to Send the Data to the Server


while True:
    msg = input("Me:")
    client_socket.sendall(msg.encode())
    
    srvr_msg = client_socket.recv(1024) #Now Receive the Data from the Server
    print("Receieved:",srvr_msg.decode())  #Print the Message

#Now Connection needs to be Closed by using close() method

client_socket.close()
