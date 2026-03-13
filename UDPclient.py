import socket

PORT = 5051

SERVER_IP = "192.168.1.31"
ADDRESS = (SERVER_IP, PORT)

FORMAT = 'utf-8'
DISCONNECT_MSG = "stop"

clientt = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def sendMsg(msg):
    #send message directly no header
    messageEncoded = msg.encode(FORMAT)
    clientt.sendto(messageEncoded, ADDRESS)
    
    data, _ = clientt.recvfrom(1024)
    response = data.decode(FORMAT)
    if not response.lower()=="disconnected":
        print(f"[SERVER RESPONSE]: {response}")

myMsg = input("enter msg: ")
sendMsg(myMsg)
sendMsg(DISCONNECT_MSG)

clientt.close()