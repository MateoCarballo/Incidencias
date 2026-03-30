from tkinter import messagebox

class IncidenciaController:

    def __init__(self, model, view):
        self.model = model
        self.view = view

        # Conectar botones a métodos
        self.view.boton_guardar.configure(command=self.guardar)
        self.view.boton_modificar.configure(command=self.modificar)
        self.view.boton_actualizar.configure(command=self.cargar_tabla)

        # Evento de la tabla de ttk
        self.view.tabla.bind("<<TreeviewSelect>>", self.fila_seleccionada)

        self.cargar_tabla()

    def cargar_tabla(self):
        for fila in self.view.tabla.get_children():
            self.view.tabla.delete(fila)

        try:
            incidencias = self.model.leer_incidencias()
            for inc in incidencias:
                self.view.tabla.insert("", "end", values=inc)
            # Reseteamos estado del botón por si alguien borró localmente la tabla
            self.view.boton_modificar.configure(state="disabled")
        except Exception as e:
            messagebox.showerror("Aviso del Sistema", str(e))

    def guardar(self):
        cliente = self.view.cliente.get()
        problema = self.view.problema.get("1.0", "end").strip()
        solucion = self.view.solucion.get("1.0", "end").strip()
        usuario = self.view.usuario.get()
        estado = self.view.estado.get()

        if not problema:
            messagebox.showwarning("Atención", "El campo problema no puede estar vacío.")
            return

        try:
            self.model.guardar_incidencia(cliente, problema, solucion, usuario, estado)
            # Limpiamos el formulario en caso de éxito
            self.view.problema.delete("1.0", "end")
            self.view.solucion.delete("1.0", "end")
            self.cargar_tabla()
        except Exception as e:
            messagebox.showerror("Error al guardar", str(e))

    def fila_seleccionada(self, event):
        if self.view.tabla.selection():
            self.view.boton_modificar.configure(state="normal")

    def modificar(self):
        seleccion = self.view.tabla.selection()
        if not seleccion:
            return

        item = self.view.tabla.item(seleccion)
        datos = item["values"]

        ventana = self.view.abrir_ventana_modificacion()

        # Rellenar datos actuales
        ventana["cliente"].set(datos[2])
        ventana["problema"].insert("1.0", datos[3])
        if str(datos[4]) and str(datos[4]) != "None":
            ventana["solucion"].insert("1.0", str(datos[4]))
        ventana["usuario"].set(datos[5])
        ventana["estado"].set(datos[6])

        def guardar_cambios():
            cliente = ventana["cliente"].get()
            problema = ventana["problema"].get("1.0", "end").strip()
            solucion = ventana["solucion"].get("1.0", "end").strip()
            usuario = ventana["usuario"].get()
            estado = ventana["estado"].get()

            if not problema:
                messagebox.showwarning("Atención", "El campo problema no puede estar vacío.")
                return

            nuevos = [cliente, problema, solucion, usuario, estado]

            try:
                self.model.actualizar_incidencia(datos[0], nuevos)
                self.cargar_tabla()
                ventana["ventana"].destroy()
            except Exception as e:
                messagebox.showerror("Error al actualizar", str(e))

        ventana["boton"].configure(command=guardar_cambios)