
VERSION=0.0.1

build:
	docker build -t diogok/fluentbit-http-to-loki:$(VERSION) .
	docker build -t diogok/fluentbit-http-to-loki:latest .

push:
	docker push diogok/fluentbit-http-to-loki:$(VERSION)
	docker push diogok/fluentbit-http-to-loki:latest
