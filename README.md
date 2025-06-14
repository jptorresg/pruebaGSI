# Kanban API – Prueba Técnica Desarrollador Backend Jr. en GSI

Este proyecto es una **API RESTful desarrollada con FastAPI** para la gestión de tareas tipo Kanban. Fue creado como parte de la prueba técnica para la posición de Desarrollador Backend Jr. en GSI.

Esta API permite **crear, consultar, actualizar, eliminar y avanzar tareas** a través de un flujo de estados previamente definido. Cada tarea avanza desde `stories` → `to_do` → `in_progress` → `testing` → `done`.

---

## Tecnologías utilizadas

- **Python 3.11**
- **FastAPI**
- **SQLAlchemy**
- **PostgreSQL**
- **Pydantic**
- **Uvicorn**
- **python-dotenv**
- **Postman**

---

## Estructura del proyecto

<pre>text kanban-api/
  ├── main.py                            # Entrypoint principal con todos los endpoints
  ├── models.py                          # Modelos SQLAlchemy para la base de datos 
  ├── schemas.py                         # Esquemas Pydantic para validación de datos
  ├── database.py                        # Configuración de la base de datos
  ├── utils.py                           # Lógica de transición de estados
  ├── .env                               # Variables de entorno (NO incluido en el repo)
  ├── .env.example                       # Plantilla del archivo .env
  ├── .gitignore                         # Archivos que Git debe ignorar
  ├── requirements.txt                   # Lista de dependencias del proyecto
  ├── README.md                          # Este archivo
  ├── KANBAN API.postman_collection.json # Colección Postman con todos los endpoints
  └── venv/                              # Entorno virtual (ignorado por Git)</pre>

---

## Instalación y ejecución

### 1. Clona el repositorio
```bash
git clone https://github.com/tuusuario/kanban-api.git
cd kanban-api
```

### 2. Crea y activa un entorno virtual
```bash
python -m venv venv
# En Windows:
venv\Scripts\activate
# En macOS/Linux:
source venv/bin/activate
```

### 3. Instala las dependencias
```bash
pip install -r requirements.txt
```

### 4. Configura tu base de datos
Crea un archivo `.env` en la raíz del proyecto basado en `.env.example`:
```bash
DATABASE_URL=postgresql://usuario:contraseña/@localhost/pruebagsi
```

### 5. Ejecuta la aplicación
```bash
uvicorn main:app --reload
```

### 6. Prueba la API
Accede a la documentación automática de FastAPI en tu navegador:<br>
Swagger UI: `http://127.0.0.1:8000/docs`<br>
Redoc: `http://127.0.0.1:8000/redoc`

---

## Endpoints disponibles

| Método | Endpoint                  | Descripción                      |
|--------|---------------------------|----------------------------------|
| POST   | `/tareas/`                | Crear una nueva tarea            |
| GET    | `/tareas/`                | Listar todas las tareas          |
| GET    | `/tareas/{id}`            | Obtener una tarea por ID         |
| PUT    | `/tareas/{id}`            | Editar una tarea existente       |
| DELETE | `/tareas/{id}`            | Eliminar una tarea               |
| PATCH  | `/tareas/{id}/avanzar`    | Avanzar el estado de una tarea   |

---

## Flujo de estados

Cada tarea debe avanzar secuencialmente a través de los siguientes estados:<br>
`stories → to_do → in_progress → testing → done`<br>
El endpoint `/tareas/{id}/avanzar` permite mover una tarea al siguiente estado automáticamente.

---

## Colección de Postman

La colección de pruebas se encuentra en el archivo:<br>
`KANBAN API.postman_collection.json`<br>
Incluye todos los endpoints y utiliza una variable `{{tarea_id}}` para facilitar las pruebas dinámicas.
Puedes importar esta colección directamente en Postman Web, Escritorio o desde la extensión de VS Code.

--- 

## Variables de entorno

Incluye una plantilla `.env.example`.<br>
Asegúrate de crear tu propio archivo `.env` con las credenciales reales de tu base de datos.

---

## Estado del proyecto

-  CRUD completo funcional
-  Flujo de estados implementado correctamente
-  Conexión a base de datos funcional (SQLite o PostgreSQL)
-  Código limpio, comentado y modular
-  Postman listo para pruebas

--- 

## Autor

Desarrollado por Juan Pablo Torres.<br>
Para la Prueba Técnica de GSI.

---

## Licencia

Este proyecto es de uso académico/técnico únicamente para evaluación en procesos de reclutamiento. No está licenciado para uso comercial.
