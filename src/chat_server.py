# importing networking modules
import socket
#multithreading module to handle multiple clients(multiple connections/Processing)
import threading

# Server configuration
HOST = '127.0.0.1'
PORT = 65432

def handle_client(connection, address):
    print(f"New connection from {address}")
    try:
        while True:
            # Receiving data from the client
            data = connection.recv(1024)
            if not data:
                break
            # Decoding the received bytes to string
            message = data.decode('utf-8')
            print(f"[{address[0]}:{address[1]}] {message}")

            # Echo the message back to the client
            reply_message = input("Server response: ")
            # Encoding the string to bytes before sending
            connection.sendall(reply_message.encode('utf-8'))
    except ConnectionResetError:
        print(f"Connection with {address} lost.")
    finally:
        connection.close()
        print(f"Connection with {address} closed.")


#function to set up and run our server
def start_server():
    #creating a new socket object
    """socket.AF_INET: This specifies the address family, indicating that we will be using IPv4 addresses.
    socket.SOCK_STREAM: This specifies the socket type,
      indicating that we will be using TCP, which is a connection-oriented protocol."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        # This method associates the server_socket with a specific network address.
        server_socket.bind((HOST, PORT))
        server_socket.listen()
        print(f"Server listening on {HOST}:{PORT}")

        while True:
            connection, address = server_socket.accept()
            client_thread = threading.Thread(target=handle_client, args=(connection, address))
            client_thread.start()

if __name__ == "__main__":
    start_server()
