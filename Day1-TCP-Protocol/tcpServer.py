import socket

if __name__=="__main__":
    ip = "127.0.0.1"
    port = 1234

    ## Use TCP protocol
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ## Bind the ip address with server 
    server.bind((ip, port))
    server.listen(5)

    while True:
        client, address = server.accept()
        print(f"Connection Establish - {address[0]}:{address[1]}")

        ## Server Receive the message from client
        string = client.recv(1024)
        ## Decode the meassage
        string = string.decode('utf-8')
        print(string)

        ## Send a successfully recieve message to client
        client.send(bytes("Success!","utf-8"))
        client.close()