import ctypes
import os

class LibreriaBridge:
    def __init__(self):
        # La DLL sera copiada a esta misma carpeta por el script de compilacion
        dll_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "libreria.dll"))
        
        # Si no esta en la carpeta local, intentar en la carpeta cpp (por si acaso)
        if not os.path.exists(dll_path):
            dll_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "cpp", "libreria.dll"))
        
        try:
            self.lib = ctypes.CDLL(dll_path)
        except Exception as e:
            print(f"Error al cargar la DLL en {dll_path}: {e}")
            raise

        # Configurar tipos de argumentos y retornos
        self.lib.inicializar.argtypes = []
        self.lib.inicializar.restype = None

        self.lib.procesarPlaca.argtypes = [ctypes.c_char_p, ctypes.c_char_p]
        self.lib.procesarPlaca.restype = None

        self.lib.obtenerEstadoCeldas.argtypes = [ctypes.c_char_p]
        self.lib.obtenerEstadoCeldas.restype = None

