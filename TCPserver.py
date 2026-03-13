import socket
import threading


PORT = 5050

# SERVER (ip address) = "192.168.1.31" //my local ip , variable , don't hardcode it
SERVER_IP = socket.gethostbyname(socket.gethostname())
# print(socket.gethostname())
ADDRESS = (SERVER_IP,PORT)
#pick server and port , then bind the socket to them

FORMAT='utf-8'
DISCONNECT_MSG="stop"
HEADER = 64#default length of msg from client to server : 64 bytes,to be changed later

sockett = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #tcp using ipv4   

sockett.bind(ADDRESS)

def handleClient(connection,address):
    #this runs for each client separately using thread
    print(f"[NEW CONNECTION]:{address}")
    connected=True
    while(connected):
        msgLen = connection.recv(HEADER).decode(FORMAT)
        if msgLen:
            msgLen = int(msgLen)
            msg=str(connection.recv(msgLen).decode(FORMAT))
            response=""
            if msg[0].upper()=='A':
                response="".join(sorted(msg[1:], reverse=True))
            elif msg[0].upper()=='C':
                response="".join(sorted(msg[1:]))
            elif msg.upper()=='D':
                response=msg[1:].upper()
            else:
                response=msg[1:]    
            connection.send(response.encode(FORMAT))
        # connected=False        
            if msg == DISCONNECT_MSG:
                connected=False
                print(f"[CONNECTION WITH {address} CLOSED]")
                connection.close()
def startServer():
    sockett.listen()
    while(True):
        connection,address=sockett.accept()#wait for connection (.join y3ny)
        thread=threading.Thread(target=handleClient,args=(connection,address))
        thread.start()
        print(f"[ACTIVE CONNECTIONS: {threading.active_count()-1}]")


if (__name__=="__main__"):
    print(f"[STARTING] Server started on {SERVER_IP}:{PORT}")
    startServer()