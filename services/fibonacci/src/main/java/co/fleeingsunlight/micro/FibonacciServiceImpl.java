package co.fleeingsunlight.micro;

import co.fleeingsunlight.micro.FibonacciServiceGrpc;
import co.fleeingsunlight.micro.FibonacciReq;
import co.fleeingsunlight.micro.FibonacciRes;
import io.grpc.Status;
import io.grpc.stub.StreamObserver;

public class FibonacciServiceImpl extends FibonacciServiceGrpc.FibonacciServiceImplBase {
    @Override
    public void fibonacci(FibonacciReq request, StreamObserver<FibonacciRes> responseObserver) {
        // super.fibonacci(request, responseObserver);
        if (request.getOrder() <= 0) {
            responseObserver.onError(
                    Status.FAILED_PRECONDITION
                            .withDescription("Order should not be negative.")
                            .asException()
            );
        }

        responseObserver.onNext(
                FibonacciRes
                        .newBuilder()
                        .setNumber(this.fibonacci(request.getOrder()))
                        .build()
        );
        responseObserver.onCompleted();
    }

    @Override
    public void fibonacciFaster(FibonacciReq request, StreamObserver<FibonacciRes> responseObserver) {
        // super.fibonacciFaster(request, responseObserver);
        if (request.getOrder() <= 0) {
            responseObserver.onError(
                    Status.FAILED_PRECONDITION
                            .withDescription("Order should not be negative.")
                            .asException()
            );
        }

        responseObserver.onNext(
                FibonacciRes
                        .newBuilder()
                        .setNumber(this.fibonacciFaster(request.getOrder()))
                        .build()
        );
        responseObserver.onCompleted();
    }

    private int fibonacci(int order) {
        return order <= 1 ? 1 : fibonacci(order - 1) + fibonacci(order - 2);
    }

    private int fibonacciFaster(int order) {
        int a = 1;
        int b = 0;
        int temp = 0;
        while (order >= 0) {
            temp = a;
            a = a + b;
            b = temp;
            order--;
        }
        return b;
    }
}
