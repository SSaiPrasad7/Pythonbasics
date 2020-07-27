import socket
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(("127.0.0.1",8080))
print("Request Sent.")

data=client.recv(1024)
message=data.decode()
print(message)

message="Yes!!!"
data=message.encode()
client.send(data)
client.close()