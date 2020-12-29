use std::f64::consts::PI;
use tonic::{transport::Server, Request, Response, Status};

use geometry::{AreaOfCircleReq, AreaOfRectangleReq, AreaRes};

pub mod geometry {
    tonic::include_proto!("geometry");
}

#[derive(Debug, Default)]
pub struct GeometryServiceServer;

#[tonic::async_trait]
impl geometry::geometry_service_server::GeometryService for GeometryServiceServer {
    async fn area_of_circle(
        &self,
        request: Request<AreaOfCircleReq>,
    ) -> Result<Response<AreaRes>, Status> {
        let radius = request.into_inner().radius;

        if radius < 0.0 {
            return Status::failed_precondition("Radius should not be negative.");
        }

        let area = geometry::AreaRes {
            area: radius * (PI as f32),
        };

        Ok(Response::new(area))
    }

    async fn area_of_rectangle(
        &self,
        request: Request<AreaOfRectangleReq>,
    ) -> Result<Response<AreaRes>, Status> {
        let req = request.into_inner();
        let width = req.width;
        let height = req.height;
        
        if width < 0.0 {
            return Status::failed_precondition("Width should not be negative.");
        }

        if height < 0.0 {
            return Status::failed_precondition("Height should not be negative.");
        }

        let area = geometry::AreaRes {
            area: width * height,
        };

        Ok(Response::new(area))
    }
}

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let addr = "0.0.0.0:50051".parse()?;
    let server = GeometryServiceServer::default();
    Server::builder()
        .add_service(geometry::geometry_service_server::GeometryServiceServer::new(server))
        .serve(addr)
        .await?;
    Ok(())
}
