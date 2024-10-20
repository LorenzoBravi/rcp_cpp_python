// src/server.cpp
#include <rpc/server.h>
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
    // Create an RPC server on port 8080
    rpc::server srv(8080);

    srv.suppress_exceptions(true);

    // Bind a function that returns a Person object
    srv.bind("get_person", []() -> Person {
        Person person = {"John Doe", 30};  // Example Person object
        return person;
    });

    std::cout << "Server is running on port 8080..." << std::endl;

    // Run the server
    srv.run();

    return 0;
}
