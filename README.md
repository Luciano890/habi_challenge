# Reto Backend Developer por: Luciano Chavarria

---

## Tecnologías a usar:

- **Python3.10+** 🐍
    - mysql-connector-python
    - pytest
- ************Docker************ 🐳
    - Dockerfile
    - docker compose

## ¿Cómo abordar el reto?

Para este reto se crearon 2 microservicios, uno (ms_get_properties) para el ******API****** el cual soporta peticiones **GET,**  y posee una arquitectura inspirada en Frameworks famosos para el desarrollo Backend en Python tales como [FastAPI](https://fastapi.tiangolo.com/) y [Django](https://www.djangoproject.com/), el segundo (ms_likes_properties) el cual busca explicar como integrar un sistema de “me gusta” para las propiedades de **Habi.**

1. Para abordar el primer MS se debe tener en cuenta las siguientes características desde Backend
    1. Servidor WEB, el cual sirva para el levantamiento de la aplicación, el registro de las peticiones y registre las actividades del API en un todo.
    2. Un Driver de conexión a la BBDD, el cual permita crear una conexión del servidor hacia la BBDD MySQL.
    3. Una arquitectura tipo REST la cual permita mantener y gestionar el área de Backend.
2. Para abordar el segundo MS se debe tener en cuenta las siguientes características desde Backend
    1. Una tabla en la base de datos que almacene los datos de los "me gusta" de las propiedades. Esta tabla debería tener al menos dos columnas: una para almacenar el ID del usuario que dio like y otra para almacenar el ID de la propiedad que recibió el like.

## Dudas

- ¿Cómo iniciar la aplicación?

Primero que todo se debe crear archivos llamado `.env` dentro de **ms_get_properties** con los siguientes datos

```bash
PORT=8000
HOST=127.0.0.1
DB_HOST=3.138.156.32
DB_PORT=3309
DB_USER=pruebas
DB_PASSWORD=VGbt3Day5R
DB_SCHEMA=habi_db
```

Los cuales se puede editar según se requiera, después de esto se debe usar los requerimientos para el uso correcto de la aplicación, los cuales estarán dentro de `requirements.txt` para hacer esto se deben seguir los siguientes pasos (desde la raíz del proyecto):

1. Con Python `python -m venv .venv`  y para activar el entorno virtual `source .venv/bin/activate` (Desde Linux).
2. Para verificar que se halla realizado de forma correcta el anterior paso debe salir en la consola el prefijo `(.venv)` .
3. Ahora `pip install -r requirements.txt` para instalar los requerimientos.
4. Cambiar nuevamente a **ms_get_properties `cd ms_get_properties`** y ejecutar con `python main.py`

Ahora desde la consola debe salir

```bash
Server started at http://localhost:8000; close with (Ctrl + C)
```

Felicitaciones! ahora se pueden realizar las peticiones

- ¿Cómo realizar las peticiones de consulta?

El endpoint tiene la siguiente estructura

```bash
curl --location 'http://localhost:8000/properties/available-to-users/?city={{str}}&year={{int}}&status={{int}}&operator={{str}}'
```

Todos los query params son opcionales

1. **city** = ciudad donde se encuentra el inmueble
2. ****************************************************************************year =**************************************************************************** Año de publicación del inmueble
3. **status =** Estado del inmueble
4. **********************operator =********************** Operador con el cual se realizan las consultas (por defecto es “and”, la otra opción es “or”)
- ¿Cómo ejecutar los Test Unitarios?

Ya con el entorno virtual y la instalación de los requerimientos, ejecutar desde **ms_get_properties** `python -m pytest core/tests -v`

Ejemplo:

![Untitled](Reto%20Backend%20Developer%20por%20Luciano%20Chavarria%20a03cdd90cbbf420d9078937be9255653/Untitled.png)

- ¿Por que hay un `"code": 1000` en la respuesta?

Por buenas practicas este código sirve como ayuda en adición del 200 que por defecto retorna el servidor, con este código se puede identificar el tipo de respuesta y desde que endpoint se realizo lo que facilita la trazabilidad de la aplicación.

---

## JSON de ejemplo desde Frontend

```json
{
  "city": "bogota",
  "year": 2018,
}
```

## Aplicación en acción 🚀

![Untitled](Reto%20Backend%20Developer%20por%20Luciano%20Chavarria%20a03cdd90cbbf420d9078937be9255653/Untitled%201.png)

---

## Ejecutar con Docker

1. Asegurar de tener un archivo `.env` en el **ms_get_properties** 
2. Desde la raíz del proyecto ejecutar `docker-compose up -d`
3. Listo 😃