## Overview
The system is a real-time payment fraud screening platform that evaluates card-not-present payment authorizations and manages analyst reviews. It ensures strict PCI-DSS compliance, 7-year tamper-evident auditability, and sub-50ms P99 decision latency at 3,000 transactions per second.

## Key Elements
- Transactional Store: Amazon Aurora Serverless v2 PostgreSQL
- Feature Store: Amazon ElastiCache Serverless (Redis)
- Audit Ingestion Queue: Amazon SQS with Dead Letter Queue (DLQ)
- Security Controls: AWS KMS with customer-managed keys (CMK), AWS Secrets Manager, IAM Database Authentication
- Compliance Tools: Amazon S3 Object Lock, PostgreSQL pgAudit

## Relationships
- Scoring Engine -> Feature Store: Reads velocity features [RESP, <5ms]
- Scoring Engine -> Async Messaging (SQS): Enqueues decision audit payloads [AWS SDK, HTTP/S]
- Case Management -> Transactional Store: Reads and writes analyst cases and reviews [PostgreSQL Wire Protocol, TLS 1.3]
- Transactional Store -> S3 Object Lock: Streams audit logs for tamper-evident 7-year retention [HTTPS]

## Technology Stack
- Amazon Aurora Serverless v2 PostgreSQL: Chosen for ACID compliance, relational case management, and scalable transactional throughput.
- Amazon ElastiCache Serverless (Redis): Chosen for sub-5ms real-time feature lookups without operational server management.
- Amazon SQS: Chosen to decouple synchronous scoring from database writes, ensuring P99 latency under 50 ms.
- AWS KMS: Chosen to enforce column-level encryption and zero exposure of plaintext card numbers (PAN).
- PostgreSQL pgAudit: Chosen to generate detailed security and compliance logs for PCI-DSS Level 1.

## Rationale
This architecture balances ultra-low latency requirements with strict financial compliance through asynchronous processing and high-performance in-memory caching. It maintains a lean operational footprint suited for a 3-engineer team while satisfying rigorous PCI-DSS Level 1 and 7-year auditability mandates.