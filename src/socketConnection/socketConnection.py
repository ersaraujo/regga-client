import socket

class SocketClient:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        try: 
            self.client.connect((self.host, self.port))
            print("Connected to server: ", self.host, self.port)
        except ConnectionRefusedError:
            print("Connection refused by server: ", self.host, self.port)
            raise
    
    def send(self, message):
        try:
            self.client.sendall(message.encode())
        except ConnectionError:
            print("Connection error")
            raise

    def close(self):
        self.client.close()