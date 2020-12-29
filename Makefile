generate-gitignore:
	rm -rf ./services/.gitignore
	sh ./scripts/generate-gitignore.sh

protoc-trigonometry:
	protoc \
		--go_out=./services/trigonometry/ \
		--go-grpc_out=./services/trigonometry/ \
		--go_opt=paths=source_relative \
		--go-grpc_opt=paths=source_relative \
		./proto/trigonometry/trigonometry.proto
