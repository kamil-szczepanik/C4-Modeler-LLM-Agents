## Overview
The system is a real-time payment fraud screening platform that evaluates card-not-present payment authorizations and provides case management for fraud analysts. It is hosted on AWS in region eu-west-1, adhering to PCI-DSS Level 1 compliance and a 7-year audit retention mandate.

## Key Elements
- Fraud Analysts (Users)
- Payment Gateway (External System)
- AWS ECS with Fargate Containers (API Gateway, Tokenization/Masking Proxy, Real-Time Scoring Engine, Case Management, Model & Rule Registry, Audit & Compliance)
- Amazon ElastiCache (Redis)
- Amazon Aurora
- Amazon SQS / SNS
- Amazon S3 Object Lock (WORM storage with S3 Glacier Lifecycle policies)

## Relationships
- Payment Gateway -> API Gateway: Forwards authorization requests [HTTPS/TLS 1.3, OpenAPI / AsyncAPI]
- Real-Time Scoring Engine -> Amazon Aurora & Amazon ElastiCache (Redis): Fetches scoring rules and caches state [gRPC/REST]
- Audit & Compliance Container -> Amazon S3 Object Lock: Writes tamper-evident audit logs with client-side SHA-256 hashes and schema versions [AWS SDK]
- Audit & Compliance Container -> Amazon SQS / SNS: Buffers payloads and handles dead-letter queues during transient S3 degradation [AWS SDK]

## Technology Stack
- AWS ECS with Fargate: Chosen for container orchestration within a 3-engineer team capacity.
- Amazon S3 Object Lock (Compliance Mode): Selected for immutable, 7-year Write-Once-Read-Many (WORM) audit compliance.
- S3 Lifecycle Policies: Automatically transitions logs to Glacier Flexible Archive to meet the 25,000 EUR/month budget.
- SHA-256 Cryptographic Hashing: Applied at the application layer for independent data integrity verification.

## Rationale
This architecture uses serverless and managed AWS services to minimize operational overhead for a three-engineer team while meeting strict P99 latency (<50ms) and PCI-DSS compliance standards. Automated cost-tiering and immutable storage mechanisms ensure the system satisfies 7-year audit rules within the fixed monthly budget constraint.