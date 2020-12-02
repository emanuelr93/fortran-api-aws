all: build run

build:
	docker build -t aws-demo/fortran-serverless .

run:
	docker rm -vf fortran-lambda || true
	docker run -p 9000:8080 -d --name fortran-lambda aws-demo/fortran-serverless

exec:
	docker exec -it fortran-lambda sh

logs:
	docker logs -f fortran-lambda
