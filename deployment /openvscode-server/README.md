# OpenVSCode Server (open-source alternative to Microsoft VS Code)

Image: `ghcr.io/gitpod-io/openvscode-server:1.109.5` (OpenVSCode Server, MIT). Microsoft-branded VS Code is not the same as the fully open-source Code - OSS source tree; this folder uses the community OpenVSCode Server distribution to satisfy the open-source requirement.

Start: `docker compose up -d`. Browser IDE: http://127.0.0.1:3002. A connection token is required.

Treat terminal/editor access as remote code execution. Bind only to loopback, mount only project directories, avoid Docker socket and host secrets, install extensions from trusted sources, and use TLS/SSO proxy before team access.
