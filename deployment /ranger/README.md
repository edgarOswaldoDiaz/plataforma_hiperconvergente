# Apache Ranger (solo desarrollo/evaluación)

Imágenes oficiales ASF: `apache/ranger:2.9.0`, `apache/ranger-db:2.9.0`, `apache/ranger-solr:2.9.0` y `apache/ranger-zk:2.8.0` (Apache-2.0). UI: http://127.0.0.1:6080.

Inicia: `docker compose up -d`. La composición reproduce los comandos de arranque de la guía oficial de imágenes. No se publican PostgreSQL, Solr ni ZooKeeper.

**No es una topología de producción.** La documentación de Apache indica que el quick-start es de desarrollo y evaluación. Las imágenes Docker no están firmadas; descarga por tag y verifica digest/procedencia. Ranger Admin inicia con credenciales demo conocidas (`admin` / `rangerR0cks!`); cámbialas inmediatamente. Esta configuración no persiste los datos de los servicios auxiliares; es efímera y no debe utilizarse para políticas de autorización reales. Para producción, implementa el despliegue completo soportado, TLS, persistencia, endurecimiento de cada servicio, HA y verificación de integridad.
