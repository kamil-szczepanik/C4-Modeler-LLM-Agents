## Overview
The Real-Time Payment Fraud Screening system evaluates card-not-present payment authorizations to detect fraud and manage analyst reviews. It ensures strict PCI-DSS Level 1 compliance and 7-year auditability while operating under a strict budget and lean engineering team.

## Key Elements
- Fraud Analyst & Risk/Compliance Officer (Users)
- Real-Time Scoring Engine (Go on Amazon ECS Fargate)
- Case Management App (Node.js/TypeScript on Amazon ECS Fargate)
- Feature Store & Cache (Amazon ElastiCache Redis)
- Database (Amazon Aurora PostgreSQL Serverless v2 with PgBouncer)
- Messaging & Audit Pipeline (Amazon SQS/SNS and Amazon S3 with Object Lock)
- Model Registry (Amazon SageMaker Model Registry)
- Network & Security (AWS WAF, Amazon API Gateway, AWS Secrets Manager, AWS KMS)

## Relationships
- Case Management App -> Database: Reads and writes relational case data via SQL over TLS 1.3 (TCP/5432)
- Real-Time Scoring Engine -> Reference Data Store: Queries dynamic rules and model metadata via SQL over TLS 1.3 (TCP/5432)
- Real-Time Scoring Engine -> Messaging & Audit Pipeline: Asynchronously writes decision logs to Amazon S3 Object Lock

## Technology Stack
- Amazon Aurora PostgreSQL Serverless v2: Relational database with PgBouncer connection pooling for cost-efficient scalability and strict schema boundaries
- Amazon S3 with Object Lock: Immutable, cost-effective storage for 7-year audit logs and historical case data tiering
- AWS KMS & AWS Secrets Manager: Encryption-at-rest and automated credential rotation for PCI-DSS Level 1 compliance

## Rationale
This architecture uses serverless and managed AWS services to minimize operational overhead for a three-engineer team. It maintains sub-50ms P99 latency and high availability while strictly enforcing budget limits through autoscaling constraints and audit data offloading.