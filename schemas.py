# schemas.py
from pydantic import BaseModel

class TareaBase(BaseModel):
    titulo: str
    descripcion: str
    estado: str = "stories"  # por defecto

class TareaCrear(TareaBase):
    pass  # igual a TareaBase, pero lo dejamos separado por si luego se modifica

class Tarea(TareaBase):
    id: int

    class Config:
        orm_mode = True  # permite compatibilidad con SQLAlchemy
