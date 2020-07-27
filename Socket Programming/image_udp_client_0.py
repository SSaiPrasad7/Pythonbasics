import pickle
import socket
client_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
client_socket.connect(("127.0.0.3",2020))
print("Client Connected.")
data,address=client_socket.recvfrom(1024)
message=data.decode()
print(message)