import tkinter as tk
from tkinter import ttk
from config.settings import CLIENTES, USUARIOS, ESTADOS


class IncidenciaView:

    def __init__(self):

        self.root = tk.Tk()
        self.root.title("Registro de incidencias")
        self.root.geometry("1100x650")

        self._crear_layout()

    def _crear_layout(self):

        self.frame_superior = tk.Frame(self.root, pady=10)
        self.frame_superior.pack(fill="x")

        self.frame_detalle = tk.Frame(self.root, pady=10)
        self.frame_detalle.pack(fill="x")

        self.frame_tabla = tk.Frame(self.root)
        self.frame_tabla.pack(fill="both", expand=True)

        self._crear_formulario_superior()
        self._crear_detalle()
        self._crear_tabla()

    # -----------------------------
    # FORMULARIO SUPERIOR
    # -----------------------------

    def _crear_formulario_superior(self):

        tk.Label(self.frame_superior, text="Cliente").grid(row=0, column=0)

        self.cliente = ttk.Combobox(self.frame_superior, values=CLIENTES)
        self.cliente.grid(row=0, column=1)

        tk.Label(self.frame_superior, text="Usuario").grid(row=0, column=2)

        self.usuario = ttk.Combobox(self.frame_superior, values=USUARIOS)
        self.usuario.grid(row=0, column=3)

        tk.Label(self.frame_superior, text="Estado").grid(row=0, column=4)

        self.estado = ttk.Combobox(self.frame_superior, values=ESTADOS)
        self.estado.grid(row=0, column=5)

        self.boton_guardar = tk.Button(self.frame_superior, text="Guardar")
        self.boton_guardar.grid(row=0, column=6, padx=20)

    # -----------------------------
    # DETALLE PROBLEMA / SOLUCION
    # -----------------------------

    def _crear_detalle(self):

        tk.Label(self.frame_detalle, text="Problema").grid(row=0, column=0)

        self.problema = tk.Text(self.frame_detalle, height=5, width=45)
        self.problema.grid(row=1, column=0)

        tk.Label(self.frame_detalle, text="Solución").grid(row=0, column=1)

        self.solucion = tk.Text(self.frame_detalle, height=5, width=45)
        self.solucion.grid(row=1, column=1)

        self.boton_modificar = tk.Button(
            self.frame_detalle,
            text="Modificar",
            state="disabled"
        )

        self.boton_modificar.grid(row=1, column=2, padx=20)

    # -----------------------------
    # TABLA
    # -----------------------------

    def _crear_tabla(self):

        columnas = (
            "ID",
            "Fecha",
            "Cliente",
            "Problema",
            "Solucion",
            "Usuario",
            "Estado"
        )

        self.tabla = ttk.Treeview(
            self.frame_tabla,
            columns=columnas,
            show="headings"
        )

        for col in columnas:

            self.tabla.heading(col, text=col)
            self.tabla.column(col, width=140)

        scrollbar = ttk.Scrollbar(
            self.frame_tabla,
            orient="vertical",
            command=self.tabla.yview
        )

        self.tabla.configure(yscroll=scrollbar.set)

        self.tabla.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

    # -----------------------------
    # VENTANA MODIFICACIÓN
    # -----------------------------

    def abrir_ventana_modificacion(self):

        ventana = tk.Toplevel(self.root)
        ventana.title("Modificar incidencia")
        ventana.geometry("400x300")

        # Cliente
        tk.Label(ventana, text="Cliente").grid(row=0, column=0, pady=5)

        cliente = ttk.Combobox(ventana, values=CLIENTES, width=30)
        cliente.grid(row=0, column=1)

        # Problema
        tk.Label(ventana, text="Problema").grid(row=1, column=0, pady=5)

        problema = tk.Text(ventana, height=3, width=30)
        problema.grid(row=1, column=1)

        # Solución
        tk.Label(ventana, text="Solución").grid(row=2, column=0, pady=5)

        solucion = tk.Text(ventana, height=3, width=30)
        solucion.grid(row=2, column=1)

        # Usuario
        tk.Label(ventana, text="Usuario").grid(row=3, column=0, pady=5)

        usuario = ttk.Combobox(ventana, values=USUARIOS, width=30)
        usuario.grid(row=3, column=1)

        # Estado
        tk.Label(ventana, text="Estado").grid(row=4, column=0, pady=5)

        estado = ttk.Combobox(ventana, values=ESTADOS, width=30)
        estado.grid(row=4, column=1)

        boton = tk.Button(ventana, text="Guardar cambios")
        boton.grid(row=5, column=0, columnspan=2, pady=15)

        return {
            "ventana": ventana,
            "cliente": cliente,
            "problema": problema,
            "solucion": solucion,
            "usuario": usuario,
            "estado": estado,
            "boton": boton
        }

    # -----------------------------

    def iniciar(self):

        self.root.mainloop()