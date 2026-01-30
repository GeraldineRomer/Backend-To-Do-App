from pydantic import BaseModel
from typing import Optional

class TaskBase(BaseModel):
    titulo: str
    descripcion: Optional[str] = None
    completado: bool = False
    
class TaskCreate(TaskBase):
    pass

class TaskResponse(TaskBase):
    id_tarea: int
    
    class Config:
        from_attributes = True
