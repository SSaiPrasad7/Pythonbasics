import pickle
import socket
import time

server_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server_socket.bind(("0.0.0.0",2020))
print("Waiting for Client to connect.....")
time.sleep(3)
server_socket.sendto("Hello".encode(),("127.0.0.3",2020))
