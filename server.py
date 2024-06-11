import socket

def start_server():
    #Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #Get local machine name
    host = socket.gethostname()
    port = 12345

    #Bind the socket to the port
    server_socket.bind((host, port))
    print(f"socket binded to {port}")

    #Queue up to 5 requests
    server_socket.listen(5)

    print("Server started. Waiting for connections...")

    while True:
        #Establish a connection
        client_socket, addr = server_socket.accept()  # Accepts a connection and returns a new socket and address
        print(f"Got a connection from {addr}")  # addr contains the client's IP address and port number

        #Send a message to the client
        message = input()
        client_socket.send(message.encode('ascii'))

        #Receive data from the client
        data = client_socket.recv(1024)  #In this case, it tries to receive up to 1024 bytes of data from the client.
        print(f"Received from client: {data.decode('ascii')}")
    
        #Close the connection
        client_socket.close()

if __name__ == '__main__':
    start_server()