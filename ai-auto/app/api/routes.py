from fastapi import APIRouter, BackgroundTasks
from pydantic import BaseModel
from app.agents.brain import run_agent
from app.models.models import Task, TaskStatus, TaskType
from app.core.database import SessionLocal

router = APIRouter()

class TaskRequest(BaseModel):
    prompt: str

async def execute_task(task_id: int, prompt: str):
    try:
        print(f"\n--- Iniciando tarea {task_id} ---")
        result = await run_agent(prompt)
        print(f"--- Tarea {task_id} finalizada ---\nResultado: {result}")
        
        db = SessionLocal()
        try:
            task = db.query(Task).filter(Task.id == task_id).first()
            if task:
                task.status = TaskStatus.SUCCESS
                db.commit()
        finally:
            db.close()
    except Exception as e:
        print(f"Error en tarea {task_id}: {e}")

@router.post("/tasks/")
async def create_task(request: TaskRequest, background_tasks: BackgroundTasks):
    db = SessionLocal()
    try:
        # AQUÍ ESTABA EL ERROR: Usamos TaskType.SCRAPING en lugar del string "scraping"
        new_task = Task(
            prompt=request.prompt, 
            status=TaskStatus.PENDING, 
            type=TaskType.SCRAPING
        )
        db.add(new_task)
        db.commit()
        db.refresh(new_task)
        task_id = new_task.id
    finally:
        db.close()
    
    background_tasks.add_task(execute_task, task_id, request.prompt)
    
    return {"task_id": task_id, "status": "dispatched"}