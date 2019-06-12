# Fluentbit HTTP to Loki HTTP

This is a simple API to receive logs from Fluentbit HTTP integration and send to Grafana Loki HTTP API.


The fluentbit output config:

```
[OUTPUT]
  Match *
  Name http
  Host ${HTTP_HOST}
  Port ${HTTP_PORT}
  URI /push
  Format json
```

Them run this container:

```
docker run -e LOKI_HOST=loki LOKI_PORT=3001 diogok/fluentbit-http-to-loki:0.0.1
```

## License

MIT
