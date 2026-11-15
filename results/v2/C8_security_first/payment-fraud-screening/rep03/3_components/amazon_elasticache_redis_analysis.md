## Overview
The Real-Time Payment Fraud Screening system processes card-not-present payment authorizations for a mid-size payment processor. It screens transactions for fraud before approval and provides case management tools for fraud analysts.

## Key Elements
- Fraud Operations Analysts & Risk Managers
- Payment Gateway / Merchant Systems
- Model Registry / Feature Store
- Amazon Application Load Balancer (ALB) / Ingress Router
- Scoring Engine Container (Rust, Axum, Tokio)
- Case Management Container (Python, FastAPI)
- Audit Logger Sidecar Container
- Amazon ElastiCache (Redis OSS v7.0+, cache.r6g.xlarge)
- Amazon Aurora Serverless v2
- Amazon S3 with Object Lock (Compliance Mode)

## Relationships
- Payment Gateway -> Amazon ALB: Sends payment authorization requests [HTTPS / REST]
- Amazon ALB -> Scoring Engine Container: Forwards authorization requests [HTTP/2 / gRPC]
- Scoring Engine Container -> Amazon ElastiCache (Redis): Performs low-latency feature store lookups [gRPC / TCP over TLS 1.3]
- Scoring Engine Container -> Model Registry / Feature Store: Retrieves scoring models [HTTPS]
- Scoring Engine Container -> Audit Logger Sidecar Container: Emits tamper-evident decision logs [Local IPC / gRPC]
- Audit Logger Sidecar Container -> Amazon S3 with Object Lock: Stores immutable audit logs [AWS SDK / HTTPS]
- Case Management Container -> Amazon Aurora Serverless v2: Manages analyst review cases [SQL / TLS]
- Fraud Operations Analysts -> Amazon ALB: Accesses case management UI [HTTPS]

## Technology Stack
- AWS (Region: eu-west-1): Chosen cloud provider meeting infrastructure requirements within budget.
- Rust (Axum, Tokio): Used for the Scoring Engine to achieve sub-50 ms P99 latency at 3,000 TPS.
- Python (FastAPI): Powers the Case Management container for rapid development by a 3-engineer team.
- Amazon ElastiCache (Redis OSS v7.0+): Provides high-performance in-memory feature caching.
- Amazon Aurora Serverless v2: Provides scalable, relational data storage for case management.
- Amazon S3 with Object Lock (Compliance Mode): Ensures 7-year tamper-evident auditability.

## Rationale
This architecture uses managed AWS services to minimize operational overhead for a three-engineer team while strictly enforcing PCI-DSS Level 1 compliance. The technology choices guarantee sub-50 ms P99 decision latency at 3,000 TPS within a fixed 25,000 EUR monthly budget.