import socket

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server socket
client_socket.connect(('148.225.64.49', 3000))

# Send a message to the server
message = 'Hola somos tecolotes!!!!!'
client_socket.send(message.encode())

# Close the socket
client_socket.close()

