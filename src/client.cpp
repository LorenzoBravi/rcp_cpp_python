// src/client.cpp
#include <rpc/client.h>
#include <rpc/msgpack.hpp>  // MessagePack library
#include <iostream>
#include <string>

// Define the Person struct and its serialization support
struct Person {
    std::string name;
    int age;

    // Enable serialization of this struct
    MSGPACK_DEFINE(name, age);
};

int main() {
    // Create an RPC client that connects to the server on localhost at port 8080
    rpc::client client("127.0.0.1", 8080);

    // Call the server function and get the serialized Person object
    Person person = client.call("get_person").as<Person>();

    // Print the received Person's details
    std::cout << "Received Person:\n";
    std::cout << "Name: " << person.name << "\n";
    std::cout << "Age: " << person.age << std::endl;

    return 0;
}
