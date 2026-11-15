## Overview
The system is a real-time payment fraud screening platform that evaluates card-not-present payment authorizations and provides case management tools for fraud analysts. It runs on AWS in the eu-west-1 region, targeting PCI-DSS Level 1 compliance while maintaining strict auditability and latency budgets.

## Key Elements
- Fraud Analyst & Risk Engineer (Users)
- Payment Gateway / Acquirer & Payment Network / Card Schemes (External Systems)
- Audit / Compliance Archive & External Notification / Alerting Service (External Systems)
- AWS API Gateway (API Gateway)
- Go Fraud Scoring Engine & Case Management Backend (AWS ECS Fargate, Go, gRPC, AWS Cognito)
- Amazon ElastiCache (Redis) (In-memory cache)
- Amazon Aurora Serverless v2 with Amazon RDS Proxy (Relational database and connection pooler)
- AWS Backup with S3 Object Lock (Immutable compliance storage)

## Relationships
- Go Fraud Scoring Engine -> Amazon RDS Proxy: Executes write-heavy fraud scoring and audit logging [PostgreSQL Wire Protocol over TLS 1.3, IAM Auth]
- Case Management Backend -> Amazon RDS Proxy: Queries case data and reads audit histories [PostgreSQL Wire Protocol over TLS 1.3, IAM Auth, Read Replica Routing]
- Amazon Aurora Serverless v2 -> Audit / Compliance Archive: Exports tamper-evident logs for 7-year retention [AWS S3 Object Lock (Compliance Mode)]

## Technology Stack
- AWS ECS Fargate: Container orchestration for microservices, minimizing operational overhead for a 3-engineer team.
- Amazon Aurora Serverless v2: Scalable relational database meeting performance and budgetary constraints.
- Amazon RDS Proxy: Connection multiplexing and TLS 1.3 enforcement to prevent connection exhaustion from Fargate tasks.
- AWS Backup with S3 Object Lock: Ensures tamper-evident, immutable 7-year audit log retention for compliance.
- PostgreSQL `pgcrypto` & Partitioning: Column-level encryption and time-based table partitioning for efficient, secure auditing.

## Rationale
This architecture uses serverless and managed AWS services to minimize operational complexity for a three-engineer team while easily scaling to meet a 3,000 TPS workload under a 25,000 EUR monthly budget. Rigorous security controls, encryption, and immutable backups satisfy PCI-DSS Level 1 compliance and 7-year auditability mandates.