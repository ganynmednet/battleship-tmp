# https://www.fastapitutorial.com/blog/fastapi-hello-world/

from fastapi import FastAPI
# uvico
from core.config import settings
# from apis.general_pages.route_homepage import general_pages_router
from apis.routes import general_pages_router


# app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)


def include_router(app):
    app.include_router(general_pages_router)


# def configure_static(app):
#     app.mount("/static", StaticFiles(directory="static"), name="static")


def start_application():
    app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)
    include_router(app)
    # configure_static(app)
    return app


app = start_application()
# print(dir(Request))

# @app.get("/")
# def hello_api():
#     return {
#         "msg": "Hello API"
#     }


print("ok")
