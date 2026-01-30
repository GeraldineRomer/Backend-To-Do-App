from sqlalchemy.orm import Session
from app.models.task_model import Task
from app.schemas.task_schema import TaskCreate

def create_task(db: Session, task: TaskCreate):
    new_task = Task(**task.model_dump())
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task

def get_tasks(db: Session):
    return db.query(Task).all()

def get_task_by_id(db: Session, task_id: int):
    return db.query(Task).filter(Task.id_tarea == task_id).first()

def update_task(db: Session, task_id: int, task_data: TaskCreate):
    task = db.query(Task).filter(Task.id_tarea == task_id).first()

    if not task:
        return None

    for key, value in task_data.dict().items():
        setattr(task, key, value)

    db.commit()
    db.refresh(task)
    return task


def delete_task(db: Session, task_id: int):
    task = db.query(Task).filter(Task.id_tarea == task_id).first()

    if not task:
        return None

    db.delete(task)
    db.commit()
    return task
