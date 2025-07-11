from fastapi import APIRouter, Depends
from dependency_injector.wiring import Provide, inject
from app.core.container import AppContainer
from app.crud.crud import AuthService


router = APIRouter(tags=["hello"])


@router.get("/get/user")
@inject
def get_current_user(
    auth_service: AuthService = Depends(Provide[AppContainer.auth_service])
):
    return auth_service.get_user("demo")