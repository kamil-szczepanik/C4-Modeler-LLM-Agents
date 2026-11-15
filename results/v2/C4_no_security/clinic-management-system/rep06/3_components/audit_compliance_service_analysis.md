## Overview
[The Audit & Compliance Service manages HIPAA/GDPR regulatory compliance, secure log ingestion, and immutable data retention for the Clinic Management System. It guarantees 10-year auditability and high-performance querying for internal officers and external regulators.]

## Key Elements
- Audit Event Ingestion Engine (Python / FastAPI / Pydantic)
- Immutable Storage Writer (SQLAlchemy / S3 SDK)
- Search & Indexing Engine (Elasticsearch / OpenSearch)
- Compliance Query & Reporting API (Python / FastAPI)
- Report & Cryptographic Export Generator (Python / ReportLab / Celery / Redis)
- Storage Tier (WORM Object Storage with S3 Object Lock and Glacier Deep Archive)
- Key Management (HashiCorp Vault / AWS KMS)

## Relationships
- EMR & Scheduling Service -> Audit Event Ingestion Engine [gRPC / Apache Kafka]
- Audit Event Ingestion Engine -> Search & Indexing Engine [REST API / Bulk]
- Audit Event Ingestion Engine -> Immutable Storage Writer [S3 API]
- Compliance Query & Reporting API -> Search & Indexing Engine [REST API]
- Report & Cryptographic Export Generator -> WORM Object Storage [S3 API]
- Report & Cryptographic Export Generator -> Key Management [HTTPS / KMS API]

## Technology Stack
- Python / FastAPI: High-performance asynchronous API development
- Elasticsearch / OpenSearch: Sub-second search and indexing for audit logs
- Apache Kafka: Reliable high-throughput event ingestion
- WORM Object Storage & S3 Object Lock: Cryptographically secure 10-year data retention
- Celery / Redis: Asynchronous background processing for heavy report generation
- HashiCorp Vault / AWS KMS: Secure cryptographic key management for digital signatures

## Rationale
[This architecture enforces strict HIPAA and GDPR compliance by isolating immutable audit logs in WORM storage while providing sub-second search capabilities via Elasticsearch. Asynchronous task queues and dedicated cryptographic key management ensure the system remains scalable, secure, and resilient under regulatory investigations.]