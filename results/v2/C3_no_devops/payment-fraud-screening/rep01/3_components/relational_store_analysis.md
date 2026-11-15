## Overview
The system provides real-time payment fraud screening for card-not-present transactions and managed case reviews for fraud analysts. It ensures sub-50 ms decisions, strict compliance, and 7-year auditability on AWS.

## Key Elements
- **Users**: Fraud Analyst, ML Engineer / Data Scientist, Finance / Operations Manager
- **External Systems**: Payment Gateway / Core Processing Engine, Card Schemes / Identity Providers, Archival Storage / Compliance Ledger
- **Containers**: AWS API Gateway / NLB, Fraud Scoring Engine (Go), Case Management Backend (Java / Spring Boot with React UI), Audit Logger (AWS Lambda / Worker), Feature Store (AWS ElastiCache for Redis), Relational Store (Amazon RDS for PostgreSQL), Tamper-Evident Storage (Amazon S3), Message Queue (Amazon SQS)
- **Relational Store Components**: Case Repository Component, Audit Ledger Index Component, Database Migration Manager

## Relationships
- Case Management Backend -> Relational Store: Persists and retrieves case state [PostgreSQL wire protocol (TCP/IP) via TLS 1.3]
- Audit Logger -> Relational Store: Streams advanced audit logs [PostgreSQL wire protocol (TCP/IP) via TLS 1.3]
- Database Migration Manager -> Relational Store: Executes schema migrations [Flyway / TCP/IP]

## Technology Stack
- **Amazon RDS for PostgreSQL (`db.m6g.xlarge`)**: Managed relational persistence layer balancing multi-AZ high availability with cost constraints.
- **AWS KMS & AWS Secrets Manager**: AES-256 storage-level encryption, transparent column-level encryption, and automated 30-day credential rotation for security compliance.
- **PostgreSQL Row-Level Security (RLS) & Advanced Auditing**: Enforces strict data segregation for analysts and tamper-evident logging for PCI-DSS.
- **Flyway**: Zero-downtime schema migrations supporting rule and model evolution.
- **AWS (eu-west-1)**: Target cloud provider complying with infrastructure budget and residency requirements.

## Rationale
This architecture meets PCI-DSS Level 1 and 7-year audit mandates while staying within the 25,000 EUR monthly budget through managed AWS services. It empowers a three-engineer team to maintain high availability, security, and sub-200 ms case query latencies under peak loads.