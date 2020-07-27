import socket
import sys


def server_setup():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("0.0.0.0", 2020))
    server_socket.listen()
    print("Waiting for Connection")
    connection_socket, address = server_socket.accept()
    print("Connected", address)
    try:
        message_func(connection_socket, "")
        connection_socket.close()
        server_socket.close()
    except:
        print("Connection terminated with client")
        connection_socket.close()
        server_socket.close()


def client_setup():
    server_ip = input("Enter the IP address of the Server: ")
    if server_ip == " ":
        server_ip = "127.0.0.2"
    connection_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        connection_socket.connect((server_ip, 2020))
        print("Connected to server")
        message_func(connection_socket, "Connected to server")
        connection_socket.close()
    except:
        print("ERROR: Unable to connect to server")


def message_func(connection_socket, text):
    while True:
        if text != "":
            send_text(connection_socket, text)
            text = ""
        else:
            message = next(get_text(connection_socket))
            print(message)
            try:
                text = input("Input your message: ")
            except:
                sys.exit()


def send_text(connection_socket, text):
    text = text + '\n'
    data = text.encode()
    connection_socket.send(data)


def get_text(connection_socket):
    buffer = ""
    socket_open = True
    while socket_open:
        data = connection_socket.recv(1024)
        if not data:
            socket_open = False
        buffer += data.decode()
        position = buffer.find('\n')
        while position > -1:
            message = buffer[:position]
            buffer = buffer[position + 1:]
            yield message
            position = buffer.find('\n')


if __name__ == "__main__":
    print("1.Server \n2.Client \n3.Quit")
    choice = input("Select 1 or 2 option from the above:")
    while True and choice!=3:
        if choice == "1":
            server_setup()
        elif choice == "2":
            client_setup()
        elif choice=="3":
            print("QUIT")
            break
        else:
            print("Incorrect choice")
