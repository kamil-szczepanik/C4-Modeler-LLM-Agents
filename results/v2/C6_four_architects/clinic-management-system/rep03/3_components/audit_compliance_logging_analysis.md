## Overview
The Clinic Management System is a hybrid healthcare platform that manages patient admissions, electronic medical records, scheduling, and billing for medium-sized hospitals and clinics. It ensures strict HIPAA/GDPR compliance, 99.99% availability, and long-term secure data retention.

## Key Elements
- **Log Collector Component (FluentBit)**: Gathers and sanitizes OTLP streams from all upstream containers, dropping plaintext PHI/PII.
- **Log Forwarder / Buffer Component (FluentBit local buffer)**: Persistent local disk buffer preventing log loss during network partitions.
- **Log Indexer & Search Engine (OpenSearch)**: Indexes structured audit events with WORM policies.
- **Compliance Reporter Component (Go service)**: Generates automated HIPAA/GDPR audit reports.
- **Audit Integrity Verifier (Go daemon)**: Computes SHA-256 cryptographic hashes for tamper-evidence.

## Relationships
- Upstream Containers -> Log Collector: Buffered log push [OTLP/gRPC over TLS 1.3]
- Log Collector -> Log Indexer: Bulk indexing [HTTPS/REST via mTLS]
- Compliance Reporter -> Log Indexer: Audit queries [HTTPS/REST via mTLS]
- Audit Integrity Verifier -> Log Indexer: Read audit blocks [HTTPS/REST via mTLS]
- Log Indexer & Audit Integrity Verifier -> Cloud Backup Archive: Cold storage tiering and cryptographic proofs [S3 API / HTTPS]

## Technology Stack
- **FluentBit**: Used for DaemonSet log collection and local buffering to ensure zero log loss.
- **OpenSearch**: Provides searchable audit indexes with Index State Management (ISM) for WORM retention.
- **Go**: Used for Compliance Reporter and Audit Integrity Verifier microservices.
- **OTLP/gRPC over TLS 1.3 / mTLS**: Standardizes secure, encrypted telemetry transport.
- **AWS S3 API / MinIO**: Targets hybrid cloud storage for $\ge$ 10-year retention.

## Rationale
This architecture guarantees regulatory compliance and data integrity via automated PII/PHI sanitization, WORM storage policies, and tamper-evident cryptographic verification. The hybrid Kubernetes deployment utilizing local disk buffers and active-active topologies successfully meets the strict 99.99% uptime and long-term retention requirements.