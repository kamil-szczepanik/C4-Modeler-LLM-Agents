## Overview
[System screen card-not-present payment authorizations for fraud in real-time, providing case management and tamper-evident 7-year audit logs for analysts and compliance auditors.]

## Key Elements
- Fraud Scoring Engine (Go, Amazon ECS on EC2)
- Case Management Backend (Node.js/TypeScript, Amazon ECS Fargate)
- Audit Ingestion Component (Go)
- Ledger Storage Engine (Amazon Aurora PostgreSQL Ledger Tables)
- Retention & Archival Component (AWS Step Functions + Amazon ECS Fargate + Amazon S3 Object Lock)
- Auditor Query Service (Go)

## Relationships
- Fraud Scoring Engine -> Audit Ingestion Component: Writes decision logs via internal HTTP/gRPC [AWS SDK, mTLS, IAM]
- Case Management Backend -> Audit Ingestion Component: Writes audit trails via internal HTTP/gRPC [AWS SDK, mTLS, IAM]
- Case Management Backend -> Auditor Query Service: Requests audit bundles via internal REST API [TLS 1.3]
- Retention & Archival Component -> Ledger Storage Engine: Offloads historical partitions [PostgreSQL wire protocol]
- Retention & Archival Component -> Amazon S3: Stores WORM-compliant archives [HTTPS/TLS 1.3]

## Technology Stack
- Go: Used for high-throughput audit ingestion and query services to maintain sub-50ms constraints
- Amazon Aurora PostgreSQL: Utilizes ledger tables for cryptographic immutability and simple operations
- Amazon S3 Object Lock: Provides cost-effective, WORM-compliant 7-year retention within budget
- AWS KMS: Enforces envelope encryption and customer-managed keys for data protection
- AWS Cognito & Secrets Manager: Secures authentication, authorization, and automated credential rotation

## Rationale
[This architecture satisfies PCI-DSS Level 1 compliance and 7-year tamper-evident auditability using managed AWS services. It stays within the 25,000 EUR monthly budget and can be operated by a 3-engineer team.]