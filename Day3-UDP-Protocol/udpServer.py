import socket

if __name__=='__main__':
    host="127.0.0.1"
    port = 12345

    server = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

    server.bind((host, port))

    while True:
        data, addr = server.recvfrom(1024)
        data = data.decode('utf-8')

        print(f"Received message: {data} from {addr}")
        mess="Data Receive Successfully!!"
        mess=mess.encode('utf-8')
        server.sendto(mess,addr)

    
