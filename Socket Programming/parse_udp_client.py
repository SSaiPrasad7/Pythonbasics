import socket
import time
import pickle

print("UDP CLIENT SOCKET")
udp_client=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
print("Client Connected.")
client_ip = "127.0.0.1"
message={"client":1,"server":2}
data=pickle.dumps(message)
print(f"{client_ip}-> Sending {message} to ")
udp_client.sendto(data, (("%s" % client_ip), 2020))
time.sleep(10)