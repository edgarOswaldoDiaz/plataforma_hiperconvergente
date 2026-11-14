# Rebuild from upstream source: MinIO Community binaries are no longer maintained.
ARG MINIO_REF=RELEASE.2025-10-15T17-29-55Z
FROM golang:1.25-alpine AS build
ARG MINIO_REF
RUN apk add --no-cache git build-base
RUN git clone --depth 1 --branch "${MINIO_REF}" https://github.com/minio/minio.git /src
WORKDIR /src
ENV CGO_ENABLED=0 GOOS=linux
RUN mkdir -p /out && go build -trimpath -ldflags="-s -w" -o /out/minio .

FROM gcr.io/distroless/static-debian12:nonroot
COPY --from=build /out/minio /usr/bin/minio
WORKDIR /data
USER 65532:65532
ENTRYPOINT ["/usr/bin/minio"]
CMD ["server", "/data", "--console-address", ":9001"]
