"""
CPAN 226 - Lab 05
File Transfer Server using TCP Socket
Owen Imudia
This program acts as a TCP server that sends a requested file to a client.
"""

import socket

HOST = "127.0.0.1"   # Loopback address for local testing
PORT = 63025          # Port to listen on

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen()

print("Waiting for Connection...")
conn, addr = s.accept()

try:
    with conn:
        print(f"Connection from {addr}")

        # Receive the file name from the client
        filename = conn.recv(1024).decode()
        print(f"Server received file name request: {filename}")

        try:
            # Try to open and read the requested file
            with open(filename, "rb") as f:
                data = f.read(1024)
                while data:
                    conn.sendall(data)
                    print("Sent:", data)
                    data = f.read(1024)
            print("Done sending file.")
        except FileNotFoundError:
            # If the file doesn’t exist, send an error message
            error_msg = "ERROR: File not found on server."
            conn.sendall(error_msg.encode())
            print(error_msg)

except Exception as e:
    print("An error occurred:", e)

finally:
    s.close()
    print("Server closed.")
