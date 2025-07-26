from fastapi import APIRouter

router = APIRouter(
    prefix="/student",
    tags=["student"],
)

@router.get("/profile/{id}")
async def get_my_profile(id: str):
    """
    Returns student profile data
    """
    return {"message": "ok"}

@router.get("/reports/{id}")
async def get_my_reports(id: str):
    """
    Returns student's all terms reports
    """
    
    return {"message": "ok"}

@router.get("/reports/subject/{id}")
async def get_subject_report(id: str, subject: str):
    """
    Get student reports subject wise
    """
    
    return {"message": "ok"}
