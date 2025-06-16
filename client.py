import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('localhost', 8080)
while True:
    msg = input("Enter message: ")
    sock.sendto(msg.encode(), server_address)
    data, _ = sock.recvfrom(1024)
    print("Echoed:", data.decode())