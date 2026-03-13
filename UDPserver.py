import socket

PORT = 5051

# SERVER (ip address) = "192.168.1.31" //my local ip , variable , don't hardcode it
SERVER_IP = socket.gethostbyname(socket.gethostname())
ADDRESS = (SERVER_IP, PORT)

FORMAT = 'utf-8'
DISCONNECT_MSG = "stop"

sockett = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sockett.bind(ADDRESS)

def processMessage(msg):
    response = ""
    if msg[0].upper() == 'A':
        response = "".join(sorted(msg[1:], reverse=True))
    elif msg[0].upper() == 'C':
        response = "".join(sorted(msg[1:]))
    elif msg[0].upper() == 'D':
        response = msg[1:].upper()
    else:
        response = msg[1:]
    return response

def startServer():
    print(f"[STARTING] UDP Server started on {SERVER_IP}:{PORT}")
    while True:
        data, client_address = sockett.recvfrom(1024)
        msg = data.decode(FORMAT)
        print(f"[{client_address}]: {msg}")
        
        if msg == DISCONNECT_MSG:
            response = "Disconnected"
        else:
            response = processMessage(msg)
        
        sockett.sendto(response.encode(FORMAT), client_address)

if __name__ == "__main__":
    startServer()