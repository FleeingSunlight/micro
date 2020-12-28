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

  onModuleInit() {
    this.geometryService = this._geometryService.getService<any>(
      'GeometryService',
    );
  }

  async getAreaOfCircle(radius: number): Promise<any> {
    return await this.geometryService.areaOfCircle({ radius });
  }

  async getAreaOfRectangle(width: number, height: number): Promise<any> {
    return await this.geometryService.areaOfRectangle({ width, height });
  }
}
