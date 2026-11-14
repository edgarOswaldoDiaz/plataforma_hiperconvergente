# MinIO Community (build from source)

**Licensing/status exception:** MinIO source is AGPL-3.0, but the Community distribution moved to source-only; older precompiled binaries are no longer maintained. This kit builds a historical upstream source tag into a local image so it does not silently use an obsolete public binary. It is **not a recommendation for a new production deployment**. Verify the current upstream support/security status and AGPL obligations before use; prefer a currently maintained object-store distribution such as RustFS if its feature/compatibility profile fits.

Start: `docker compose up -d --build`. S3 API: http://127.0.0.1:19000 ; console: http://127.0.0.1:19001.

The container runs as UID 65532, read-only root filesystem, drops Linux capabilities, and persists data in a named volume. The init service fixes volume ownership. Use HTTPS, separate least-privilege access keys, versioning/replication and tested backups for production.
