import socket
import sys
import datetime as dt
import time

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = (sys.argv[1], 8089)
client_socket.connect(server_address)
count = 1

try:

    while count < 10:
        t1 = dt.datetime.now()
        client_socket.send('hello')
        data = client_socket.recv(1024)
        t2 = dt.datetime.now()
        delay = (t2.microsecond - t1.microsecond)/1e6
        print("from server: " + data + ", delay: " + str(delay))
        count=count + 1
        time.sleep(1)
finally:
    client_socket.close()
