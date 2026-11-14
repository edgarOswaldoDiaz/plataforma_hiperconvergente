# MLflow

Image: `ghcr.io/mlflow/mlflow:v3.17.1-full` (MLflow, Apache-2.0). PostgreSQL is a separate OSS dependency.

Start with `docker compose up -d`. UI: http://127.0.0.1:5000.

**Security:** this Compose is intended for a single-host lab. MLflow's tracking server must not be exposed directly to an untrusted network. The username/password env values in the example are not an authentication implementation; use an authenticated TLS reverse proxy or supported authentication plugin. Artifact storage is a local named volume; for production use private object storage, TLS, backups, and least-privilege credentials.
