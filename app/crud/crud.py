from app.core.db import Database


class AuthService:
    """
    A simple authentication service that simulates user retrieval.
    """
    def __init__(
            self,
            db_conn: Database  # This can be an AsyncSession or any other DB connection type
            ):
        # no real db needed
        # self.fake_users = {"demo": {"id": 1, "username": "demo"}}
        self.db_conn = db_conn

    def get_user(self, username: str):
        # return self.fake_users.get(username)
        return "hello world"
