# CMakeLists.txt

# Minimum CMake version
cmake_minimum_required(VERSION 3.10)

# Project name and version
project(RPCProject VERSION 1.0)

# Set C++ standard
set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED True)

# Define the directory for output binaries
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/bin)

# Include directories for rpclib and project headers
include_directories(${PROJECT_SOURCE_DIR}/rpclib/include)
include_directories(${PROJECT_SOURCE_DIR}/include)

# Path to rpclib static library
set(RPCLIB_STATIC ${PROJECT_SOURCE_DIR}/libs/librpc.a)

# Define the source files for the server and client
set(SERVER_SOURCES ${PROJECT_SOURCE_DIR}/src/server.cpp)
set(CLIENT_SOURCES ${PROJECT_SOURCE_DIR}/src/client.cpp)

# Create an executable for the server
add_executable(server ${SERVER_SOURCES})

# Link the rpclib static library with the server executable
target_link_libraries(server ${RPCLIB_STATIC} pthread)

# Create an executable for the client
add_executable(client ${CLIENT_SOURCES})

# Link the rpclib static library with the client executable
target_link_libraries(client ${RPCLIB_STATIC} pthread)

# Display some messages for clarity
message(STATUS "RPCLIB_STATIC: ${RPCLIB_STATIC}")
