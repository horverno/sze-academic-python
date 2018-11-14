import time
import socket
from sense_hat import SenseHat

def get_ip_address():
    ip_address = '';
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8",80))
    ip_address = s.getsockname()[0]
    s.close()
    return ip_address

sense = SenseHat()
for _ in range(10):
    sense.show_message("IP:", text_colour=(255, 0, 0))
    time.sleep(1)
    try:
        sense.show_message(get_ip_address())
    except:
        print("exception")
    time.sleep(1)
print(get_ip_address())