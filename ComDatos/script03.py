import socket

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
server_socket.bind(('10.10.138.127', 3000))

# Listen for incoming connections
server_socket.listen(1)

print('Listening on port 3000...')

while True:
    # Wait for a client to connect
    client_socket, address = server_socket.accept()

    # Read data from the client
    data = client_socket.recv(1024).decode()

    # Print the received string
    print(f'Received: {data}')

    # Close the client socket
    client_socket.close()
