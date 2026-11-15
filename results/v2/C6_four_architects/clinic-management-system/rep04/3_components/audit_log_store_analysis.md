## Overview
The Clinic Management System is a clinical IT platform that manages patient admissions, electronic medical records, scheduling, and billing for medium-sized hospitals and clinics. It ensures high availability, strict security, and compliance with healthcare regulations.

## Key Elements
- Log Ingestion API Component (Go/gRPC)
- Tamper-Evident Hashing Engine (SHA-256 Merkle Tree Processor)
- Primary Storage Indexer (Elasticsearch / OpenSearch)
- Long-Term Archival Manager (S3 Glacier Object Lock / WORM Storage)
- Compliance Query Interface (REST/HTTPS)
- Key Management & Encryption Component (HashiCorp Vault Integration)

## Relationships
- Core Clinical Microservice -> Log Ingestion API via gRPC/TLS
- Log Ingestion API -> Tamper-Evident Hashing Engine via Internal Method Call
- Tamper-Evident Hashing Engine -> Primary Storage Indexer via Internal Channel
- Primary Storage Indexer -> Long-Term Archival Manager via HTTPS
- Auditor / Compliance Service -> Compliance Query Interface via HTTPS/mTLS
- Tamper-Evident Hashing Engine -> Key Management & Encryption Component via gRPC/TLS
- Primary Storage Indexer -> Vault / Cloud KMS via HTTPS (AES-256)
- Message Broker (Kafka) -> Log Ingestion API via Kafka Consumer Protocol (TLS)
- Compliance Query Interface -> Observability & Telemetry Collector via OpenTelemetry (gRPC)

## Technology Stack
- Go/gRPC: High-performance, secure audit event ingestion.
- SHA-256 Merkle Tree: Cryptographic chaining for log immutability and tamper detection.
- Elasticsearch / OpenSearch: Fast compliance querying with role-based access control.
- S3 Glacier Object Lock: Cost-effective WORM storage for 10-year retention compliance.
- HashiCorp Vault: HSM-backed envelope encryption and zero-knowledge verification.
- Apache Kafka: Decoupled, asynchronous event streaming to protect clinical performance.

## Rationale
This component architecture uses asynchronous Kafka ingestion and indexed search to maintain sub-second clinical transaction performance. Cryptographic hashing, WORM storage, and envelope encryption strictly satisfy HIPAA, GDPR, and 10-year audit retention mandates.