# vLLM OpenAI-compatible server

Images: `vllm/vllm-openai-cpu:v0.33.0` (CPU default) or `vllm/vllm-openai:v0.32.0` (GPU overlay); vLLM is Apache-2.0. API: http://127.0.0.1:8000/v1.

CPU: `docker compose up -d`. NVIDIA GPU: `docker compose -f docker-compose.yml -f docker-compose.gpu.yml up -d` with a compatible NVIDIA Container Toolkit/driver.

Set a strong API key. Model downloads are persisted in a cache volume. **Model weights/datasets have their own licenses and acceptable-use terms**; review the selected model independently. In production, use TLS/auth proxy, quotas, egress restrictions, model allowlists, GPU memory limits and monitoring. Avoid mounting arbitrary host paths.
