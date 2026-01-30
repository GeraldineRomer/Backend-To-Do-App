from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime
from sqlalchemy.sql import func
from app.core.database import Base

class Task(Base):
    __tablename__ = "tareas"
    
    id_tarea = Column(Integer, primary_key=True, index=True)
    titulo = Column(String(100), nullable=False)
    descripcion = Column(String(500), nullable=True)
    completado = Column(Boolean, default=False)
    id_usuario = Column(Integer, ForeignKey("usuarios.id_usuario"), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
