import socket


PORT = 5050

# SERVER (ip address) = "192.168.1.31" //my local ip , variable , don't hardcode it
SERVER_IP = "192.168.1.31"
# print(socket.gethostname())
ADDRESS = (SERVER_IP,PORT)
#pick server and port , then bind the socket to them

FORMAT='utf-8'
DISCONNECT_MSG="stop"
HEADER = 64#default length of msg from client to server : 64 bytes,to be changed later

clientt = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #tcp using ipv4   
clientt.connect(ADDRESS)

def sendMsg(msg):
    messageEncoded = msg.encode(FORMAT)
    msgLen = len(messageEncoded)
    sendLen = str(msgLen).encode(FORMAT)
    sendLen=sendLen+(HEADER-len(sendLen))*b' '
    clientt.send(sendLen)
    clientt.send(messageEncoded)
    response = clientt.recv(1024).decode(FORMAT)
    if not response== "top":
        print(f"[SERVER RESPONSE]: {response}")
myMsg = input("enter msg: ")
sendMsg(myMsg)    
sendMsg(DISCONNECT_MSG)