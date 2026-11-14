# Grafana OSS

Image: `grafana/grafana:13.3.0` (Grafana OSS, AGPL-3.0). PostgreSQL stores metadata; Grafana data/plugin volume persists separately. UI: http://127.0.0.1:3001.

Start: `docker compose up -d`. Anonymous access and self-signup are disabled.

For production, configure HTTPS and `GF_SECURITY_COOKIE_SECURE=true`, SSO/LDAP, least-privilege service accounts, provisioning via reviewed config, alerting secrets, plugin allowlists, DB backups and resource limits. Review plugin licenses separately; Grafana OSS does not make every plugin/datasource open source.
