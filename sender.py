import sys
from PyQt5 import QtWidgets
import socket

port = 5000
ip = "localhost"
moves_per_send = 1

print(f"port: {port}")
print(f"ip: {ip}")

class WebCanvas(QtWidgets.QLabel):

    def __init__(self):
        super().__init__()
        self.point = [0, 0]
        self.setText(f"port: {port}\nip: {ip}")

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.connect((ip, port))

        self.att = 0
        self.x = 0
        self.y = 0

    def mousePressEvent(self, e):
        self.point[0] = e.x()
        self.point[1] = e.y()

    def mouseMoveEvent(self, e):
        self.x = self.point[0] - e.x()
        self.y = self.point[1] - e.y()

        if self.att == moves_per_send:
            self.byt = bytes(f"{self.x}|{self.y};", "utf-8")
            self.sock.sendto(self.byt, (ip, port))
            self.point[0] = e.x()
            self.point[1] = e.y()
        else:
            self.att += 1

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()

        self.canvas = WebCanvas()

        w = QtWidgets.QWidget()
        l = QtWidgets.QVBoxLayout()
        w.setLayout(l)
        l.addWidget(self.canvas)

        self.setCentralWidget(w)


app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
