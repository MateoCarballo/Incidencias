import customtkinter as ctk
from tkinter import ttk
from config.settings import CLIENTES, USUARIOS, ESTADOS

ctk.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


class IncidenciaView:
    # Declaraciones de tipo para atributos de la clase (evita advertencias del linter)
    frame_superior: ctk.CTkFrame
    frame_detalle: ctk.CTkFrame
    frame_tabla: ctk.CTkFrame
    cliente: ctk.CTkComboBox
    usuario: ctk.CTkComboBox
    estado: ctk.CTkComboBox
    boton_guardar: ctk.CTkButton
    problema: ctk.CTkTextbox
    solucion: ctk.CTkTextbox
    boton_modificar: ctk.CTkButton
    boton_actualizar: ctk.CTkButton
    tabla: ttk.Treeview

    def __init__(self):
        self.root = ctk.CTk()
        self.root.title("Registro de Incidencias Profesionales")
        self.root.geometry("1150x700")

        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_rowconfigure(2, weight=1)

        self._crear_layout()

    def _crear_layout(self):
        # Frame Superior (Formulario)
        self.frame_superior = ctk.CTkFrame(self.root, corner_radius=10)
        self.frame_superior.grid(row=0, column=0, padx=20, pady=(20, 10), sticky="ew")

        # Frame Detalle
        self.frame_detalle = ctk.CTkFrame(self.root, corner_radius=10)
        self.frame_detalle.grid(row=1, column=0, padx=20, pady=10, sticky="ew")

        # Frame Tabla
        self.frame_tabla = ctk.CTkFrame(self.root, corner_radius=10)
        self.frame_tabla.grid(row=2, column=0, padx=20, pady=(10, 20), sticky="nsew")

        self._crear_formulario_superior()
        self._crear_detalle()
        self._crear_tabla()

    def _crear_formulario_superior(self):
        self.frame_superior.grid_columnconfigure((0, 2, 4, 6), weight=0)
        self.frame_superior.grid_columnconfigure((1, 3, 5), weight=1)

        ctk.CTkLabel(self.frame_superior, text="Cliente:", font=("Roboto", 14, "bold")).grid(row=0, column=0, padx=10, pady=15, sticky="e")
        self.cliente = ctk.CTkComboBox(self.frame_superior, values=CLIENTES)
        self.cliente.grid(row=0, column=1, padx=10, pady=15, sticky="ew")

        ctk.CTkLabel(self.frame_superior, text="Usuario:", font=("Roboto", 14, "bold")).grid(row=0, column=2, padx=10, pady=15, sticky="e")
        self.usuario = ctk.CTkComboBox(self.frame_superior, values=USUARIOS)
        self.usuario.grid(row=0, column=3, padx=10, pady=15, sticky="ew")

        ctk.CTkLabel(self.frame_superior, text="Estado:", font=("Roboto", 14, "bold")).grid(row=0, column=4, padx=10, pady=15, sticky="e")
        self.estado = ctk.CTkComboBox(self.frame_superior, values=ESTADOS)
        self.estado.grid(row=0, column=5, padx=10, pady=15, sticky="ew")

        self.boton_guardar = ctk.CTkButton(self.frame_superior, text="Guardar Incidencia", font=("Roboto", 14, "bold"))
        self.boton_guardar.grid(row=0, column=6, padx=20, pady=15)

    def _crear_detalle(self):
        self.frame_detalle.grid_columnconfigure((0, 1), weight=1)

        ctk.CTkLabel(self.frame_detalle, text="Problema:", font=("Roboto", 14, "bold")).grid(row=0, column=0, padx=10, pady=(10, 0), sticky="w")
        self.problema = ctk.CTkTextbox(self.frame_detalle, height=80)
        self.problema.grid(row=1, column=0, padx=10, pady=(5, 15), sticky="ew")

        ctk.CTkLabel(self.frame_detalle, text="Solución:", font=("Roboto", 14, "bold")).grid(row=0, column=1, padx=10, pady=(10, 0), sticky="w")
        self.solucion = ctk.CTkTextbox(self.frame_detalle, height=80)
        self.solucion.grid(row=1, column=1, padx=10, pady=(5, 15), sticky="ew")

        frame_botones = ctk.CTkFrame(self.frame_detalle, fg_color="transparent")
        frame_botones.grid(row=0, column=2, rowspan=2, padx=20, pady=15, sticky="n")

        self.boton_modificar = ctk.CTkButton(frame_botones, text="Modificar Selección", state="disabled", font=("Roboto", 13))
        self.boton_modificar.pack(fill="x", pady=5)
        
        self.boton_actualizar = ctk.CTkButton(frame_botones, text="↻ Actualizar Datos", fg_color="#E67E22", hover_color="#D35400", font=("Roboto", 13, "bold"))
        self.boton_actualizar.pack(fill="x", pady=5)

    def _crear_tabla(self):
        style = ttk.Style()
        style.theme_use("default")
        style.configure("Treeview", 
                        background="#2b2b2b",
                        foreground="white",
                        rowheight=30,
                        fieldbackground="#2b2b2b",
                        bordercolor="#343638",
                        borderwidth=0,
                        font=("Roboto", 11))
        style.map('Treeview', background=[('selected', '#22559b')])
        style.configure("Treeview.Heading",
                        background="#565b5e",
                        foreground="white",
                        relief="flat",
                        font=("Roboto", 12, "bold"))
        style.map("Treeview.Heading", background=[('active', '#3484F0')])

        columnas = ("ID", "Fecha", "Cliente", "Problema", "Solucion", "Usuario", "Estado")

        self.tabla = ttk.Treeview(self.frame_tabla, columns=columnas, show="headings", style="Treeview")

        anchos = {"ID": 50, "Fecha": 130, "Cliente": 130, "Problema": 300, "Solucion": 300, "Usuario": 100, "Estado": 100}
        for col in columnas:
            self.tabla.heading(col, text=col)
            self.tabla.column(col, width=anchos.get(col, 100), anchor="w" if col in ["Problema", "Solucion"] else "center")

        scrollbar = ctk.CTkScrollbar(self.frame_tabla, orientation="vertical", command=self.tabla.yview)
        # Fix for yscrollcommand argument to use the correct variable
        self.tabla.configure(yscrollcommand=scrollbar.set)

        self.tabla.pack(side="left", fill="both", expand=True, padx=(10, 0), pady=10)
        scrollbar.pack(side="right", fill="y", padx=5, pady=10)

    def abrir_ventana_modificacion(self):
        ventana = ctk.CTkToplevel(self.root)
        ventana.title("Modificar Incidencia")
        ventana.geometry("500x550")
        ventana.attributes("-topmost", True)
        ventana.grab_set()

        ventana.grid_columnconfigure(0, weight=0)
        ventana.grid_columnconfigure(1, weight=1)

        ctk.CTkLabel(ventana, text="Cliente:", font=("Roboto", 13, "bold")).grid(row=0, column=0, padx=20, pady=15, sticky="e")
        cliente = ctk.CTkComboBox(ventana, values=CLIENTES)
        cliente.grid(row=0, column=1, padx=(0, 20), pady=15, sticky="ew")

        ctk.CTkLabel(ventana, text="Problema:", font=("Roboto", 13, "bold")).grid(row=1, column=0, padx=20, pady=15, sticky="ne")
        problema = ctk.CTkTextbox(ventana, height=80)
        problema.grid(row=1, column=1, padx=(0, 20), pady=15, sticky="ew")

        ctk.CTkLabel(ventana, text="Solución:", font=("Roboto", 13, "bold")).grid(row=2, column=0, padx=20, pady=15, sticky="ne")
        solucion = ctk.CTkTextbox(ventana, height=80)
        solucion.grid(row=2, column=1, padx=(0, 20), pady=15, sticky="ew")

        ctk.CTkLabel(ventana, text="Usuario:", font=("Roboto", 13, "bold")).grid(row=3, column=0, padx=20, pady=15, sticky="e")
        usuario = ctk.CTkComboBox(ventana, values=USUARIOS)
        usuario.grid(row=3, column=1, padx=(0, 20), pady=15, sticky="ew")

        ctk.CTkLabel(ventana, text="Estado:", font=("Roboto", 13, "bold")).grid(row=4, column=0, padx=20, pady=15, sticky="e")
        estado = ctk.CTkComboBox(ventana, values=ESTADOS)
        estado.grid(row=4, column=1, padx=(0, 20), pady=15, sticky="ew")

        boton = ctk.CTkButton(ventana, text="Guardar Cambios", font=("Roboto", 14, "bold"))
        boton.grid(row=5, column=0, columnspan=2, pady=25)

        return {
            "ventana": ventana,
            "cliente": cliente,
            "problema": problema,
            "solucion": solucion,
            "usuario": usuario,
            "estado": estado,
            "boton": boton
        }

    def iniciar(self):
        self.root.mainloop()