// src/main.cpp
#include <rpc/client.h>
#include <iostream>

int main() {
    // Create an RPC client and connect to the server
    rpc::client client("127.0.0.1", 8080);
    
    // Call a function on the server and get the result
    auto result = client.call("some_function").as<int>();

    // Print the result
    std::cout << "Result from server: " << result << std::endl;

    return 0;
}
