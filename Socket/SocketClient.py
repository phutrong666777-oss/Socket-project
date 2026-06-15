import socket

class SocketClient:
    def __init__(self):
        self.hostSever=input("Please Enter IP sever you want to connect:")
        self.portSever=int(input("Please enter port number you want to connect:"))

        self.client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("Client is connecting to server with port: " + str(self.portSever))
        self.client.connect((self.hostSever,self.portSever))

    def read(self):
        data=self.client.recv(1024)
        if len(data)>0:
            strData=data.decode("utf8")
            print("Client recv:",strData)

    def write(self):
        try:
            while(True):
                msg=input("Enter your mail:")
                self.client.sendall(bytes(msg,"utf8"))
                if msg=="quit":
                    break
                print("Client is waiting request from sever...")
                self.read()
        except ConnectionResetError:
            print("Connection with server was closed.")
        except OSError:
            print("An error occurred while communicating with the server.")
        except KeyboardInterrupt:
            print("Client was closed.")
            self.client.close()
        finally:
            print("Client was closed.")
            self.client.close() 
              
myClient=SocketClient()
myClient.write()