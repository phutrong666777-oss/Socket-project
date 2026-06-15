# Socket-project

## Description

This project aims to create a system that include sever and client. They can interact basically with other thought the virtual socket like:

-Comunicating, sending or receiving mail.
-Perfomance status of sever or client.
-Response request in real-time.

## Features

### Sever

-Init sever and display relative information
-Handle client with work-flow read and write
-Block client or close sever whenever we want

### Client

-Connect sever with specific number port and host id
-Send request to sever and receive response
-Close client whenever we want

## File struct
```text

Socket/
│   ├── SocketSever/
|   |   
│   │
│   ├── SocketClient/
|   |
|   |
└── README.md
```

## Compile

```bash
python SocketSever.py
python SocketClient.py
```

## Sample Output

### Sever

```text
The server has been created successfully!
Sever is waitting for client at 127.0.0.1:65432...

Sever is connecting with client 0
Sever is waiting request from client 0...

Sever is connecting with client 1
Sever is waiting request from client 1...

Server recv from client 1:hello sever
Sever reponse client 1:hi client 1
Sever is waiting request from client 1...

Server recv from client 0:hi sever
Sever reponse client 0:hello client 0
Sever is waiting request from client 0...

Server recv from client 1:quit
client 1 was closed.
Server recv from client 0:quit
client 0 was closed.
There are no clients connected
Do you want continue sever (y/n)?
n
Sever is closing...
Sever was closed
```

### Client 0

```text
Please Enter IP sever you want to connect:127.0.0.1
Please enter port number you want to connect:65432
Client is connecting to server with port: 65432

Enter your mail:hi sever
Client is waiting request from sever...
Client recv: hello client 0

Enter your mail:quit
Client was closed.
```
### Client 1

```text
Please Enter IP sever you want to connect:127.0.0.1
Please enter port number you want to connect:65432
Client is connecting to server with port: 65432

Enter your mail:hello sever
Client is waiting request from sever...
Client recv: hi client 1

Enter your mail:quit
Client was closed.
```
