from app.grpc.generated import auth_pb2_grpc, auth_pb2
from app.services.auth_service import verify_token  # your business logic

class AuthServiceServicer(auth_pb2_grpc.AuthServiceServicer):
    def ValidateToken(self, request, context):
        result = verify_token(request.token)
        if result:
            return auth_pb2.ValidateTokenResponse(
                is_valid=True,
                user_id=result["user_id"]
            )
        return auth_pb2.ValidateTokenResponse(is_valid=False)
