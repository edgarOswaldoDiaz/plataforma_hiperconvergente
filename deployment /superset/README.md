# Apache Superset

Image: `apache/superset:6.1.0` (Apache-2.0). Metadata DB: PostgreSQL. UI: http://127.0.0.1:8088.

Start: `docker compose up -d`. The `init` job migrates metadata DB and creates the bootstrap admin. If the user already exists, the create-admin command is tolerated and `superset init` still runs.

Superset's own documentation does not recommend the quickstart Compose topology for production. This file is a local/development baseline. Before production use external managed PostgreSQL, Redis/Celery workers, TLS, SSO, secure cookie settings, hardened CSP/CSRF, secret rotation, backups, resource limits and a supported deployment architecture. Keep the SECRET_KEY private and stable across replicas.
