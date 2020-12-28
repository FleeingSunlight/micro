import { Controller, Get, Param, ParseIntPipe } from '@nestjs/common';
import { AppService } from './app.service';

@Controller()
export class AppController {
  constructor(private readonly appService: AppService) {}

  @Get('geometry/circle/:radius')
  async getAreaOfCircle(
    @Param('radius', ParseIntPipe) radius: number,
  ): Promise<any> {
    return this.appService.getAreaOfCircle(radius);
  }

  @Get('geometry/rectangle/:width/:height')
  async getAreaOfRectangle(
    @Param('width', ParseIntPipe) width: number,
    @Param('height', ParseIntPipe) height: number,
  ): Promise<any> {
    return this.appService.getAreaOfRectangle(width, height);
  }
}
