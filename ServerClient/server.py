# Streaming Server
# Library needs for Server
import socket
import time
import os
from random import randint

block_size = 1024
# Create a dummy.img with the following command...
# dd if=/dev/zero of=_current_workdirectory/dummy.img bs=4096k count=64
# The file size should be 256Mb
file_name = "./dummy.img"
HOST = 'localhost'
PORT = 50007

# Create an INET,STREAMing socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# bind the socket to a public host.
s.bind((HOST, PORT))
# Enable a server to accept connections. It specifies the number of unaccepted connections thtat the system will allow before refusing new connetions.
s.listen(1)

bbytes = 0
file_stats = os.stat(file_name)
bbytes = file_stats.st_size

while True:
    # Accept a connection.
    (client_socket, address) = s.accept()
    with client_socket:
        print('Client connection accepted ', address)
        while True:
            print("Sending big file...")
            # open file and return a corresponding file obj. Default, open a file for reading
            with open("dummy.img","rb") as f:
                # Function read([size]) -> Read at most size bytes from the file. If size < 0 or omitted, reads all data until EOF
                data = f.read(block_size)
                while(data):
                    send = client_socket.sendall(data)
                    print(f'Send {send} of {bbytes}\n')
print("Send done !")
