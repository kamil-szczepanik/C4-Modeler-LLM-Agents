## Overview
[The Go Audit Logging Container provides high-throughput, secure, and immutable audit logging for the Clinic Management System to meet strict HIPAA, GDPR, and 10-year data retention mandates. It ingests events via gRPC, processes them through validation and batch writing engines, and archives data securely to WORM storage.]

## Key Elements
- API Ingestion Handler (`net/http` and `gRPC`)
- Event Validation & Sanitizer (PHI/PII scrubbing)
- Batch Writer Engine (Go routines and channels with `pgx`)
- Archival & Policy Manager (Lifecycle and retention management)
- Local Disk-Backed Queue / WAL (Backpressure buffer)
- External Dependencies: Istio Service Mesh, PostgreSQL, WORM Object Storage (MinIO/S3), HashiCorp Vault, Apache Superset

## Relationships
- Istio Service Mesh -> API Ingestion Handler: `gRPC` over mTLS (Strict)
- Event Validation & Sanitizer -> Batch Writer Engine: Internal Go Channels
- Batch Writer Engine -> PostgreSQL: `TCP/SSL` with `pgx` connection pooling
- Archival & Policy Manager -> WORM Object Storage (MinIO/S3): `HTTPS` with Object Lock API
- Batch Writer Engine -> Apache Superset: Read-only PostgreSQL replica queries

## Technology Stack
- Go (`net/http`, `gRPC`): Chosen for high-throughput concurrency and low memory footprint
- PostgreSQL (`pgx`): Primary storage with connection pooling for rapid writes and audit querying
- WORM Object Storage (MinIO/S3): Object Lock storage ensuring tamper-proof 10-year retention compliance
- HashiCorp Vault: Dynamic secret injection for secure credential management
- OpenTelemetry & Prometheus: Structured telemetry and metrics for observability

## Rationale
[This architecture satisfies 99.99% availability and high-throughput EMR mutation requirements through active-active hybrid deployment patterns and resilient batch-writing. Strict mTLS, PHI scrubbing, and cryptographic hashing ensure comprehensive regulatory compliance for healthcare data.]