#chat_Server

import socket

#Define the Server Host (ip address) and Server Port Number(greater than 1024) of your Choice

srvr_host='srvr ip'
srvr_port=35791

#Create a Server Socket using socket() method and pass the IP Socket and the TCP socket inside the method as arguments

srvr_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#Now we need to Bind the Socket by using bind() method

srvr_socket.bind((srvr_host,srvr_port))

#Now we need to Listen to the Incoming Connections

srvr_socket.listen(1)
print("[*] Listening on ",srvr_host,":",srvr_port)

#Now Accept a Client Connection by using accept() method
while True:
    client_socket, client_address=srvr_socket.accept()
    print("[*] Accepted Connection from ", client_address[0],":",client_address[1])
    
    while True:
        #Start Receiving the Data from the Client by using recv() method
        data=client_socket.recv(1024)
        if not data:
            break
        print("Received:",data.decode())
        
        reply=input("Your Reply:")
        client_socket.sendall(reply.encode())
    #We need to Send the Received data back to the Client by using sendall() method
    print("Convo ended")
    client_socket.close()

#Now the Connection needs to be Closed
client_socket.close()
srvr_socket.close()
