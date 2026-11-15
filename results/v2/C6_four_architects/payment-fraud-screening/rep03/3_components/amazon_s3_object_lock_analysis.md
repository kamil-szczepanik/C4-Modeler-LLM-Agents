## Overview
The system screens card-not-present payment authorizations in real-time for fraud and provides case management for human analysts. It ensures PCI-DSS Level 1 compliance and tamper-evident 7-year audit retention on AWS.

## Key Elements
- Fraud Analysts
- Scoring Engine Container (Go, ONNX Runtime, AWS ECS Fargate)
- Case Management Backend Container (Node.js, TypeScript, AWS ECS Fargate)
- Amazon S3 Object Lock Container (Compliance Mode, S3 Glacier Deep Archive)
- Internal Components: Object Writer, Lifecycle Management, Audit Verification, Access Control & Compliance Policy Manager, Metadata Indexer
- Supporting Services: Amazon DynamoDB, AWS KMS, Amazon SQS/SNS

## Relationships
- Scoring Engine Container -> Object Writer Component: Writes decision payloads [AWS SDK, HTTPS]
- Case Management Backend Container -> Object Writer Component: Writes human review audit trails [AWS SDK, HTTPS]
- Object Writer Component -> AWS S3 Storage Layer: Persists immutable objects [AWS SDK, HTTPS]
- Lifecycle Management Component -> AWS S3 Storage Layer: Configures transition to S3 Glacier Deep Archive [AWS SDK, HTTPS]
- Audit Verification Component -> AWS S3 Storage Layer: Reads and verifies object integrity [AWS SDK, HTTPS]
- Access Control & Compliance Policy Manager -> AWS S3 Storage Layer: Configures bucket compliance parameters [AWS IAM / AWS SDK, HTTPS]
- Access Control & Compliance Policy Manager -> AWS KMS: Enforces server-side encryption [AWS SDK, HTTPS]
- AWS S3 Storage Layer -> Metadata Indexer Component: Triggers event notifications [S3 Event Notifications, HTTPS]
- Metadata Indexer Component -> Amazon DynamoDB: Persists audit metadata pointers [AWS SDK, HTTPS]

## Technology Stack
- Amazon S3 Object Lock in Compliance Mode: Ensures immutable, tamper-evident 7-year retention (R-06)
- S3 Glacier Deep Archive: Optimizes storage costs to meet the 25,000 EUR/month budget
- AWS KMS: Encrypts data at rest for PCI-DSS Level 1 compliance (R-05)
- Amazon DynamoDB & SQS/SNS: Indexes audit metadata for rapid auditor querying without full-bucket scans
- AWS SDK (HTTPS): Protocol for secure intra-container and AWS service communication

## Rationale
This architecture uses managed AWS cloud services to meet strict PCI-DSS and 7-year auditability mandates while staying within a 25,000 EUR monthly budget and supporting a 3-engineer team. Automated tiering and indexing balance deep storage compliance with high-performance query access.