import socket
def send_text(client,text):
    text=text+'\n'
    data=text.encode()
    client.send(data)

server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(("127.0.0.1",2000))
server.listen()
print("Waiting for client to connect.")
client_socket,address=server.accept()
print("Client Connected.")
send_text(client_socket,"Hello,My name is S.Sai Prasad.")
client_socket.close()
server.close()
