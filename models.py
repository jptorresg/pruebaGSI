# models.py
from sqlalchemy import Column, Integer, String, Enum
from database import Base
import enum

class TareaState(str, enum.Enum):
    stories = "stories"
    to_do = "to_do"
    in_progress = "in_progress"
    testing = "testing"
    done = "done"

class Tarea(Base):
    __tablename__ = "tareas"
    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String, index=True)
    descripcion = Column(String, nullable=True)
    estado = Column(String, default="stories")
