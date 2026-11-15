## Overview
The Audit Log Service is a high-availability, tamper-proof system designed to capture, store, and provide searchable access to clinical event logs. It ensures HIPAA/GDPR compliance through immutable storage, cryptographic integrity, and granular access control.

## Key Elements
*   **Ingestion Controller (Go):** Asynchronous event processing and circuit breaking.
*   **Log Processor (Go):** Schema validation and cryptographic hashing.
*   **Search Indexer (OpenSearch):** Rapid retrieval and query performance.
*   **Storage Controller:** Interface for S3 Glacier with WORM Object Lock.
*   **Event Orchestrator:** Manages DSAR workflows, log redaction, and health scoring.
*   **Query API (Go/gRPC):** Read-only interface for auditors with Identity Proxy.
*   **Sidecar (EMR):** Local event buffering and mTLS-secured transmission.

## Relationships
*   **EMR Sidecar → Ingestion Controller:** Asynchronous event shipment via mTLS.
*   **Query API → Compliance Dashboard:** HTTPS/gRPC for secure, ABAC-restricted auditing.
*   **Storage Controller → S3 Glacier:** WORM-compliant archival with quarterly checksum verification.
*   **Identity Proxy → IAM Provider:** Validates claims for non-repudiable auditor access.

## Technology Stack
*   **Go:** Chosen for high-throughput, concurrent event processing.
*   **S3 Glacier (Object Lock):** Ensures 10-year immutable data retention.
*   **OpenSearch:** Facilitates high-performance search and compliance monitoring.
*   **KMS/HSM:** Provides cryptographic signing and non-repudiation of logs.
*   **gRPC:** Enables efficient, secure communication for the Query API.

## Rationale
The architecture decouples high-throughput ingestion from complex retrieval to maintain 99.99% availability during heavy audit queries. Multi-layered security, including mTLS, ABAC, and hardware-backed signing, ensures the system meets stringent HIPAA/GDPR regulatory requirements.