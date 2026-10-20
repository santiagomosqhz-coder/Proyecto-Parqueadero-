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

    #actualizacion de la interfaz
        self.root.configure(bg=self.bg_fondo)

        self.celdas_widgets = {}

        self._setup_ui()
        self.actualizar_grilla()
    #contenedor principal de la celdas
    def _setup_ui(self):
        main_container = tk.Frame(self.root, bg=self.bg_fondo, padx=10, pady=10)
        main_container.pack(fill="both", expand=True)

        # --- PARTE SUPERIOR: GRILLA DE CELDAS (27 puestos) ---
        frame_grilla = tk.LabelFrame(
            main_container, text=" Estado de Celdas (27) ",
            padx=10, pady=10, bg=self.bg_fondo, fg=self.titulo,
            font=("Segoe UI", 12, "bold"), highlightbackground=self.borde_panel, highlightthickness=1, bd=0
        )
        frame_grilla.pack(fill="x", padx=5, pady=5)

        for c in range(9):
            frame_grilla.columnconfigure(c, weight=1)

        for i in range(27):
            fila = i // 9
            col = i % 9

            cell_frame = tk.Frame(
                frame_grilla, width=115, height=65, bd=0,
                highlightbackground=self.libre_borde, highlightthickness=1.5, bg=self.libre_fondo
            )
            cell_frame.grid(row=fila, column=col, padx=5, pady=5, sticky="nsew")
            cell_frame.pack_propagate(False)

            lbl_num = tk.Label(cell_frame, text=f"Celda {i+1}", font=("Segoe UI", 9, "bold"), fg=self.texto, bg=self.libre_fondo)
            lbl_num.pack(pady=(4, 1))

            lbl_placa = tk.Label(cell_frame, text="LIBRE", font=("Segoe UI", 10, "bold"), fg=self.texto_secundario, bg=self.libre_fondo)
            lbl_placa.pack(pady=(0, 4))

            self.celdas_widgets[i] = {
                "frame": cell_frame,
                "placa_label": lbl_placa,
                "num_label": lbl_num
            }    #parte superior de la celda

            # --- BARRA INFERIOR: ADMINISTRADORAS (horizontal y pequeña) ---
        # Se empaca antes que el historial para que quede fija abajo.
        barra_admin = tk.Frame(
            main_container, bg=self.bg_panel,
            highlightbackground=self.borde_panel, highlightthickness=1, bd=0
        )
        barra_admin.pack(side="bottom", fill="x", padx=5, pady=(5, 0))

        lbl_nombres = tk.Label(
            barra_admin,
            text="SANTIAGO  &  YEISON",
            font=("Segoe UI", 10, "bold"),
            fg=self.nombres, bg=self.bg_panel
        )
        lbl_nombres.pack(side="left", padx=12, pady=4)

        lbl_itm = tk.Label(
            barra_admin, text="Estudiantes ITM",
            font=("Segoe UI", 9, "italic"),
            fg=self.texto_secundario, bg=self.bg_panel
        )
        lbl_itm.pack(side="right", padx=12, pady=4)

        # PARTE CENTRAL: HISTORIAL (ocupa todo el ancho) 
        frame_historial = tk.LabelFrame(
            main_container, text=" Historial de Eventos ",
            padx=10, pady=10, bg=self.bg_fondo, fg=self.titulo,
            font=("Segoe UI", 11, "bold"), highlightbackground=self.borde_panel, highlightthickness=1, bd=0
        )
        frame_historial.pack(fill="both", expand=True, padx=5, pady=5)

        style = ttk.Style()
        style.theme_use("clam")
        style.configure(
            "Treeview",
            background=self.bg_panel,
            fieldbackground=self.bg_panel,
            foreground=self.texto,
            rowheight=24,
            bd=0
        )
        style.configure("Treeview.Heading", background=self.encabezado, foreground=self.texto, font=("Segoe UI", 10, "bold"))
        style.map("Treeview.Heading", background=[("active", self.borde_panel)])
        style.map("Treeview", background=[("selected", self.libre_borde)], foreground=[("selected", self.texto)])
        style.configure(
            "Vertical.TScrollbar",
            background=self.libre_borde, troughcolor=self.bg_panel,
            bordercolor=self.bg_panel, arrowcolor=self.texto
        )

        columnas = ("hora", "placa", "celda", "estado")
        self.tabla = ttk.Treeview(frame_historial, columns=columnas, show="headings", height=6)

        self.tabla.heading("hora", text="Hora")
        self.tabla.heading("placa", text="Placa")
        self.tabla.heading("celda", text="Celda")
        self.tabla.heading("estado", text="Estado")

        self.tabla.column("hora", width=90, anchor="center")
        self.tabla.column("placa", width=120, anchor="center")
        self.tabla.column("celda", width=80, anchor="center")
        self.tabla.column("estado", width=120, anchor="center")

        scrollbar = ttk.Scrollbar(frame_historial, orient="vertical", command=self.tabla.yview)
        self.tabla.configure(yscroll=scrollbar.set)

        self.tabla.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
