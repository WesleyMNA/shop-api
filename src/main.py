from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from src.routers import api


def create_app() -> FastAPI:
    application = FastAPI()
    application.add_middleware(
        CORSMiddleware,
        allow_origins=['*'],
        allow_credentials=True,
        allow_methods=['*'],
        allow_headers=['*'],
    )
    application.include_router(api.router)
    return application


app = create_app()
