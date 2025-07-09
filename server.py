import socket
import threading


HOST = socket.gethostbyname(socket.gethostname())
PORT = 6060
ADRESS = (HOST, PORT)
FORMAT = 'ascii'
MESSAGESIZE = 1024
DISCONNECTIONMESSAGE = '!exit'

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADRESS)


clients = []

def broadcast(clients, message):
    for client in clients:
        client.send(message)
    
def handle(connection: socket.socket,adress):
    connected = True
    clients.append(connection)
    while connected:
        try:
            message = connection.recv(MESSAGESIZE)
            if message == DISCONNECTIONMESSAGE:
                connected = False
            if message:
                broadcast(clients, message)
        except:
            print(f'[SERVER MESSAGE] We Found an error, closing {adress} connection')
            connected = False
    clients.remove(connection)
    connection.close()


def start():
    server.listen()
    print('[SERVER MESSAGE] server listening... ')
    while True:
        connection, adress = server.accept()
        thread = threading.Thread(target=handle, args=(connection,adress))
        thread.start()
        print(f'[SERVER MESSAGE] new connection detected! {connection}{adress}, is now welcome! total active connections: {threading.active_count() - 1}')
    
print('[SERVER MESSAGE] server starting... ')
start()