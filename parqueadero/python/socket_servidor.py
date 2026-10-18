import socket
import threading
import datetime

class SocketServidor:
    def __init__(self, host="0.0.0.0", puerto=5000):
        self.host = host
        self.puerto = puerto
        self.callback = None
        self.running = False