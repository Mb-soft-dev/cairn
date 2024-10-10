from fastapi import APIRouter
from api.routes import auth, points

api_router = APIRouter()
api_router.include_router(auth.router, tags=["auth"])
api_router.include_router(points.router, tags=["points"])