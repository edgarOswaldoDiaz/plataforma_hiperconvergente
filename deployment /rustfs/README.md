# RustFS

Image: `rustfs/rustfs:1.0.5` (upstream RustFS, Apache-2.0; Docker Hub publica amd64 y arm64). La etiqueta y arquitectura se comprobaron el 14-nov-2026.

Inicia: `docker compose up -d`. API S3: http://127.0.0.1:9000 ; consola: http://127.0.0.1:9001.

Se usa un volumen con cuatro directorios locales, no una topología distribuida. `RUSTFS_UNSAFE_BYPASS_DISK_CHECK=false` mantiene habilitadas las comprobaciones del almacenamiento. Cambia la clave de acceso y el secreto por valores únicos. CORS de consola se restringe a localhost; no copies el CORS comodín ni las credenciales de ejemplo del upstream. Para producción, usa Linux, TLS, discos dedicados, topología multi-nodo compatible, logs/rotación y respaldos probados.
