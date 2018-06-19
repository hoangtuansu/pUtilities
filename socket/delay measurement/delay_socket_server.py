import socket
import sys

if __name__ == '__main__':
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = (sys.argv[1], 8089)
    server_socket.bind(server_address)
    server_socket.listen(5) # become a server socket, maximum 5 connections
    print("Server is listening")
    while True:
        connection, address = server_socket.accept()
        try:
            while True:
                data = connection.recv(64)
                print("receive: " + data)
                if data:
                    connection.send("got: " + data)
                else:
                    break
        except KeyboardInterrupt:
            print "Stop server"
            connection.close()
            raise
        finally:
            connection.close()

