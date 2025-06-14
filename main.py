# main.py
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import models, schemas
from database import SessionLocal, engine
from fastapi.middleware.cors import CORSMiddleware

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Para permitir llamadas desde frontend local
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependency para obtener una sesión de base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ----------------- CRUD DE TAREAS -----------------

@app.post("/tareas/", response_model=schemas.Tarea)
def crear_tarea(tarea: schemas.TareaCrear, db: Session = Depends(get_db)):
    db_tarea = models.Tarea(**tarea.dict())
    db.add(db_tarea)
    db.commit()
    db.refresh(db_tarea)
    return db_tarea

@app.get("/tareas/", response_model=list[schemas.Tarea])
def listar_tareas(db: Session = Depends(get_db)):
    return db.query(models.Tarea).all()

@app.get("/tareas/{tarea_id}", response_model=schemas.Tarea)
def obtener_tarea(tarea_id: int, db: Session = Depends(get_db)):
    tarea = db.query(models.Tarea).filter(models.Tarea.id == tarea_id).first()
    if tarea is None:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    return tarea

@app.put("/tareas/{tarea_id}", response_model=schemas.Tarea)
def actualizar_tarea(tarea_id: int, tarea: schemas.TareaCrear, db: Session = Depends(get_db)):
    db_tarea = db.query(models.Tarea).filter(models.Tarea.id == tarea_id).first()
    if db_tarea is None:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    for key, value in tarea.dict().items():
        setattr(db_tarea, key, value)
    db.commit()
    db.refresh(db_tarea)
    return db_tarea

@app.delete("/tareas/{tarea_id}")
def eliminar_tarea(tarea_id: int, db: Session = Depends(get_db)):
    db_tarea = db.query(models.Tarea).filter(models.Tarea.id == tarea_id).first()
    if db_tarea is None:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    db.delete(db_tarea)
    db.commit()
    return {"mensaje": "Tarea eliminada correctamente"}

# ----------------- GESTIÓN DE ESTADOS -----------------

# Flujo de estados válido
state_flow = {
    "stories": "to_do",
    "to_do": "in_progress",
    "in_progress": "testing",
    "testing": "done",
    "done": None
}

@app.patch("/tareas/{tarea_id}/avanzar", response_model=schemas.Tarea)
def avanzar_estado_tarea(tarea_id: int, db: Session = Depends(get_db)):
    tarea = db.query(models.Tarea).filter(models.Tarea.id == tarea_id).first()
    if not tarea:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")

    estado_actual = tarea.estado
    siguiente_estado = state_flow.get(estado_actual)

    if not siguiente_estado:
        raise HTTPException(status_code=400, detail="La tarea ya está en el estado final")

    tarea.estado = siguiente_estado
    db.commit()
    db.refresh(tarea)
    return tarea
