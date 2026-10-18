import socket
import threading
import datetime

class SocketServidor:
    def __init__(self, host="0.0.0.0", puerto=5000):
        self.host = host
        self.puerto = puerto
        self.callback = None
        self.running = False

    def iniciar(self, callback_evento):
        self.callback = callback_evento
        self.running = True
        # Iniciar el servidor en un hilo separado
        hilo = threading.Thread(target=self._escuchar, daemon=True)
        hilo.start()
        print(f"[SERVIDOR] Escuchando en {self.host}:{self.puerto}...")
    