#   Import Socket module for networking
import socket
# Import threading module to handle multiple connections
import threading
# It allows your Python program to interact with the Python interpreter itself and the environment in which it's running.
import sys

Host = '127.0.0.1'
Port = 65432


def receive_messages(client_socket):
    try:
        while True:
            data = client_socket.recv(1024)
            if not data:
                print("Connection closed by the server.")
                break
            message = data.decode('utf-8')
            # Print the received message to the console
            print(f"\nServer: {message}")
            # Prompt for user input again
            sys.stdout.write("You: ")
            # Flush the output buffer to ensure the prompt appears immediately
            sys.stdout.flush()
    except ConnectionResetError:
        print("Connection lost.")
    finally:
        client_socket.close()


def start_client():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        try:
            client_socket.connect((Host, Port))
            print(f"Connected to server at {Host}:{Port}")

            # Start a thread to receive messages from the server
            receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
            receive_thread.start()

            while True:
                message = input("You: ")
                if message.lower() == 'exit':
                    print("Exiting chat...")
                    break
                # Send the message to the server
                client_socket.sendall(message.encode('utf-8'))
        except ConnectionRefusedError:
            print(f"Could not connect to server at {Host}:{Port}. Is the server running?")
        finally:
            client_socket.close()
            print("Connection closed.")   

if __name__ == "__main__":
    start_client()    