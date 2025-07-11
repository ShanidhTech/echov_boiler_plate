from dependency_injector import containers, providers

from app.core.db import Database

from ..crud.crud import AuthService  # Adjust the import path as necessary

class AppContainer(containers.DeclarativeContainer):
    """Dependency Injection Container for the application."""
    # auth_service = providers.Singleton(AuthService)

    database = providers.Singleton(Database)
    auth_service = providers.Factory(AuthService, db_conn=database)
