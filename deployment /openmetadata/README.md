# OpenMetadata (server + database + OpenSearch)

Images: `docker.getcollate.io/openmetadata/server:2.0.7` (OpenMetadata, Apache-2.0); `postgres:15-alpine` (PostgreSQL License); `opensearchproject/opensearch:2.19.0` (Apache-2.0). OpenSearch security plugin is disabled **only because all ports are private to the Compose network**.

Start: `docker compose up -d`. UI/API: http://127.0.0.1:8585.

This is a minimal single-node setup. It deliberately does not include an ingestion orchestrator (Airflow/ingestion workflows); add the matching OpenMetadata ingestion image/version after deciding the deployment model. The application UI may have its own initial user setup. Before production enable TLS and OpenSearch security, configure auth/SSO, secure secrets, backups, JVM/resource limits and high-availability dependencies. Do not expose OpenSearch directly.
