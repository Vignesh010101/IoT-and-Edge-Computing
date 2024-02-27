#Server

import socket

srvr_host = 'server ip'
srvr_port = 35791

srvr_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
srvr_socket.bind((srvr_host, srvr_port))
srvr_socket.listen(1)
print("[*] Listening on", srvr_host, ":", srvr_port)

client_socket, client_address = srvr_socket.accept()
print("[*] Accepted connection from", client_address[0], ":", client_address[1])

# Receive the file name
file_name = client_socket.recv(1024).decode()
print("[*] Receiving file:", file_name)

# Open the file in binary write mode
with open(file_name, 'wb') as file:
    while True:
        # Receive data in chunks
        data = client_socket.recv(1024)
        if not data:
            break
        # Write data to the file
        file.write(data)

print("[*] File received successfully.")

# Close the connection
client_socket.close()
srvr_socket.close()
