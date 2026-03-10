class IncidenciaController:

    def __init__(self, model, view):

        self.model = model
        self.view = view

        self.view.boton_guardar.config(command=self.guardar)
        self.view.boton_modificar.config(command=self.modificar)

        self.view.tabla.bind("<<TreeviewSelect>>", self.fila_seleccionada)

        self.cargar_tabla()


    def cargar_tabla(self):

        for fila in self.view.tabla.get_children():
            self.view.tabla.delete(fila)

        incidencias = self.model.leer_incidencias()

        for inc in incidencias:
            self.view.tabla.insert("", "end", values=inc)


    def guardar(self):

        cliente = self.view.cliente.get()

        problema = self.view.problema.get("1.0", "end").strip()

        solucion = self.view.solucion.get("1.0", "end").strip()

        usuario = self.view.usuario.get()

        estado = self.view.estado.get()

        self.model.guardar_incidencia(
            cliente,
            problema,
            solucion,
            usuario,
            estado
        )

        self.view.problema.delete("1.0", "end")
        self.view.solucion.delete("1.0", "end")

        self.cargar_tabla()


    def fila_seleccionada(self, event):

        if self.view.tabla.selection():
            self.view.boton_modificar.config(state="normal")


    def modificar(self):

        seleccion = self.view.tabla.selection()

        if not seleccion:
            return

        item = self.view.tabla.item(seleccion)

        datos = item["values"]

        ventana = self.view.abrir_ventana_modificacion()

        def guardar_cambios():

            cliente = ventana["cliente"].get()

            problema = ventana["problema"].get("1.0", "end").strip()

            solucion = ventana["solucion"].get("1.0", "end").strip()

            usuario = ventana["usuario"].get()

            estado = ventana["estado"].get()

            nuevos = [
                cliente,
                problema,
                solucion,
                usuario,
                estado
            ]

            self.model.actualizar_incidencia(datos[0], nuevos)

            self.cargar_tabla()

            ventana["ventana"].destroy()

        ventana["boton"].config(command=guardar_cambios)