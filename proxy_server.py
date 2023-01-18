import socket
import _thread

BYTES_TO_READ = 4096
PROXY_SERVER_HOST = "127.0.0.1"
PROXY_SERVER_PORT = 8080

def send_request(host, port, request_data):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((host, port))
        client_socket.send(request_data)
        client_socket.shutdown(socket.SHUT_WR)

    return

def handle_request(conn, addr):
    with conn:
        print("connected by (addr)")
        request = b''
        while True:
            data = conn.recv(BYTES_TO_READ)
            if not data:
                break
            print(data)
            request =+ data

        response = send_request("www.google.com", 80, request)
        conn.sendall(response)

def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind(PROXY_SERVER_HOST, PROXY_SERVER_PORT)
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.listen(2)
        conn, addr = server_socket.accept()
        handle_request(conn, addr)

    return

def start_threaded_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind(PROXY_SERVER_HOST, PROXY_SERVER_PORT)
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.listen(2)
        while True:
            conn, addr = server_socket.accept()
            thread = thread(target=handle_request, args=(conn, addr))
            thread.run()

start_threaded_server
