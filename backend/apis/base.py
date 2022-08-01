from fastapi import APIRouter

from apis.version1 import route_game
from apis.version1 import route_move
from apis.version1 import route_start

api_router = APIRouter()
api_router.include_router(route_game.router, prefix="/game", tags=["board"])
api_router.include_router(route_move.router, prefix="/move", tags=["move"])
api_router.include_router(route_start.router, prefix="/start", tags=["start"])
