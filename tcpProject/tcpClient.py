import socket

if __name__=="__main__":
    ip = "127.0.0.1"
    port = 1234

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.connect((ip, port))

    ## Client Send message to server
    string = input("Enter Your message:- ")
    server.send(bytes(string,"utf-8"))

    ## Receive the meassage from Server
    message = server.recv(1024)
    message = message.decode("utf-8")
    print(message)