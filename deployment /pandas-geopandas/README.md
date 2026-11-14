# Pandas + GeoPandas

This is a **one-shot Python tooling container**, not a server. It builds from `python:3.13-slim-bookworm`, installs `pandas==3.1.1` (BSD-3-Clause) and `geopandas==1.2.0` (BSD-3-Clause), and runs as a non-root UID. Native geo libraries (GDAL/GEOS/PROJ) are OS packages with their own licenses.

Start the sample version check: `docker compose --profile tools run --rm python-gis`. Run a script: `docker compose --profile tools run --rm python-gis python your_script.py` (place it in `workspace/`).

For production, build and scan an immutable image, pin base image by digest, record all Python/system dependencies in an SBOM, and review licenses of datasets, drivers and additional libraries.
