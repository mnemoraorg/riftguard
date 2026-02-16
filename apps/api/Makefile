.PHONY: build run test dev tidy clean

build:
	go build -o tmp/core cmd/server/main.go

run: build
	@trap 'make clean' INT TERM; ./tmp/core

test:
	go test ./...

dev:
	@air; make clean

tidy:
	go mod tidy

clean:
	rm -rf tmp
