# GitLab CE + GitLab Runner

- Images: `gitlab/gitlab-ce:19.5.5-ce.0` (MIT), `gitlab/gitlab-runner:v19.5.3` (MIT), Docker Engine DinD rootless image (Apache-2.0 components).
- UI: http://127.0.0.1:8929 ; SSH: 127.0.0.1:2224.
- Start GitLab first: `docker compose up -d gitlab docker`. Create a runner in **Admin > CI/CD > Runners** or a project/group runner, then set `RUNNER_AUTH_TOKEN` in `.env` and run `docker compose up -d runner`.

**Security:** DinD is isolated from the host daemon, but the service uses `privileged: true` to support nested container features. Run only trusted CI jobs, use a dedicated host/VM, restrict runner tags/protected branches, and never share this runner with untrusted projects. Do not mount `/var/run/docker.sock`. This is a local HTTP baseline; put it behind TLS/reverse proxy before remote access.
