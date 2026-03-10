import csv
import os
from datetime import datetime
from config.settings import ARCHIVO_CSV


class IncidenciaModel:

    def __init__(self):
        self._crear_csv()

    def _crear_csv(self):

        if not os.path.exists(ARCHIVO_CSV):

            with open(ARCHIVO_CSV, "w", newline="", encoding="utf-8") as f:

                writer = csv.writer(f)

                writer.writerow([
                    "id",
                    "fecha",
                    "cliente",
                    "problema",
                    "solucion",
                    "usuario",
                    "estado"
                ])

    def leer_incidencias(self):

        with open(ARCHIVO_CSV, "r", encoding="utf-8") as f:

            reader = list(csv.reader(f))

            if len(reader) <= 1:
                return []

            return reader[1:]

    def obtener_siguiente_id(self):

        incidencias = self.leer_incidencias()

        if not incidencias:
            return 1

        return int(incidencias[-1][0]) + 1

    def guardar_incidencia(self, cliente, problema, solucion, usuario, estado):

        nueva = [
            self.obtener_siguiente_id(),
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

    def actualizar_incidencia(self, id_incidencia, nuevos):

        incidencias = self.leer_incidencias()

        for inc in incidencias:

            if inc[0] == str(id_incidencia):

                for i, valor in enumerate(nuevos):

                    if valor != "":
                        inc[i+2] = valor

        with open(ARCHIVO_CSV, "w", newline="", encoding="utf-8") as f:

            writer = csv.writer(f)

            writer.writerow([
                "id",
                "fecha",
                "cliente",
                "problema",
                "solucion",
                "usuario",
                "estado"
            ])

            writer.writerows(incidencias)