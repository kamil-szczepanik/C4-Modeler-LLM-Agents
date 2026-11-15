## Overview
The Real-Time Payment Fraud Screening system screens card-not-present payment authorizations for fraud below 50 ms P99 latency while enabling secure analyst case management. It guarantees 7-year tamper-evident auditability for every decision under PCI-DSS Level 1 compliance.

## Key Elements
- Fraud Analyst, ML Engineer / Data Scientist, Finance / Operations Manager, Compliance Auditor
- AWS API Gateway / NLB, AWS Lambda / Worker, Amazon S3 with Object Lock
- Fraud Scoring Engine (Go), Case Management Backend (Java / Spring Boot with React UI)
- Feature Store (Amazon ElastiCache for Redis), Relational Store (Amazon RDS for PostgreSQL)
- Tamper-Evident Storage (Amazon S3 with Object Lock in Compliance Mode)
- Message Queue (Amazon SQS with AWS KMS encryption), Amazon Athena

## Relationships
- `Audit Logger` -> `Tamper-Evident Storage`: Appends immutable decision logs [HTTPS / S3 API via VPC Endpoint]
- `Compliance Auditor` -> `Tamper-Evident Storage`: Queries audit bundles [HTTPS via Presigned URLs / Athena]
- `Fraud Scoring Engine` -> `Feature Store`: Retrieves user features [Redis Protocol / TCP]
- `Fraud Scoring Engine` -> `Relational Store`: Persists scoring rules and metadata [PostgreSQL Wire Protocol / TCP]

## Technology Stack
- AWS (eu-west-1): Target cloud infrastructure within fixed 25,000 EUR/month budget.
- Go & Java/Spring Boot: High-performance backend containers meeting strict P99 latency.
- Amazon S3 (Object Lock Compliance Mode): WORM storage guaranteeing 7-year tamper-evident retention.
- Amazon S3 Glacier Deep Archive: Cost-effective long-term storage tier for budget compliance.
- Amazon Athena: Serverless SQL querying engine for audit log analysis.

## Rationale
This architecture uses serverless and managed AWS services to minimize operational overhead for a three-engineer team while satisfying strict PCI-DSS Level 1 and 7-year auditability mandates. Lifecycle tiering to Glacier ensures long-term compliance remains within the 25,000 EUR/month budget.