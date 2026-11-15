## Overview
The Amazon S3 Model Registry container provides immutable storage, secure access control, and atomic versioning for fraud scoring models and rules. It enables zero-downtime hot-reloading for the Real-Time Payment Fraud Screening system while maintaining PCI-DSS compliance and 7-year auditability.

## Key Elements
- S3 Bucket & Versioning/Object Lock (Amazon S3)
- S3 Event Notification to SQS Queue (Amazon SQS)
- Access Control & Encryption (AWS IAM & KMS SSE-S3)
- Model Metadata Manifest (`manifest.json`)
- Staging and Production Prefixes (/staged and /production)

## Relationships
- Fraud Scoring Service -> Amazon S3 Model Registry: Polls SQS queue and fetches version-pinned binaries securely via AWS SDK (HTTPS) using IAM roles
- S3 Event Notifications -> SQS Queue: Triggers asynchronous deployment alerts upon new model uploads (HTTPS / S3 API)
- Fraud Scoring Service -> Model Metadata Manifest: Periodically polls `manifest.json` for atomic version synchronization (HTTPS / S3 API)

## Technology Stack
- Amazon S3: Chosen for managed, highly available object storage with zero operational overhead for a 3-engineer team
- Amazon S3 Object Lock & Versioning: Ensures tamper-evident, immutable model storage required for 7-year auditability (R-06)
- Amazon SQS: Decouples deployment notifications to prevent dropped reload signals during ECS Fargate scaling events
- AWS IAM & KMS SSE-S3: Enforces least-privilege access and customer-managed encryption to satisfy PCI-DSS Level 1 compliance
- JSON Manifest & S3 Prefixes: Implements lightweight atomic version pinning and logical staging separation without custom infrastructure

## Rationale
This architecture uses native AWS serverless primitives to maintain high availability and sub-50ms latency without increasing operational complexity for a 3-engineer team. It rigorously enforces PCI-DSS security and 7-year auditability while staying strictly within the 25,000 EUR monthly budget.