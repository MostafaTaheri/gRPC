import grpc

# import the generated classes
import calculator_pb2_grpc
import calculator_pb2


# open a gRPC channel
channel = grpc.insecure_channel('localhost:50051')


# create a stub (client)
stub = calculator_pb2_grpc.CalculatorStub(channel)

# create a valid request message
number = calculator_pb2.Number(value=10)

# make the call
response = stub.SquareRoot(number)

print(response.value)
