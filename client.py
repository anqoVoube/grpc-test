import grpc

import calculator_pb2
import calculator_pb2_grpc

channel = grpc.insecure_channel('localhost:80')

# Create Stub
stub = calculator_pb2_grpc.CalculatorStub(channel)

# Call the API
number = calculator_pb2.Number(value=16)
response = stub.Square(number)
print(response.value)