import socket
from pynput.mouse import Button, Controller

mouse = Controller()

port = 5000
ip = "localhost"
multiplier = 1

def networking():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((ip, port))

    while True:
        data, addr = sock.recvfrom(1024)
        data = data.decode("utf-8")
        if (data[-1] == ";" and "|" in data):
            pass
            data = data[0:-1].split("|")

            try:
                x = data[0]
                y = data[1]
                x = -int(x)
                y = -int(y)
                x *= multiplier
                y *= multiplier
                pass

                mouse.move(x, y)
            except:
                x = 0
                y = 0
                pass
        else:
            pass

def mouse_btn_handling():
    pass

networking()
