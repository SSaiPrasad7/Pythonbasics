import socket
import time

print("UDP CLIENT SOCKET")
udp_client=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
print("Client Connected.")
client_ip = "127.0.0.1"
data = "Hello"
print(f"{client_ip}-> Sending {data} to ")
udp_client.sendto(data.encode(), (("%s" % client_ip), 2020))
time.sleep(10)
data, server_address = udp_client.recvfrom(1024)
returned_message = data.decode()
print(f"{client_ip} -> Received the following message {returned_message}")
