import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('localhost', 8080))
print("UDP Echo Server started...")
while True:                            
    data, addr = sock.recvfrom(1024)
    print("Received:", data.decode())
    sock.sendto(data, addr)