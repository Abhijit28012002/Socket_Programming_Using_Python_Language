import socket
from decouple import config

IP = config('IP')
PORT = int(config('PORT'))
ADDR = (IP,PORT)
FORMAT = config('FORMAT')
SIZE = int(config('SIZE'))

def main():
    ## Use TCP Protocol Connection
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    ## Bind the IP and PORT to the server.
    server.bind(ADDR)

    ## Server Is Ready for listen
    server.listen()
    print("Server is listening!!!!!!")

    while True:
        ## Server has accepted the connection from client
        conn, addr = server.accept()
        print(f" New Client {addr} connected.")

        ## Receiving client filename
        filename = conn.recv(SIZE).decode(FORMAT)
        print(f"Receiving the filename:- {filename}")
        file = open(filename, "w")
        conn.send("Filename received.".encode(FORMAT))

        ## Receiving file data from the client
        data = conn.recv(SIZE).decode(FORMAT)
        print(f"Receiving data sucessful.")
        file.write(data)
        conn.send("File data received".encode(FORMAT))

        ## Closing the file
        file.close()

        ## Close the connection between Server and Client
        conn.close()
        print(f"connection {addr} disconnected.")

if __name__ == "__main__":
    main()