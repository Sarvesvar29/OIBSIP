#Server

import socket
import threading

# Function to handle communication with clients
def handle_client(client_socket, client_address):
    print(f"[NEW CONNECTION] {client_address} connected.")
    
    while True:
        try:
            # Receiving messages from the client
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                print(f"[{client_address}] {message}")
                # Broadcasting the message to other clients
                broadcast(message, client_socket)
            else:
                # If message is empty, client has disconnected
                print(f"[DISCONNECTED] {client_address}")
                clients.remove(client_socket)
                client_socket.close()
                break
        except:
            print(f"[ERROR] Connection with {client_address} lost.")
            clients.remove(client_socket)
            client_socket.close()
            break

# Function to broadcast messages to all connected clients
def broadcast(message, sender_socket):
    for client in clients:
        if client != sender_socket:
            client.send(message.encode('utf-8'))

# Server setup
def start_server():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        client_socket, client_address = server.accept()
        clients.append(client_socket)
        thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")

# Server configuration
SERVER = "127.0.0.1"  # localhost, you can replace this with the server's IP address
PORT = 5555
ADDRESS = (SERVER, PORT)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDRESS)

clients = []

print("[STARTING] Server is starting...")
start_server()


