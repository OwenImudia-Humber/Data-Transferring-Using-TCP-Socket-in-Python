"""
CPAN 226 - Lab 05
File Transfer Client using TCP Socket
Owen Imudia
This program connects to a TCP server and downloads the requested file.
"""

import socket

HOST = "127.0.0.1"  # Must match the server address
PORT = 63025        # Must match the server port

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    # Ask for the file name to download from the server
    filename = input("Enter the filename to request: ")
    s.sendall(filename.encode())  # Send the filename to the server
    print("Request sent. Receiving data...")

    # Create a new file to save the incoming data
    with open("received_" + filename, "wb") as f:
        while True:
            data = s.recv(1024)
            if not data:  # End of transmission
                break
            f.write(data)  # Write received data to file
            print("Receiving:", data)

    print("File transfer complete. Saved as received_" + filename)

s.close()
print("Connection closed.")
