package co.fleeingsunlight.micro;

import io.grpc.Server;
import io.grpc.ServerBuilder;

import java.io.IOException;

public class App 
{
    public static void main( String[] args ) throws IOException, InterruptedException {
        Server server = ServerBuilder.forPort(50051).addService(new FibonacciServiceImpl()).build();
        server.start();
        server.awaitTermination();
    }
}
