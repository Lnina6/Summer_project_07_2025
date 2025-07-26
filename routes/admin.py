from fastapi import APIRouter

router = APIRouter(
    prefix="/admin",
    tags=["admin"],
)

@router.get("/list/student/{std}")
async def list_all_student(std: str):
    """
    List all students of a standard
    """
    
    return {"message": "ok"}

@router.post("/create/student")
async def create_student_profile():
    """
    Create student profile
    """
    
    return {"message": "ok"}

@router.get("/get/student/{id}")
async def get_student_by_id(id: str):
    """
    Get student info of a standard by their unique id
    """
    
    return {"message": "ok"}

@router.put("/update/student/{id}")
async def update_student_by_id(id: str):
    """
    Update student's information using their id
    """
    
    return {"message": "ok"}

@router.delete("/delete/student/{id}")
async def delete_student_by_id(id: str):
    """
    Deletes student information
    """
    
    return {"message": "ok"}

@router.post("/create/report/{id}")
async def create_student_report(id: str):
    """
    Create student's report card
    """
    
    return {"message": "ok"}

@router.put("/update/report/{id}")
async def update_student_report(id: str):
    """
    Update student's report card
    """
    
    return {"message": "ok"}
