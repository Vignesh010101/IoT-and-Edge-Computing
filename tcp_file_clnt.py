#Client

import socket

srvr_host = 'client ip'
srvr_port = 35791

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((srvr_host, srvr_port))

# Send the file name
file_name = 'chatgpt.txt'  # Change this to the name of the file you want to send
client_socket.sendall(file_name.encode())

# Open the file in binary read mode
with open(file_name, 'rb') as file:
    # Read and send data in chunks
    data = file.read(1024)
    while data:
        client_socket.sendall(data)
        data = file.read(1024)

print("[*] File sent successfully.")

# Close the connection
client_socket.close()
