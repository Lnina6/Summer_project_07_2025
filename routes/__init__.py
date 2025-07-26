from .student import router as student_router
from .admin import router as admin_router

routers = [
    student_router,
    admin_router,
]
