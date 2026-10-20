import tkinter as tk
from tkinter import ttk
# creacion de metodo constructor
class Visualizador:
    def __init__(self, root, bridge):
        self.root = root
        self.bridge = bridge
        self.root.title("Sistema de Parqueadero — En vivo")
        self.root.geometry("1150x780")

    #paleta de colore
        self.bg_fondo = "#050B1A"       
        self.bg_panel = "#0A1530"        
        self.libre_fondo = "#10264D"    
        self.libre_borde = "#1E4D8C"     
        self.ocupada = "#2979FF"         
        self.borde_panel = "#2962C9"     
        self.encabezado = "#1565C0"      
        self.titulo = "#4FC3F7"          
        self.texto = "#E3F2FD"          
        self.texto_secundario = "#7A9CC6"
        self.nombres = "#00E5FF"         
        self.texto_ocupada = "#050B1A"   
