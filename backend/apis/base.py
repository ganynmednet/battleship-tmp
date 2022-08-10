from fastapi import APIRouter
from apis.version1 import route_game
from apis.version1 import route_start
from apis.version1 import route_users
from apis.version1 import route_login
from apis.version1 import route_shoot

api_router = APIRouter()
api_router.include_router(route_game.router, prefix="/game", tags=["game"])
api_router.include_router(route_start.router, prefix="/start", tags=["start"])
api_router.include_router(route_users.router, prefix="/users", tags=["users"])
api_router.include_router(route_login.router, prefix="/login", tags=["login"])
api_router.include_router(route_shoot.router, prefix="/shoot", tags=["shoot"])
