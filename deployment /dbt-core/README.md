# dbt Core

Image: `ghcr.io/dbt-labs/dbt-core:1.12.7` (dbt Core, Apache-2.0). dbt Core is a CLI, **not a continuously running service**, so there is intentionally no exposed port.

1. Place your dbt project in `project/`.
2. Provide `profiles/profiles.yml` (copy the example and configure it securely).
3. Run `docker compose run --rm dbt debug` or `docker compose run --rm dbt build`.

**Adapter requirement:** a Core-only image may not include the warehouse adapter you need. Build a derived image that pins a compatible adapter (for example `dbt-postgres`) rather than installing unpinned packages at runtime. Avoid storing production credentials in the project directory or committing profiles to Git.
