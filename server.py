import socket as skt
import threading



HOST = skt.gethostbyname(skt.gethostname())
PORT = 6060
ADDR = (HOST,PORT)
HEADER = 64
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = 'exit'

sv = skt.socket(skt.AF_INET, skt.SOCK_STREAM)
sv.bind(ADDR)

connections = []

def handle(conn, ADDR):
    print(f"[NEW CONNECTION] {ADDR[0]}:{ADDR[1]} connected.")
    connected = True
    connections.append(conn)
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False
            print(f"[{ADDR[0]}:{ADDR[1]}] {msg}")
            
    conn.close()

def start():
    sv.listen()
    print(f'[SERVER] listening on {HOST}')
    while True:
        conn, ADDR = sv.accept()
        thread = threading.Thread(target=handle, args=(conn, ADDR))
        thread.start()
        print(f"[SERVER] Active connections: {threading.active_count() - 1}")

print("[SERVER] starting...")
start()