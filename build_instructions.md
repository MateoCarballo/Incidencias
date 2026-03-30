# Guía de Despliegue: App de Incidencias (.exe)

¡Hola Mateo! Contestando a tu pregunta: **Sí, es una idea excelente**. 
Dejar el `.exe` en una carpeta compartida y que cada usuario se copie ese archivo a su escritorio (o desde donde lo quieran ejecutar localmente) y apunte al `settings.json` o al CSV es el **mejor enfoque** (y el más profesional) para este escenario.

**¿Por qué es buena idea?**
1. **Rendimiento**: La interfaz gráfica carga en el PC local sin depender de la red, por lo que será instantánea.
2. **Sin bloqueos (Locks)**: Si 5 personas ejecutan el MISMO `.exe` desde la carpeta compartida a la vez, Windows bloqueará ese ejecutable. Si un día quieres lanzar la versión 2.0 de tu app, tendrás que pedirle a todos que lo cierren para poder borrar y reemplazar el archivo en el servidor. Al copiarlo al equipo local, ese problema desaparece. Solo se comparte el CSV!
3. **Descentralización y portabilidad extrema**: Nadie nota qué pasa por detrás.

> [!NOTE]
> Configuración del entorno real
> 
> En tu carpeta local de tu PC de programador (`c:/Users/Mateo/Desktop/Incidencias`), en `config/settings.json`, tienes que cambiar la ruta del CSV por la ruta ABSOLUTA de tu carpeta compartida en la red. 
> Ejemplo: `"ARCHIVO_CSV": "Z:\\Compartida_IT\\incidencias.csv"` o `"\\192.168.1.10\Publico\incidencias.csv"`
>
> Si el archivo no existe, la primera vez que un usuario abra la app, se generará el modelo base y los encabezados de forma automática en la red.

---

## 🛠️ Paso a Paso: Cómo Generar el .exe

Para llevar la app a las máquinas, debes compilar el código. Usaremos `PyInstaller`.

### 1. Preparar el Entorno (Instalar Dependencias)
Abre tu terminal (PowerShell o CMD) dentro del directorio `c:\Users\Mateo\Desktop\Incidencias` y lanza estos comandos para asegurar que tienes los paquetes requeridos por el código moderno que hemos añadido:

```bash
pip install customtkinter
pip install pyinstaller
```

### 2. Generar el Ejecutable (.exe)
Continúa en tu terminal y escribe el siguiente comando que empaquetará todo (el código y las librerías, permitiendo a CustomTkinter y Tkinter ir dentro del archivo para que los demas no deban instalar Python):

```bash
pyinstaller --noconfirm --onedir --windowed --add-data "config;config/"  "main.py"
```

**Explicación de las flags:**
- `--onedir` o `--onefile`: Recomendable en directorios para arrancar mas rapido. Puedes sustituir `--onedir` por `--onefile` si solo quieres un único `.exe` y ningún folder mágico atado de carpetas (puede ser un poco más lento de arrancar). Usaremos `onefile` en todo caso a ser el mas comodo de trasladar:
  `pyinstaller --noconfirm --onefile --windowed --add-data "config;config/"  "main.py"`
- `--windowed`: Hace que no aparezca una molesta pantalla negra (Consola) por detrás del programa gráfico.
- `--add-data`: Como tenemos una carpeta `config` vital para el `settings.json`, hay que decirle a PyInstaller que se la lleve con la instalación.

### 3. Distribución (Tu plan maestro)
Una vez que el comando finalice, PyInstaller habrá creado 2 carpetas nuevas (`build` y `dist`).
1. Entra a la carpeta `/dist/` y observarás un reluciente `main.exe`. Puedes renombrarlo a `GestorIncidencias.exe`.
2. Como has empaquetado `settings.json` mediante `--add-data`, o bien si has hecho mode file suelto y no se actualiza, la mejor recomendación (para que los clientes, usuarios y estados se puedan modificar al vuelo en la carpeta compartida en un futuro por _ti_ sin recompilar) es **tener el *settings.json* en la misma ruta compartida que el .exe**!
   > *Pro tip: Si editas tu `settings.py` podrías hacerlo buscar el .json en el mismo directorio de red. Para esta versión se preempaqueta. ¡Si quisieras editar la lista de clientes o empleados tras el empaquetado, tendríais que recompilar la pequeña lista!*
3. Pásalo a tus compañeros, ellos lo lanzan en su pc local, y **magia**. Todos listos.
