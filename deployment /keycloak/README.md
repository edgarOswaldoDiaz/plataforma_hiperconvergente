# Keycloak

Image base: `quay.io/keycloak/keycloak:26.8.2` (Keycloak, Apache-2.0), locally optimized with a build stage for PostgreSQL support. PostgreSQL is a separate dependency. UI: http://127.0.0.1:18082.

Start: `docker compose up -d --build`. This uses the production `start --optimized` command, **not** `start-dev`.

This example enables HTTP only because the listener is loopback-only. For real deployments, configure a stable external hostname, HTTPS at the ingress/reverse proxy, trusted proxy headers, hostname strictness, secure cookies, backups, HA database and a supported proxy/TLS topology. Do not expose the admin console over cleartext HTTP.
