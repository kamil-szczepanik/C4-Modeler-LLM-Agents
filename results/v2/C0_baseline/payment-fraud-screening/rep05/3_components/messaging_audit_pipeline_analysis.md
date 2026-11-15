## Overview
Real-time payment fraud screening system processing card-not-present transactions for a mid-size payment processor. It provides sub-50ms fraud scoring and case management while ensuring strict compliance, auditability, and cost efficiency.

## Key Elements
- Fraud Analyst & Risk/Compliance Officer (Users)
- Payment Gateway / Merchants & Card Tokenization Vault (External Systems)
- Real-Time Scoring Engine (Go on Amazon ECS Fargate container)
- Case Management App (Node.js/TypeScript on Amazon ECS Fargate container)
- Messaging & Audit Pipeline (Amazon SQS and Amazon S3 with Object Lock)
- Feature Store & Cache (Amazon ElastiCache Redis)
- Database (Amazon Aurora PostgreSQL Serverless v2)
- Model Registry (Amazon SageMaker Model Registry)
- Network & Security (AWS WAF, Amazon API Gateway, AWS Secrets Manager, AWS KMS)

## Relationships
- Payment Gateway -> API Gateway: Forwards authorization requests [HTTPS / TLS 1.3]
- Real-Time Scoring Engine -> Messaging & Audit Pipeline: Publishes asynchronous events and logs [AWS SDK / HTTPS over VPC Endpoints]
- Messaging & Audit Pipeline -> Immutable Audit Sink: Writes tamper-evident logs [Amazon S3 Object Lock Compliance Mode and AWS KMS]
- Fraud Analyst -> Case Management App: Reviews flagged transactions [HTTPS]

## Technology Stack
- Compute: Amazon ECS Fargate (Go for scoring/workers, Node.js/TypeScript for case management) for predictable resource usage and zero Lambda cold starts
- Storage & Caching: Amazon Aurora PostgreSQL Serverless v2 and Amazon ElastiCache Redis for relational data and low-latency feature retrieval
- Messaging & Audit: Amazon SQS and Amazon S3 with Object Lock (Compliance Mode) using AWS KMS for 7-year tamper-evident audit logs
- Lifecycle Management: Amazon S3 Lifecycle Policies transitioning to S3 Glacier Deep Archive after 30 days to meet budget constraints

## Rationale
This architecture uses serverless containers and managed AWS services to guarantee P99 latency under 50 ms at 3,000 TPS within a 25,000 EUR monthly budget. It enforces PCI-DSS Level 1 compliance and 7-year auditability via S3 Object Lock and AWS KMS while remaining maintainable for a three-person engineering team.