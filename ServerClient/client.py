#  Streaming Client

import socket
import time

HOST = 'localhost'
PORT = 50007

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

while True:
    data = s.recv(1024)
    if not data:
        break
    time.sleep(0.5)
    print ("Data received...")

print ("All done...")
s.close()
