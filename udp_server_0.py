import socket
import time

print("UDP SERVER SOCKET")
udp_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_server.bind(("0.0.0.0", 2020))
print("Waiting for Client to connect.....")
data, client_address = udp_server.recvfrom(1024)
print(f"{client_address}")
udp_server.sendto("Server->Hello".encode(),client_address)
time.sleep(10)
udp_server.close()
