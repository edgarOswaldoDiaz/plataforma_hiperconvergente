# Trino

Image: `trinodb/trino:484` (Trino, Apache-2.0). Includes the built-in `tpch` and `tpcds` sample catalogs. UI/API: http://127.0.0.1:18081.

Start: `docker compose up -d`. Example query: `docker compose exec trino trino --execute 'SELECT * FROM tpch.tiny.customer LIMIT 5'`.

This is a local single-coordinator sample without authentication. Do not publish it to a LAN or the Internet. Before remote access, enable TLS and Trino authentication, restrict catalogs/connectors, set resource groups and use an external coordinator/worker topology appropriate to your security model.
