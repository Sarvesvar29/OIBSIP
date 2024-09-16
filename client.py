#Client


import socket
import threading

def receive_messages():
    while True:
        try:
            # Receiving message from the server
            message = client.recv(1024).decode('utf-8')
            if message:
                print(f"\n{message}")
        except:
            print("An error occurred!")
            client.close()
            break
            
def send_messages():
    while True:
        message = input("")
        client.send(message.encode('utf-8'))

# Client setup
SERVER = "127.0.0.1"  
PORT = 5555
ADDRESS = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDRESS)

receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()

send_thread = threading.Thread(target=send_messages)
send_thread.start()



