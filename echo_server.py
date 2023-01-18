import socket

BYTES_TO_READ = 4096
HOST = "1.27.0.0.1"
PORT = 8080

def handle_connection(conn, addr): 
    #the connection is a socket directly to the client
    with conn:
        print("connected by (addr)")
        while (True):
            data = conn.recv(BYTES_TO_READ)
            if not data:
                break
            print(data)
            conn.sendall(data)
            #send and sendall is different, but can be used interchangably


def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        #can rebind to the same address

        s.listen()

        conn, addr = s.accept()
        handle_connection(conn, addr)

start_server