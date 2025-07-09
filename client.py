import socket
import threading

HOST = '26.202.150.44' # Substitute with your desired hosted adress
PORT = 6060
ADRESS = (HOST, PORT)
FORMAT = 'ascii'
MESSAGESIZE = 1024
DISCONNECTIONMESSAGE = '!exit'

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADRESS)

nickname = input('Say your name: ')

def listen():
    while True:
        try:
            message = client.recv(MESSAGESIZE).decode(FORMAT)
            print(message)
        except:
            print('[CLIENT MESSAGE] Connection Closed')
            client.close()
            break

def send(message: str):
    if message == f'{nickname}: {DISCONNECTIONMESSAGE}':
        message_encoded = 'An user left'.encode(FORMAT)
        client.send(message_encoded)
        client.close()
    else:
        message_encoded = message.encode(FORMAT)
        client.send(message_encoded)

def start():
    thread = threading.Thread(target=listen)
    thread.start()
    print(f'[CLIENT MESSAGE] client is listening to {HOST}{PORT}...')
    while True:
        send_message = input(f'{nickname}:')
        send(f'{nickname}: {send_message}')

print(f'[CLIENT MESSAGE] client starting...')
start()