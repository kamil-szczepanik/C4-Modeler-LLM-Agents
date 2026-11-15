## Overview
The Audit Log Sitter collects and securely routes real-time payment audit events to tamper-evident immutable storage. It ensures strict regulatory compliance and zero data loss for downstream consumers like compliance officers and external auditors.

## Key Elements
- Audit Log Sitter (Rust / AWS ECS on Fargate)
- Kafka Consumer Component (`rdkafka`)
- Payload Normalizer & Signer Component
- WORM Storage Batcher Component
- Resilience & DLQ Router Component
- AWS MSK (Managed Kafka)
- AWS QLDB / S3 Object Lock
- AWS KMS
- Terraform

## Relationships
- AWS MSK -> Audit Log Sitter: Streams audit payloads [TCP/TLS 1.3 with mTLS]
- Kafka Consumer Component -> Resilience & DLQ Router Component: Passes failed/poisoned payloads [In-memory channel]
- Payload Normalizer & Signer Component -> WORM Storage Batcher Component: Passes normalized signed payloads [In-memory channel]
- WORM Storage Batcher Component -> AWS S3 Object Lock / QLDB: Persists audit logs [HTTPS / TLS 1.3 with IAM Condition Keys and `aws:SecureTransport`]

## Technology Stack
- Rust: Chosen for low memory footprint, performance, and safety suitable for a 3-person team
- AWS ECS on Fargate: Minimizes operational overhead and auto-scales based on consumer lag
- AWS S3 Object Lock & QLDB: Provides 7-year WORM storage in Compliance Mode for auditability (R-06)
- AWS MSK with Dead-Letter Queues: Handles event streaming and isolates poisoned payloads
- AWS KMS: Manages cryptographic keys securely for payload signing and PCI-DSS compliance

## Rationale
This architecture uses serverless and managed AWS services to remain within the 25,000 EUR monthly budget while requiring only three engineers to operate. It enforces PCI-DSS Level 1 compliance and a 7-year tamper-evident audit trail through TLS 1.3, mTLS, AWS KMS, and S3 Object Lock Compliance Mode.