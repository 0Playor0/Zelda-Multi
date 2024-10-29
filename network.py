# network.py
import socket
import pickle

class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = 'localhost'  # Change to your server address
        self.port = 5555  # Change to your server port
        self.address = (self.server, self.port)
        self.player_id = self.connect()

    def connect(self):
        try:
            self.client.connect(self.address)
            return self.client.recv(2048).decode()  # Get player ID from server
        except Exception as e:
            print(e)

    def send(self, data):
        try:
            self.client.send(pickle.dumps(data))
            return pickle.loads(self.client.recv(2048))  # Receive response
        except Exception as e:
            print(e)

    def getPos(self):
        return self.send("get_pos")  # Example of sending a request to get position