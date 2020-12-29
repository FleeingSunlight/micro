import { Injectable, OnModuleInit } from '@nestjs/common';
import { Client, ClientGrpc, Transport } from '@nestjs/microservices';
import { join } from 'path';

@Injectable()
export class AppService implements OnModuleInit {
  @Client({
    transport: Transport.GRPC,
    options: {
      url: 'svc-geometry:50051',
      package: 'geometry',
      protoPath: join(__dirname, '../proto/geometry.proto'),
    },
  })
  private readonly _geometryService: ClientGrpc;
  private geometryService: any;

  @Client({
    transport: Transport.GRPC,
    options: {
      url: 'svc-fibonacci:50051',
      package: 'fibonacci',
      protoPath: join(__dirname, '../proto/fibonacci/fibonacci.proto'),
    },
  })
  private readonly _fibonacciService: ClientGrpc;
  private fibonacciService: any;

  @Client({
    transport: Transport.GRPC,
    options: {
      url: 'svc-factorial:50051',
      package: 'factorial',
      protoPath: join(__dirname, '../proto/factorial.proto'),
    },
  })
  private readonly _factorialService: ClientGrpc;
  private factorialService: any;

  onModuleInit() {
    this.geometryService = this._geometryService.getService<any>(
      'GeometryService',
    );
    this.fibonacciService = this._fibonacciService.getService<any>(
      'FibonacciService',
    );
    this.factorialService = this._factorialService.getService<any>(
      'FactorialService',
    );
  }

  async getAreaOfCircle(radius: number): Promise<any> {
    return await this.geometryService.areaOfCircle({ radius });
  }

  async getAreaOfRectangle(width: number, height: number): Promise<any> {
    return await this.geometryService.areaOfRectangle({ width, height });
  }

  async fibonacci(order: number): Promise<any> {
    return await this.fibonacciService.fibonacci({ order });
  }

  async fibonacciFaster(order: number): Promise<any> {
    return await this.fibonacciService.fibonacciFaster({ order });
  }

  async factorial(number: number): Promise<any> {
    return await this.factorialService.factorial({ number });
  }
}
