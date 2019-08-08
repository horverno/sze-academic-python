# based on python.org example
import socket
import sys

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_address = ("localhost", 5002)
message = b"Hello UDP"

print("-- UPD client starts --")
try:
    # Send data
    print("  Sending %s" %(message))
    sent = sock.sendto(message, server_address)
finally:
    print("-- UPD client finishes, closing socket -- ")
    sock.close()