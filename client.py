import socket
import msgpack

# Define a Person "struct" as a Python class (same as server)
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def to_dict(self):
        return {'name': self.name, 'age': self.age}

    @staticmethod
    def from_dict(data):
        return Person(data['name'], data['age'])

# Define the RPC Client
class MsgpackRPCClient:
    def __init__(self, host='localhost', port=8080):
        self.host = host
        self.port = port
        self.msgid = 0

    # Make a synchronous call to the server
    def call(self, method, params):
        self.msgid += 1
        request = [0, self.msgid, method, params]
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((self.host, self.port))
            s.sendall(msgpack.packb(request))
            data = s.recv(1024)
            response = msgpack.unpackb(data, raw=False)
            return self.handle_response(response)

    # Handle the response from the server
    def handle_response(self, response):
        msg_type, msgid, error, result = response
        if error:
            raise Exception(f"RPC Error: {error}")
        return result

# Use the client to call the 'get_person' method
if __name__ == "__main__":
    client = MsgpackRPCClient()
    
    # Call the server method to get the Person data
    person_data = client.call("get_person", [])
    
    # Deserialize the result back into a Person object

    person = Person(person_data[0], person_data[1])
    
    # Print the result
    print(f"Person name: {person.name}, age: {person.age}")
