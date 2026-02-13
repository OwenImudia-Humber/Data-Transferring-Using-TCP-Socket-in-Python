# Data-Transferring-Using-TCP-Socket-in-Python
This project demonstrates a basic TCP client-server file transfer system written in Python. The server listens for a connection, receives a filename from the client, and sends back the file’s contents over a TCP socket. If the file does not exist, the server sends an error message instead. 


# Structure

Networking/
│
├──.idea
    ├── server.py
    ├── client.py
    ├── mytext.txt
├── README.md


# How to Run

Place server.py, client.py, and your test file (e.g., mytext.txt) in the same folder.

Open two terminals in that folder.

In the first terminal, start the server:

python server.py


Output example:
Server is listening for incoming connections...

In the second terminal, start the client:

python client.py


When prompted, enter the filename (e.g., mytext.txt).

The client receives and saves the file as received_mytext.txt.

Verify that the received file matches the original.

Both programs close automatically after transfer.

# Author
Owen Imudia

# Email
Imudiaowen@gmail.com

Course: CPAN 226 – Network Programming
Institution: Humber College
