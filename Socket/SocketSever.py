import socket
import threading
class SocketSever:
    def __init__(self):
        self.s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.HOST="127.0.0.1"
        self.PORT=65432
        self.s.bind((self.HOST,self.PORT))
        self.s.listen(5)
        self.clientList=[]
        print("The server has been created successfully!")
        print("Sever is waitting for client at 127.0.0.1:65432...")
        

    def handleClient(self,conn,addr):
        print("Sever is connecting with client "+str(self.clientList.index(conn)))
        clientIdx=str(self.clientList.index(conn))

        try:
            while True:
                print("Sever is waiting request from client " + clientIdx + "...")
                data = conn.recv(1024)
                strData=data.decode("utf8")
                if len(data)> 0:
                    print("Server recv from client " + clientIdx + ":" + data.decode("utf8"))
                else:
                    break
                if strData=="quit":
                    break
                try:
                    msg=input("Sever reponse client "+clientIdx + ":")
                    conn.sendall(bytes(msg,"utf8"))
                except (KeyboardInterrupt,EOFError):
                    break

        except Exception as e:
            print("Closing connection with client "+clientIdx)
        finally:
            print("client " + clientIdx + " was closed.")
            self.clientList.remove(conn)
            conn.close() 

            if(self.clientList.__len__()==0):
                    print("There are no clients connected")
                    print("Do you want continue sever (y/n)?")
                    choice=input()
                    if(choice=="n" or choice=="N"):
                        print("Sever is closing...")
                        self.s.close()
                        exit(0)

    def thread(self):
        try:
            while(True):

                conn,addr=self.s.accept()
                self.clientList.append(conn)

                clientThread=threading.Thread(target=self.handleClient,args=(conn,addr))
                clientThread.daemon=True
                clientThread.start()

        except OSError:
            print("Sever was closed")
        except KeyboardInterrupt:
            print("Sever was closed due to keyboardInterrupt")
        finally:
            self.s.close()

mySever=SocketSever()
mySever.thread()
        