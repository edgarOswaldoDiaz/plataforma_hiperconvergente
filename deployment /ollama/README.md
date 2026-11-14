# Ollama

Image: `ollama/ollama:0.40.16` (Ollama runtime, MIT). API: http://127.0.0.1:11434.

CPU: `docker compose up -d`; GPU overlay: `docker compose -f docker-compose.yml -f docker-compose.gpu.yml up -d` with a correctly installed NVIDIA runtime. Then download a model, for example `docker compose exec ollama ollama pull qwen2.5:0.5b`.

The API has no authentication in this baseline, so it is bound to loopback only. Never expose port 11434 directly to a network; use an authenticated TLS gateway and network policy. **Each model's license and terms are separate from Ollama's MIT license**; verify them before commercial or redistribution use.
