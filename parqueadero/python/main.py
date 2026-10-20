import os
# Asegúrate de poner exactamente el mismo nombre aquí
os.add_dll_directory(r"D:\Escritorio\SimuladorParqueadero\parqueadero\cpp")

import tkinter as tk
from socket_servidor import SocketServidor
from libreria_bridge import LibreriaBridge
from visualizador import Visualizador

def main():
    print("--- INICIANDO SISTEMA DE PARQUEADERO (SERVIDOR PYTHON) ---")
    
    # 1. Inicializar la conexion con la DLL de C++
    try:
        bridge = LibreriaBridge()
        bridge.inicializar()
        print("[BRIDGE] DLL de C++ cargada e inicializada correctamente.")
    except Exception as e:
        print(f"[ERROR] No se pudo inicializar la DLL: {e}")
        return
