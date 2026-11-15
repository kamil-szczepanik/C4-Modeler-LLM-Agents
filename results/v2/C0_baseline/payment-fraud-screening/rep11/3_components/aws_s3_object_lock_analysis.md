## Overview
This system provides real-time payment fraud screening for a mid-size payment processor, analyzing card-not-present transactions before approval. It ensures PCI-DSS compliance, explainable audit trails, and strict cost controls.

## Key Elements
- Fraud Analyst & Risk/Compliance Officer (Users)
- Merchant / Payment Gateway & Tokenization Provider (External Systems)
- AWS API Gateway & ACM Private CA (Ingress)
- Fraud Screening Engine (Go/Rust, Amazon ECS on EC2)
- Case Management Frontend (React SPA, CloudFront, S3) & Backend (Python FastAPI)
- Audit & Compliance Worker (Python, Amazon SQS)
- Redis (Amazon ElastiCache) & Amazon ECR
- AWS S3 Object Lock & AWS KMS (Audit Archive)
- Amazon Athena & AWS Secrets Manager

## Relationships
- Fraud Screening Engine -> Merchant / Payment Gateway: Returns approve, decline, or review decisions [HTTPS / REST]
- Fraud Screening Engine -> Amazon ElastiCache for Redis: Retrieves rules and session state [Redis Protocol / TLS]
- Audit & Compliance Worker -> AWS S3 Object Lock: Writes immutable audit objects [HTTPS / S3 API with AWS Signature V4]
- S3 Bucket -> AWS KMS: Encrypts and decrypts audit logs [AWS internal API]
- Risk / Compliance Officer -> S3 Bucket: Queries immutable audit logs via Amazon Athena [HTTPS / Athena API]

## Technology Stack
- AWS (eu-west-1): Target cloud infrastructure chosen for managed security and compliance tooling.
- Go / Rust: High-performance backend languages for sub-50ms fraud screening latencies.
- Amazon ECS on EC2: Container orchestration supporting fixed infrastructure budget constraints.
- Amazon ElastiCache for Redis: In-memory store for low-latency rule evaluation.
- AWS S3 Object Lock & Glacier Deep Archive: WORM storage enforcing 7-year tamper-evident retention within budget.

## Rationale
This architecture meets sub-50ms P99 latency requirements and PCI-DSS Level 1 compliance through localized containerized services and AWS managed security controls. It strictly adheres to the 25,000 EUR monthly budget and three-engineer operational limit using serverless storage tiers and automated Terraform infrastructure.