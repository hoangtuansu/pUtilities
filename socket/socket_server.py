import socket

if __name__ == '__main__':
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 8089))
    server_socket.listen(5) # become a server socket, maximum 5 connections

    while True:
        connection, address = server_socket.accept()
        buf = connection.recv(64)
        if len(buf) > 0:
            print buf
            break
