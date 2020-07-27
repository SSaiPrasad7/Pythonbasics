import socket
def get_text(client_socket):
    buffer=""
    socket_open=True
    while socket_open:
        data=client_socket.recv(1024)
        if not data:
            socket_open=False
        buffer+=data.decode()
        position=buffer.find('\n')
        while position>-1:
            message=buffer[:position]
            buffer=buffer[position+1:]
            yield message
            position = buffer.find('\n')
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(("127.0.0.1",2000))
print("Request Sent")
for message in get_text(client):
    print(message)
#message = next(get_text(client))
#print(message)
client.close()