import tkinter as tk
from tkinter import ttk
# creacion de metodo constructor
class Visualizador:
    def __init__(self, root, bridge):
        self.root = root
        self.bridge = bridge
        self.root.title("Sistema de Parqueadero — En vivo")
        self.root.geometry("1150x780")