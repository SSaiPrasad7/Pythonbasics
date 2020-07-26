import socket
import time

print("UDP SERVER SOCKET")
udp_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_ip = "0.0.0.0"
udp_server.bind((("%s" % server_ip), 2020))
print(f"{server_ip} -> Waiting for clients to connect.....")
data, client_address = udp_server.recvfrom(1024)
print(f"{server_ip} -> Received a message from {client_address}")
print(f"{server_ip} -> Sending a response to  {client_address}")
udp_server.sendto("Hello from Server".encode(),client_address)
time.sleep(10)
udp_server.close()
