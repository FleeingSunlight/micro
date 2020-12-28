use tonic::{transport::Server, Request, Response, Status};
use std::f64::consts::{PI};

use geometry::geometry_service_server::{GeometryService, GeometryServiceServer};
use geometry::{AreaRes, AreaOfCircleReq, AreaOfRectangleReq};

pub mod geometry {
    tonic::include_proto!("geometry");
}

#[derive(Debug, Default)]
pub struct GeometrySVC {}

#[tonic::async_trait]
impl GeometryService for GeometrySVC {
    async fn area_of_circle(
        &self,
        request: Request<AreaOfCircleReq>,
    ) -> Result<Response<AreaRes>, Status> {
        let area = geometry::AreaRes {
            area: request.into_inner().radius * (PI as f32),
        };

        Ok(Response::new(area))
    }

    async fn area_of_rectangle(
        &self,
        _request: Request<AreaOfRectangleReq>,
    ) -> Result<Response<AreaRes>, Status> {
        unimplemented!()
    }
}

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let addr = "0.0.0.0:50051".parse()?;
    let geometry_service = GeometrySVC::default();

    println!("[services/geometry]: {}", addr);

    Server::builder()
        .add_service(GeometryServiceServer::new(geometry_service))
        .serve(addr)
        .await?;

    Ok(())
}