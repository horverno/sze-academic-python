# based on python.org example
import socket
import sys

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the port
server_address = ("localhost", 5002)
print("starting up on {} port {}".format(*server_address))
#sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(server_address)

print("-- UDP server starts -- \n  Waiting to receive message - %s, %d" % (server_address[0], server_address[1]))
while True:
    data, address = sock.recvfrom(4096)
    print("  New message: %s" %(data))
    print("  Received %d bytes from %s" %(len(data), address))
    if len(data) >= 1:
        print("-- UDP server finishes --\n")
        exit()