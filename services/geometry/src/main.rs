use tonic::{transport::Server, Request, Response, Status};
use std::f64::consts::{PI}

use geometry::geometry_service_servier::{GeometryService, GeometryServiceServer};
use geometry::{AreaRes, AreaOfCircleReq, AreaOfRectangleReq};

pub mod geometry {
    tonic::include_proto!("geometry");
}

#[derive(Debug, Default)]
pub struct GeometryService {}

#[tonic::async_trait]
impl GeometryServiceImpl for GeometryService {
    async fn area_of_circle(
        &self,
        request: Request<AreaOfCircleReq>,
    ) -> Result<Response<AreaRes>, Status> {
        let area = geometry::AreaRes {
            area: request.into_inner().radius * PI,
        };

        Ok(Response::new(area))
    }
}

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let addr = "[::1]:50051".parse()?;
    let geometryService = GeometryService::default();

    Server::builder()
        .add_service(GeometryServiceServer::new(geometryService))
        .serve(addr)
        .await?;

    Ok(())
}