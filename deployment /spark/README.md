# Apache Spark Standalone

Image: `apache/spark:4.3.0-java25-r` (Apache Spark, Apache-2.0). Includes one master and one worker. Master UI: http://127.0.0.1:18080. Spark RPC is not published to the host.

Start: `docker compose up -d`. Submit jobs from a Spark client on the Docker network using `spark://master:7077` or add a dedicated submit container.

This is a single-host development baseline, not a secured multi-tenant Spark cluster. Keep RPC/UI private; configure authentication, network encryption, TLS, authorization, resource quotas and external log/event storage before any shared deployment. Audit third-party libraries shipped in downstream Spark images as part of your software supply chain.
