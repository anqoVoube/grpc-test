import grpc
from concurrent import futures
import time
from project.calculator import square_root
import calculator_pb2
import calculator_pb2_grpc


class CalculatorService(calculator_pb2_grpc.CalculatorServicer):
    # Name of function should match with .proto function
    def Square(self, request, context):
        response = calculator_pb2.Number()
        response.value = square_root(request.value)
        return response


def run():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    calculator_pb2_grpc.add_CalculatorServicer_to_server(
        CalculatorService(), server)
    print("Starting server...")
    server.add_insecure_port('localhost:80')
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    run()