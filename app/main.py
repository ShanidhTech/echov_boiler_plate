from fastapi import FastAPI
from app.core.config import settings
from fastapi.routing import APIRoute
from app.api.main import api_router
from app.core.container import AppContainer


def custom_generate_unique_id(route: APIRoute) -> str:
    return f"{route.tags[0]}-{route.name}"

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
    generate_unique_id_function=custom_generate_unique_id,
)


container = AppContainer()
container.wire(modules=["app.api.routes.hello"])
app.container = container

app.include_router(api_router, prefix=settings.API_V1_STR)