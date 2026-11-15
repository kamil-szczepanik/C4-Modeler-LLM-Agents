## Overview
The system screens card-not-present payment authorizations for fraud in real-time and provides case management tools for fraud analysts. It is operated by a three-engineer team under strict budget and compliance constraints.

## Key Elements
- Fraud Analyst
- Shopper / Cardholder
- Merchant / Payment Gateway
- AWS ALB / API Gateway
- Real-Time Scoring Engine (Go, Amazon ECS Fargate)
- Amazon ElastiCache (Redis)
- Case Management & Analytics API
- Frontend Web App (React SPA)
- Amazon RDS PostgreSQL (Case Management Schema, Audit & Explainability Log, Partition Manager, Data Purge & TTL Worker)
- Amazon S3 with Object Lock and AWS KMS
- AWS Kinesis Data Streams / Amazon SQS
- AWS Lambda
- PgBouncer / Amazon RDS Proxy

## Relationships
- Case Management & Analytics API -> Amazon RDS PostgreSQL: Reads and writes active cases and audit logs [TCP/TLS/SQL]
- Partition Manager -> Amazon S3 with Object Lock: Offloads expired partitions [HTTPS]
- AWS Lambda -> Amazon S3 with Object Lock: Archives data partitions [HTTPS]
- Frontend Web App -> Case Management & Analytics API: Manages review cases [HTTPS/REST]

## Technology Stack
- Amazon RDS PostgreSQL: Relational database with `pg_partman` for structured data storage and partitioning.
- AWS Lambda: Serverless compute for running automated data archival pipelines.
- Amazon S3 with Object Lock and AWS KMS: Immutable, encrypted storage for 7-year audit retention.
- PgBouncer / Amazon RDS Proxy: Connection pooling to prevent database connection exhaustion.
- TLS 1.3: Network transport security protocol for strict PCI-DSS compliance.

## Rationale
This architecture uses automated partitioning and S3 archiving to maintain sub-50ms query performance while complying with 7-year audit rules under a 25,000 EUR budget. Schema decomposition and connection pooling ensure high availability and security for a three-engineer team.