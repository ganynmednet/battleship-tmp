# https://www.fastapitutorial.com/blog/fastapi-hello-world/

from fastapi import FastAPI
from core.config import settings
from apis.base import api_router

from db.session import engine
from db.base import Base


def include_router(app):
    app.include_router(api_router)


# def configure_static(app):
#     app.mount("/static", StaticFiles(directory="static"), name="static")
def create_tables():  # new
    print("create_tables")
    Base.metadata.create_all(bind=engine)


def start_application():
    app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)
    include_router(app)
    create_tables()
    # configure_static(app)
    return app


app = start_application()
