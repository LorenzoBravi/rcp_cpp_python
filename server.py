

import socket
import msgpack

# Define a Person "struct" as a Python class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def to_dict(self):
        return {'name': self.name, 'age': self.age}

    @staticmethod
    def from_dict(data):
        return Person(data['name'], data['age'])

# Define the RPC Server
class MsgpackRPCServer:
    def __init__(self, host='localhost', port=8080):
        self.host = host
        self.port = port
        self.methods = {
            "get_person": self.get_person
        }

    # Define the 'get_person' method that returns a Person instance
    def get_person(self):
        return Person("John Doe", 30).to_dict()

    # Start the server to listen for incoming connections
    def run(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((self.host, self.port))
            s.listen()
            print(f"Server listening on {self.host}:{self.port}")

            while True:
                conn, addr = s.accept()
                with conn:
                    print(f"Connected by {addr}")
                    data = conn.recv(1024)
                    if not data:
                        break
                    request = msgpack.unpackb(data, raw=False)
                    response = self.handle_request(request)
                    conn.sendall(msgpack.packb(response))

    # Handle incoming RPC requests
    def handle_request(self, request):
        msg_type, msgid, method, params = request
        if msg_type == 0:  # RPC Request type
            if method in self.methods:
                try:
                    result = self.methods[method]()
                    return [1, msgid, None, result]  # Success response
                except Exception as e:
                    return [1, msgid, str(e), None]  # Error response
            else:
                return [1, msgid, f"Method {method} not found", None]

# Start the server
if __name__ == "__main__":
    server = MsgpackRPCServer()
    server.run()
