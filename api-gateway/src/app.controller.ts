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

  @Get('fibonacci/:order')
  async fibonacci(@Param('order', ParseIntPipe) order: number): Promise<any> {
    return this.appService.fibonacci(order);
  }

  @Get('fibonacci/faster/:order')
  async fibonacciFaster(
    @Param('order', ParseIntPipe) order: number,
  ): Promise<any> {
    return this.appService.fibonacciFaster(order);
  }

  @Get('factorial/:number')
  async factorial(@Param('number', ParseIntPipe) number: number): Promise<any> {
    return this.appService.factorial(number);
  }

  @Get('trigonometry/sin/:argument')
  async trigonometrySin(
    @Param('argument', ParseIntPipe) argument: number,
  ): Promise<any> {
    return this.appService.trigonometrySin(argument);
  }

  @Get('trigonometry/cos/:argument')
  async trigonometryCos(
    @Param('argument', ParseIntPipe) argument: number,
  ): Promise<any> {
    return this.appService.trigonometryCos(argument);
  }

  @Get('trigonometry/tan/:argument')
  async trigonometryTan(
    @Param('argument', ParseIntPipe) argument: number,
  ): Promise<any> {
    return this.appService.trigonometryTan(argument);
  }
}
