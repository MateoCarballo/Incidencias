import csv
import os
import time
from datetime import datetime
from config.settings import ARCHIVO_CSV


class IncidenciaModel:

    def __init__(self):
        self._crear_csv()

    def _crear_csv(self):
        # Crear los directorios padre si es que fuera una ruta absoluta compleja nueva
        directorio = os.path.dirname(ARCHIVO_CSV)
        if directorio and not os.path.exists(directorio):
            try:
                os.makedirs(directorio)
            except OSError:
                pass # Fallar silenciosamente si no hay permisos, intentará crear el archivo abajo

        if not os.path.exists(ARCHIVO_CSV):
            with open(ARCHIVO_CSV, "w", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow([
                    "id", "fecha", "cliente", "problema",
                    "solucion", "usuario", "estado"
                ])

    def leer_incidencias(self):
        intentos = 3
        while intentos > 0:
            try:
                with open(ARCHIVO_CSV, "r", encoding="utf-8") as f:
                    reader = list(csv.reader(f))
                    if len(reader) <= 1:
                        return []
                    return reader[1:]
            except PermissionError:
                time.sleep(0.5)
                intentos -= 1
        raise Exception("El archivo CSV está siendo usado por otro programa o usuario. No se pudo leer.")

    def obtener_siguiente_id(self):
        incidencias = self.leer_incidencias()
        if not incidencias:
            return 1
        return int(incidencias[-1][0]) + 1

    def guardar_incidencia(self, cliente, problema, solucion, usuario, estado):
        # Al añadir, obtenemos el ID justo antes de escribir intentando no colisionar
        intentos = 3
        while intentos > 0:
            try:
                siguiente_id = self.obtener_siguiente_id()
                nueva = [
                    siguiente_id,
                    datetime.now().strftime("%Y-%m-%d %H:%M"),
                    cliente,
                    problema,
                    solucion,
                    usuario,
                    estado
                ]
                with open(ARCHIVO_CSV, "a", newline="", encoding="utf-8") as f:
                    writer = csv.writer(f)
                    writer.writerow(nueva)
                return True
            except PermissionError:
                time.sleep(0.5)
                intentos -= 1
        
        raise Exception("El archivo CSV está siendo usado. No se pudo guardar la incidencia.")

    def actualizar_incidencia(self, id_incidencia, nuevos):
        intentos = 3
        while intentos > 0:
            try:
                # 1. Leer el estado más reciente SIEMPRE antes de modificar
                incidencias = self.leer_incidencias()

                # 2. Modificar en memoria
                for inc in incidencias:
                    if inc[0] == str(id_incidencia):
                        for i, valor in enumerate(nuevos):
                            if valor != "":
                                inc[i+2] = valor
                        break

                # 3. Escribir de nuevo todo el archivo completo (modo W sobreescribe)
                with open(ARCHIVO_CSV, "w", newline="", encoding="utf-8") as f:
                    writer = csv.writer(f)
                    writer.writerow([
                        "id", "fecha", "cliente", "problema",
                        "solucion", "usuario", "estado"
                    ])
                    writer.writerows(incidencias)
                return True
            except PermissionError:
                time.sleep(0.5)
                intentos -= 1

        raise Exception("El archivo CSV está siendo usado. No se pudo actualizar la incidencia.")