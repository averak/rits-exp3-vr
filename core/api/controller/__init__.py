from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from core.api.controller import book_controller


def create_app() -> FastAPI:
    app = FastAPI()

    # middleware
    app.add_middleware(
        CORSMiddleware,
        allow_origins=['*'],
        allow_credentials=True,
        allow_methods=['*'],
        allow_headers=['*'],
    )

    # routing
    app.include_router(book_controller.router, prefix='/books', tags=['book'])

    # index
    @app.get('/')
    def index():
        return 'Hello, World!'

    # OpenAPI
    app.title = '実世界情報実験3 内部API'
    app.description = 'This is a document.'
    app.version = '1.0.0'

    app.openapi_tags = [
        {"name": "book", "description": "本"}
    ]

    return app
