# Harness Open Source

This project is the independent `harness/harness` open-source project (Apache-2.0), **not** the full commercial Harness SaaS/platform. Image `harness/harness:3.3.0` exists in Docker Hub, but the published stable tag is approximately one year old as checked 2026-11-14. A newer `unstable` tag is pushed more recently, but is not suitable as a reproducible production baseline. Verify the image's digest, source commit, vulnerability status and current upstream install guide before use.

Start: `docker compose up -d`. The app ports are bound to localhost on 3000 and 3022; confirm actual ports and first-run admin setup against the exact image version.

**Safety:** no host Docker socket is mounted. CI jobs that need to build images must use a separate ephemeral runner/remote builder with narrowly scoped access. Do not mount `/var/run/docker.sock` into this service. The documented initial login is `admin` / `changeit`; change it immediately. Do not expose the interface publicly without TLS/SSO.
