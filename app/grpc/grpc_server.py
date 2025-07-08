import grpc
from concurrent import futures
from app.grpc.generated import auth_pb2_grpc
from app.grpc.handlers.auth_handler import AuthServiceServicer

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    auth_pb2_grpc.add_AuthServiceServicer_to_server(AuthServiceServicer(), server)
    server.add_insecure_port("[::]:50051")
    print("gRPC server running on port 50051...")
    server.start()
    server.wait_for_termination()
