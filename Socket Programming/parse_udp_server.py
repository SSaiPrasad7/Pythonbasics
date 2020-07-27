import pickle
import socket
import time

print("Server Socket for parsing the data.")
server_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server_ip="0.0.0.0"
server_socket.bind((("%s"%server_ip),2020))
print(f"{server_ip}-> Waiting for clients to connect...")

data,client_address=server_socket.recvfrom(1024)
print(f"{server_ip}->Recieved a message from {client_address} ")
message=pickle.loads(data)
print(f"{server_ip}->Recieved a message {message} from {client_address}")
time.sleep(10)
server_socket.close()