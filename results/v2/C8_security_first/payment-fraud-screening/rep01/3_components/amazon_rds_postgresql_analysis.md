## Overview
Real-Time Payment Fraud Screening screens card-not-present payment authorizations for a mid-size payment processor using AWS. It processes transactions to approve, decline, or flag them while supporting analyst case management.

## Key Elements
- Fraud Analysts & Risk Managers
- API Gateway (AWS API Gateway - HTTP APIs)
- Scoring Engine Container (Go, ONNX runtime, Amazon ECS on AWS Fargate)
- Case Management Container (Next.js / Node.js, Amazon ECS on AWS Fargate)
- Amazon RDS PostgreSQL (Database with schemas: `cases_db`, `audit_log`, PgBouncer/RDS Proxy)
- Amazon S3 WORM Bucket & Model Bucket (Amazon S3 with WORM Object Lock)
- AWS Lambda & Amazon EventBridge (Audit log archival pipeline)
- Supporting Services: Amazon SQS, Amazon Athena, AWS Secrets Manager, AWS KMS

## Relationships
- Case Management Container -> Amazon RDS PostgreSQL: Reads and writes case and audit data via SQL over [TLS 1.3] with IAM Database Authentication
- AWS Lambda -> Amazon RDS PostgreSQL & Amazon S3 WORM Bucket: Exports and purges audit partitions older than 90 days via scheduled [HTTPS]
- Amazon RDS PostgreSQL -> Amazon CloudWatch: Streams `pgaudit` logs and performance metrics over [HTTPS]
- Fraud Analysts -> API Gateway / Case Management Container: Reviews flagged payments via secure web interface over [HTTPS]

## Technology Stack
- Amazon RDS PostgreSQL: Relational database chosen for low operational overhead and ACID compliance, fitting the 3-engineer team constraint
- AWS RDS Proxy / PgBouncer: Connection pooling to handle high-concurrency connection spikes and prevent backend exhaustion
- PostgreSQL `pgaudit` & Trigger-Based RLS: Enforces least privilege, row-level security, and immutable audit logs for PCI-DSS compliance
- Amazon S3 with WORM Object Lock: Cost-effective long-term storage for 7-year tamper-evident audit logs within the 25,000 EUR/month budget

## Rationale
This architecture meets PCI-DSS Level 1 compliance and 7-year audit requirements securely through immutable S3 offloading and RDS security controls. It stays within budget and team limits by utilizing managed AWS services and automated data lifecycles.