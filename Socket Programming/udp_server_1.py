import socket
import time

server_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server_ip = "0.0.0.0"
server_socket.bind((("%s" % server_ip), 2020))
print("Waiting for Client to connect.....")

data = "Hello"
client_ip = "127.0.0.1"
server_socket.sendto(data.encode(), (("%s" % client_ip), 2020))
time.sleep(10)
server_socket.close()


