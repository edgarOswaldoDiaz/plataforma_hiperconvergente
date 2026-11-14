FROM python:3.13-slim-bookworm
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1 PIP_NO_CACHE_DIR=1
RUN apt-get update && apt-get install -y --no-install-recommends \
    libgdal-dev libgeos-dev libproj-dev proj-data proj-bin \
    && rm -rf /var/lib/apt/lists/* \
    && groupadd --gid 10001 analyst \
    && useradd --uid 10001 --gid analyst --create-home --shell /usr/sbin/nologin analyst
RUN pip install --no-cache-dir pandas==3.1.1 geopandas==1.2.0
USER 10001:10001
WORKDIR /workspace
