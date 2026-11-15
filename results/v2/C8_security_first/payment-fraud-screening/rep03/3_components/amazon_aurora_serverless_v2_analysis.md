## Overview
The Real-Time Payment Fraud Screening system evaluates card-not-present payment authorizations for fraud, while providing case management tools for fraud analysts. It operates within strict AWS infrastructure and PCI-DSS compliance boundaries to ensure rapid scoring and secure review workflows.

## Key Elements
* Fraud Operations Analysts & Risk Managers
* Payment Gateway / Merchant Systems
* AWS Application Load Balancer (ALB)
* Scoring Engine Container (Rust, Axum, Tokio)
* Case Management Container (Python, FastAPI)
* Audit Logger Sidecar Container
* Amazon ElastiCache (Redis)
* Amazon Aurora Serverless v2 (PostgreSQL)
* AWS RDS Proxy
* Amazon S3 with Object Lock (Compliance Mode)

## Relationships
* Payment Gateway -> AWS ALB: Forwards payment authorization requests [HTTPS/TLS 1.3]
* AWS ALB -> Scoring Engine Container: Routes real-time scoring payloads [HTTP/REST]
* Scoring Engine Container -> Amazon ElastiCache (Redis): Fetches fraud rules and model metadata [RESP]
* Case Management Container -> AWS RDS Proxy: Queries and updates case data securely [SQL/TLS 1.3 via IAM Auth]
* AWS RDS Proxy -> Amazon Aurora Serverless v2: Manages database connection pool and query routing [SQL/TLS 1.3]
* Audit Logger Sidecar Container -> Amazon S3 with Object Lock: Persists immutable, tamper-evident audit logs [HTTPS/TLS 1.3]

## Technology Stack
* Rust (Axum, Tokio): Chosen for the scoring engine to guarantee sub-50ms P99 latency at high throughput.
* Python (FastAPI): Chosen for case management to enable rapid feature delivery by a 3-engineer team.
* Amazon Aurora Serverless v2 (PostgreSQL): Selected for scalable relational storage with automated multi-AZ high availability.
* AWS RDS Proxy: Deployed to prevent database connection exhaustion and handle traffic spikes.
* Amazon S3 with Object Lock (Compliance Mode): Utilized to satisfy the 7-year tamper-evident auditability constraint.
* AWS KMS & Secrets Manager: Implemented for encrypted data at rest and automated credential rotation to meet PCI-DSS Level 1.

## Rationale
The architecture combines high-performance Rust components with scalable AWS managed services to meet strict sub-50ms latency SLAs and PCI-DSS compliance. Operational overhead is minimized for the 3-engineer team through serverless scaling, managed proxies, and automated CI/CD pipelines within the 25,000 EUR monthly budget.