# server.py
import socket
import threading
import pickle

class Server:
    def __init__(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind(('localhost', 5555))
        self.server.listen()
        self.clients = []
        self.player_positions = {}

        print("Server started, waiting for connections...")
        self.accept_connections()

    def accept_connections(self):
        while True:
            client, address = self.server.accept()
            print(f"Connection from {address} has been established!")
            self.clients.append(client)
            threading.Thread(target=self.handle_client, args=(client,)).start()

    def handle_client(self, client):
        while True:
            try:
                data = pickle.loads(client.recv(2048))
                if data == "get_pos":
                    client.send(pickle.dumps(self.player_positions))
                else:
                    # Update player positions based on received data
                    self.update_player_positions(data)
            except:
                break

    def update_player_positions(self, data):
        # Update the player positions based on received data
        # Broadcast updated positions to all clients
        for client in self.clients:
            client.send(pickle.dumps(self.player_positions))

if __name__ == "__main__":
    Server()