## Overview
The Clinic Management System manages patient admissions, EMRs, scheduling, and billing for healthcare facilities while ensuring strict HIPAA and GDPR compliance. The storage subsystem provides secure, highly available, and immutable long-term data retention for audit logs and medical records.

## Key Elements
- Core Services (Spring Boot / Java)
- Ingestion & Validation Engine (Node.js)
- Encryption Manager (Java/BouncyCastle)
- Retention & Compliance Controller (Go)
- Metadata Indexer (Elasticsearch / OpenSearch)
- Object Store Backend (MinIO / AWS S3 Object Lock)
- Buffer Queue (Embedded SQLite/WAL)

## Relationships
- Core Services -> Ingestion & Validation Engine: Sends audit logs and EMR archives via `gRPC` over mTLS.
- Ingestion & Validation Engine -> Encryption Manager: Passes raw payloads for encryption via `Internal In-Memory API`.
- Ingestion & Validation Engine -> Metadata Indexer: Publishes search metadata via `Kafka/Async`.
- Encryption Manager -> Object Store Backend: Writes encrypted objects using `S3 API`.

## Technology Stack
- Node.js: powers the Ingestion & Validation Engine for high-throughput request handling.
- Go: implements the Retention & Compliance Controller for robust WORM immutability enforcement.
- MinIO / AWS S3 Object Lock: provides hybrid cloud object storage with strict immutability policies.
- Elasticsearch / OpenSearch: handles indexed metadata search with strict RBAC and AES-256 encryption.
- Java / BouncyCastle: enforces envelope encryption and KMS integration.

## Rationale
This architecture combines WORM-enabled object storage with local write-ahead logging to guarantee zero audit log loss during network partitions. It balances strict $\ge$ 10-year regulatory retention mandates with high-performance metadata indexing to meet clinical SLAs.