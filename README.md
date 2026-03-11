<div align="center">
  <h1>🛠️ Incidencias</h1>
  <p><strong>Registro y seguimiento de incidencias técnicas — rápido, portable y sin dependencias externas.</strong></p>

  <p>
    <a href="https://www.python.org/downloads/"><img src="https://img.shields.io/badge/python-3.10%2B-blue?style=flat-square&logo=python&logoColor=white" alt="Python 3.10+"></a>
    <img src="https://img.shields.io/badge/UI-Tkinter-orange?style=flat-square" alt="Tkinter">
    <img src="https://img.shields.io/badge/storage-CSV-brightgreen?style=flat-square" alt="CSV">
    <img src="https://img.shields.io/badge/arquitectura-MVC-blueviolet?style=flat-square" alt="MVC">
    <img src="https://img.shields.io/badge/licencia-MIT-yellow?style=flat-square" alt="MIT">
    <img src="https://img.shields.io/badge/plataforma-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey?style=flat-square" alt="Multiplataforma">
  </p>

  <br/>

  > **Sin base de datos. Sin servidor. Sin instalación complicada.**  
  > Solo Python y un archivo CSV que puedes llevar a cualquier sitio.

</div>

---

## ¿Por qué Incidencias?

La mayoría de herramientas de gestión de incidencias son complejas, requieren conexión a internet o son difíciles de instalar en entornos corporativos restringidos. **Incidencias** nació para resolver eso:

```
✔  Funciona offline al 100%
✔  Instalación en menos de 2 minutos
✔  Toda la configuración en un JSON legible
✔  Portátil — copia la carpeta y funciona
✔  Sin bases de datos externas ni servidores
```

---

## Funcionalidades

<table>
  <tr>
    <td>➕ <strong>Nueva incidencia</strong></td>
    <td>Registra cliente, problema, solución, técnico y estado desde un formulario limpio</td>
  </tr>
  <tr>
    <td>📋 <strong>Listado completo</strong></td>
    <td>Tabla con scroll que muestra todas las incidencias ordenadas por ID</td>
  </tr>
  <tr>
    <td>✏️ <strong>Edición inline</strong></td>
    <td>Selecciona cualquier fila y modifica sus campos desde una ventana emergente</td>
  </tr>
  <tr>
    <td>⚙️ <strong>Config centralizada</strong></td>
    <td>Clientes, técnicos y estados se gestionan desde un único <code>settings.json</code></td>
  </tr>
  <tr>
    <td>💾 <strong>Persistencia automática</strong></td>
    <td>Cada cambio se guarda instantáneamente en CSV, sin botón de "exportar"</td>
  </tr>
</table>

---

## Inicio rápido

### 1 — Clona el repositorio

```bash
git clone https://github.com/viagalicia/Incidencias.git
cd Incidencias
```

### 2 — Crea el entorno virtual

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux / macOS
source venv/bin/activate
```

### 3 — Configura tus datos

Edita `config/settings.json` con los valores de tu organización:

```json
{
    "ARCHIVO_CSV": "incidencias.csv",
    "CLIENTES":  ["Empresa A", "Empresa B", "Empresa C"],
    "USUARIOS":  ["Ana García", "Carlos López", "María Pérez"],
    "ESTADOS":   ["Abierta", "En proceso", "Resuelta", "Cerrada"]
}
```

### 4 — Ejecuta

```bash
python main.py
```

> ℹ️ El archivo `incidencias.csv` se crea automáticamente en el primer arranque si no existe.

---

## Estructura del proyecto

```
Incidencias/
│
├── config/
│   ├── __init__.py
│   ├── settings.py          # Lee y exporta variables desde el JSON
│   └── settings.json        # ← único archivo que necesitas editar
│
├── controller/
│   └── incidencias_controller.py
│
├── model/
│   └── incidencias_model.py
│
├── view/
│   └── incidencias_view.py
│
├── incidencias.csv          # Generado automáticamente
├── main.py
└── README.md
```

---

## Arquitectura

El proyecto sigue el patrón **MVC** de forma estricta, lo que hace que cada capa sea fácilmente reemplazable:

```
┌──────────────────────────────────────────────────────┐
│                       main.py                        │
└──────────────────────┬───────────────────────────────┘
                       │ instancia
                       ▼
┌──────────────────────────────────────────────────────┐
│               IncidenciaController                   │
│  • Escucha eventos de la View                        │
│  • Llama al Model para leer/escribir                 │
│  • Devuelve resultados a la View                     │
└────────────┬─────────────────────────┬───────────────┘
             │                         │
             ▼                         ▼
┌────────────────────┐     ┌───────────────────────┐
│  IncidenciaModel   │     │    IncidenciaView      │
│  • Lee CSV         │     │    • Tkinter GUI        │
│  • Escribe CSV     │     │    • Tabla + formulario │
│  • Valida IDs      │     │    • Ventana edición    │
└────────────────────┘     └───────────────────────┘
```

---

## Requisitos

| Requisito | Versión mínima |
|-----------|---------------|
| Python    | 3.10          |
| Tkinter   | Incluido con Python |

Sin dependencias externas de terceros. `pip install` no es necesario.

---

## Contribuir

Las contribuciones son bienvenidas. Para cambios importantes, abre primero un _issue_ describiendo lo que quieres cambiar.

```bash
# 1. Haz un fork del repositorio
# 2. Crea una rama para tu funcionalidad
git checkout -b feature/mi-mejora

# 3. Haz commit de tus cambios
git commit -m "feat: descripción del cambio"

# 4. Abre un Pull Request
```

---

## Licencia

Distribuido bajo la licencia **MIT**. Consulta el archivo `LICENSE` para más información.

---

<div align="center">
  <sub>Construido con Python · Diseñado para funcionar en cualquier sitio</sub>
</div>
