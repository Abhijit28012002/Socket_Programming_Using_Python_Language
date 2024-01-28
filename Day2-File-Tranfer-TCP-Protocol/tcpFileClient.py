import socket
from decouple import config

IP = config('IP')
PORT = int(config('PORT'))
ADDR = (IP,PORT)
FORMAT = config('FORMAT')
SIZE = int(config('SIZE'))


def main():
    ## Use TCP Protocol Connection
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    ## Connecting to the server
    client.connect(ADDR)

    ## Open  file and read data
    file = open("data/info.txt", "r")
    data = file.read()

    ## Sending the filename to the server.
    client.send("info.txt".encode(FORMAT))

    ## Receive Message Which Send by server
    msg = client.recv(SIZE).decode(FORMAT)
    print(f"[SERVER]: {msg}")

    ## Sending the file data to the server
    client.send(data.encode(FORMAT))
    msg = client.recv(SIZE).decode(FORMAT)
    print(f"Sever: {msg}")

    ## Close the File
    file.close()

    ## Close The Connection
    client.close()


if __name__ == "__main__":
    main()