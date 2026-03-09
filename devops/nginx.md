# NGINX

Ключевые материалы по NGINX для reverse proxy, TLS termination и load balancing.

## Official Docs

- nginx Documentation
  - url: <https://nginx.org/en/docs/>
  - type: `official`
  - why: главный reference по установке, конфигурации, request processing и основным runtime-возможностям
  - topics: `nginx, web-server, reverse-proxy, config`
  - verified: `2026-03-09`

- Beginner's Guide
  - url: <https://nginx.org/en/docs/beginners_guide.html>
  - type: `official`
  - why: хороший старт по структуре конфигурации, master/worker process model и базовым сценариям
  - topics: `nginx, beginner, processes, configuration`
  - verified: `2026-03-09`

## Reference / Best Practices

- How nginx Processes a Request
  - url: <https://nginx.org/en/docs/http/request_processing.html>
  - type: `reference`
  - why: критически важный материал для понимания `server`, `location`, matching и неожиданных routing эффектов
  - topics: `nginx, request-processing, routing, locations`
  - verified: `2026-03-09`

- Configuring HTTPS Servers
  - url: <https://nginx.org/en/docs/http/configuring_https_servers.html>
  - type: `reference`
  - why: базовый operational reference по TLS termination, сертификатам и HTTPS-конфигу
  - topics: `nginx, https, tls, certificates`
  - verified: `2026-03-09`
