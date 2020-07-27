import socket
my_server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
my_server.bind(("0.0.0.0",8080))
my_server.listen()
print("Waiting for Client to connect")
connection_socket,address=my_server.accept()
print("Client connected",address)

message="Is it possible???"
data=message.encode()
connection_socket.send(data)

data=connection_socket.recv(1024)
message=data.decode()
print(message)

connection_socket.close()
my_server.close()