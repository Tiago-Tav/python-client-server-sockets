import socket as skt

HEADER = 64
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = 'exit'
SERVER = '192.168.56.1'
PORT = 6060
ADDR = (SERVER, PORT)

cli = skt.socket(skt.AF_INET, skt.SOCK_STREAM)
cli.connect(ADDR)

def user():
    username = input('say your name: ')

def send(msg):
    message = msg.encode(FORMAT)
    msg_lenght = len(message)
    send_lenght = str(msg_lenght).encode(FORMAT)
    send_lenght += b' ' * (HEADER - len(send_lenght))
    cli.send(send_lenght)
    cli.send(message)

def gateway():
    connect = True
    while connect:
        msg = input("You: ")
        if msg == DISCONNECT_MESSAGE:
            connect = False
        send(msg)
    cli.close()

gateway()