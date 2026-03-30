# Guía de Puesta en Marcha y Despliegue (.exe)

Sigue estos pasos para compilar la aplicación, configurar las rutas de red y distribuirla al resto del equipo.

## 1. Configurar la Ruta del CSV en Red
Antes de compilar, debemos indicarle a la aplicación dónde va a vivir el archivo de datos (CSV) compartido.

1. Abre el archivo `config/settings.json` en tu editor de código.
2. Modifica el valor de `"ARCHIVO_CSV"` para que apunte a la **ruta de red (UNC)** o a la **letra de unidad compartida** donde guardaréis el archivo.
   - *Ejemplo UNC:* `"\\\\Servidor\\Carpeta_IT\\incidencias.csv"` *(Nota: en el JSON debes usar doble barra invertida `\\` para que sea válida).*
   - *Ejemplo Unidad (si todos tienen mapeada la unidad Z):* `"Z:\\Carpeta_IT\\incidencias.csv"`

## 2. Compilar el Ejecutable (.exe)
Vamos a empaquetar el código Python y su configuración en un único archivo `.exe` para que nadie más tenga que instalar Python.

1. Abre la terminal en el propio proyecto (`c:\Users\Mateo\Desktop\Incidencias`).
2. Ejecuta el comando de compilación:
   ```bash
   pyinstaller --noconfirm --onefile --windowed --add-data "config;config/" "main.py"
   ```

**¿Qué hace este comando?**
- `--onefile`: Junta todo en un solo `.exe`.
- `--windowed`: Oculta la molesta consola negra por detrás (solo se ve la interfaz gráfica).
- `--add-data`: Mete tu `settings.json` (con las rutas de red y usuarios/clientes que hayas puesto) dentro del código del `.exe`.

## 3. Localizar el Archivo Generado
- Una vez finalice el comando, verás que se han creado nuevas carpetas (`build` y `dist`).
- Entra en la carpeta `dist`. Allí estará tu flamante `main.exe`.
- Puedes renombrarlo tranquilamente a lo que quieras, por ejemplo: `GestorIncidencias.exe`.

## 4. Distribuir a los Usuarios
Aquí viene la magia del despliegue para que "las rutas se configuren solas":

1. Coge ese `GestorIncidencias.exe` y súbelo a vuestra **carpeta compartida** de la empresa.
2. Dile a tus compañeros que entren a esa carpeta, **COPIEN el `.exe`** y lo **PEGUEN en sus escritorios** locales.
3. Ya pueden hacer doble clic en su copia local.

Al estar en local, la interfaz cargará rapidísimo en todos los PCs sin consumir red ni bloquear el archivo ejecutable. Y como en el paso 1 insertaste la ruta de red en el código, el programa automáticamente viajará por la red para leer/escribir en el `incidencias.csv` compartido sin que ellos configuren nada.

### Dudas Frecuentes del Uso Diario
- **Añadir Incidencia:** Si alguien rellena el formulario y guarda, su propia tabla se actualizará automáticamente mostrando su línea.
- **Botón Actualizar:** Si *Compañero A* añade algo, *Compañero B* solo tiene que hacer clic en "Actualizar" para refrescar la tabla y ver los datos nuevos introducidos por *A*.
- **Cambiar listas (Clientes/Estados):** Si un día quieres agregar un nuevo cliente al desplegable, simplemente lo añades a tu `settings.json` local en el código, vuelves a lanzar el comando del Paso 2, y subes el nuevo `.exe` a la carpeta compartida pidiendo al equipo que se lo copien de nuevo.
