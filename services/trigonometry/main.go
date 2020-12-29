package main

import (
	"context"
	pb "github.com/FleeingSunlight/micro/trigonometry/proto/trigonometry"
	"google.golang.org/grpc"
	"google.golang.org/grpc/codes"
	"google.golang.org/grpc/status"
	"log"
	"math"
	"net"
)

type Server struct {
	pb.UnimplementedTrigonometryServiceServer
}

func (s *Server) Sin(ctx context.Context, in *pb.TrigonometryReq) (*pb.TrigonometryRes, error) {
	if in.GetArgument() < 0.0 {
		return nil, status.Error(codes.FailedPrecondition, "Argument should not be negative.")
	}

	return &pb.TrigonometryRes{
		Result: float32(math.Sin(float64(in.GetArgument()))),
	}, nil
}

func (s *Server) Cos(ctx context.Context, in *pb.TrigonometryReq) (*pb.TrigonometryRes, error) {
	if in.GetArgument() < 0.0 {
		return nil, status.Error(codes.FailedPrecondition, "Argument should not be negative.")
	}

	return &pb.TrigonometryRes{
		Result: float32(math.Cos(float64(in.GetArgument()))),
	}, nil
}

func (s *Server) Tan(ctx context.Context, in *pb.TrigonometryReq) (*pb.TrigonometryRes, error) {
	if in.GetArgument() < 0.0 {
		return nil, status.Error(codes.FailedPrecondition, "Argument should not be negative.")
	}

	return &pb.TrigonometryRes{
		Result: float32(math.Tan(float64(in.GetArgument()))),
	}, nil
}

func main() {
	lis, err := net.Listen("tcp", ":50051")
	if err != nil {
		log.Fatalf("Failed to listen: %v", err)
	}
	s := grpc.NewServer()
	pb.RegisterTrigonometryServiceServer(s, &Server{})
	if err := s.Serve(lis); err != nil {
		log.Fatalf("Failed to serve: %v", err)
	}
}