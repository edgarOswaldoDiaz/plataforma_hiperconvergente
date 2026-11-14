# JupyterLab

Image: `quay.io/jupyter/minimal-notebook:python-3.13.14` (Jupyter Docker Stacks, Modified BSD). UI: http://127.0.0.1:8888.

Start: `docker compose up -d`. The workspace is mounted from `workspace/`.

A non-empty token is required. The port is bound to loopback; do not disable token auth. Notebooks execute arbitrary code with the container user's filesystem/network permissions, so use only trusted notebooks, avoid mounting host root or Docker socket, and run in an isolated VM for untrusted users. Pin additional Python packages and scan the resulting environment.
