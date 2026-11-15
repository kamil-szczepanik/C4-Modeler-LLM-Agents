## Overview
The Clinic Management System is a hybrid cloud platform designed to manage patient admissions, EMRs, scheduling, and billing while ensuring strict compliance, high availability, and long-term data retention. The system utilizes a specialized Data Archival Worker to securely offload and preserve historical clinical data.

## Key Elements
- **Data Archival Worker:** Kubernetes-based batch processor utilizing chunk-based processing, idempotency keys, and resource throttling.
- **Cold Storage:** AWS Glacier (or on-prem equivalent) via AES-256 encryption for 10-year data retention.
- **Dead Letter Queue (DLQ):** Error handling queue for failed archival batches.
- **Audit Logging Container:** Destination for cryptographic checksums, compliance traces, and structured audit events.
- **Observability Container:** Prometheus metrics exporter tracking batch processing duration, throughput, and DLQ depth.
- **Secret Management Sidecar:** Kubernetes sidecar supplying configuration and encryption credentials.

## Relationships
- **Data Archival Worker** reads primary operational database via SQL with batched queries and throttling.
- **Data Archival Worker** streams encrypted, compressed payloads to **Cold Storage** using HTTPS/TLS and AES-256.
- **Data Archival Worker** emits structured events and correlation IDs to **Audit Logging Container** via AMQP/Kafka.
- **Data Archival Worker** exposes metrics to **Observability Container** via Prometheus scraping.
- **Data Archival Worker** fetches keys and configs from **Secret Management Sidecar** via local IPC/Volume mounts.

## Technology Stack
- **Runtime:** Kubernetes CronJob / Persistent Worker Pool for scalable background processing.
- **Encryption:** AES-256 for data at rest and in transit; SHA-256 for cryptographic checksum integrity verification.
- **Resilience Patterns:** Exponential backoff with jitter, circuit breakers, and Dead Letter Queues (DLQ).
- **Observability:** Prometheus exporters and OpenTelemetry correlation ID propagation.

## Rationale
This architecture guarantees strict HIPAA and GDPR compliance through cryptographic verification and PII sanitization while protecting operational EMR performance (<1s P95) via application-level throttling and chunk-based batching. Furthermore, active idempotency tracking, schema versioning, and DLQ mechanisms ensure robust 10-year data retention and fault tolerance across hybrid Kubernetes and cloud environments.