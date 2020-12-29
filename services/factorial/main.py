import asyncio
import logging

import grpc

import factorial_pb2
import factorial_pb2_grpc


class FactorialService(factorial_pb2_grpc.FactorialServiceServicer):
    def factorial(n):
        return 1 if n <= 1 else n * factorial(n - 1)
    
    async def Factorial(self, request: factorial_pb2.FactorialReq, context: grpc.aio.ServicerContext) -> factorial_pb2.FactorialRes:
        return factorial_pb2.FactorialRes(result=factorial(request.number))

async def serve() -> None:
    server = grpc.aio.server()
    factorial_pb2_grpc.add_FactorialServiceServicer_to_server(FactorialService(), server)
    listen_addr = '0.0.0.0:50051'
    server.add_insecure_port(listen_addr)
    logging.info("Starting server on %s", listen_addr)
    await server.start()
    try:
        await server.wait_for_termination()
    except KeyboardInterrupt:
        await server.stop(0)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(serve())