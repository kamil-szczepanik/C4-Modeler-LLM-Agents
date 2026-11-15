## Overview
The system is a real-time payment fraud screening platform that evaluates card-not-present payment authorizations to approve, decline, or flag them for review. It provides secure case management for fraud analysts while ensuring strict compliance, high performance, and fault tolerance.

## Key Elements
- Fraud Operations Analysts & Risk Managers
- Payment Gateway / Merchant Systems
- Model Registry / Feature Store
- AWS Application Load Balancer (ALB) / Ingress Router
- Scoring Engine Container (Rust)
- Case Management Container (Python / FastAPI)
- Audit Logger Sidecar Container
- Amazon ElastiCache (Redis)
- Amazon Aurora Serverless v2
- Amazon S3 with Object Lock (Compliance Mode)

## Relationships
- Payment Gateway to AWS ALB via HTTPS (TLS 1.3, HMAC-SHA256, mTLS)
- AWS ALB to Scoring Engine Container via HTTP/REST or gRPC
- Scoring Engine Container to Amazon ElastiCache (Redis) via gRPC / TCP
- Scoring Engine Container to Audit Logger Sidecar via internal message passing
- Audit Logger Sidecar to Amazon S3 via AWS SDK (HTTPS)
- Fraud Analysts to Case Management Container via HTTPS (OAuth 2.0 / OIDC, RBAC, MFA)
- Case Management Container to Amazon Aurora Serverless v2 via SQL/TLS

## Technology Stack
- AWS ECS on Fargate: Selected to minimize operational overhead for a 3-person team within a €25,000 monthly budget.
- Rust (Axum, Tokio): Powers the Scoring Engine for high throughput (3,000 TPS) and sub-50ms P99 latency.
- Python (FastAPI): Powers the Case Management service for rapid developer iteration.
- Amazon ElastiCache (Redis): Provides low-latency feature store lookups.
- Amazon Aurora Serverless v2: Automatically scales relational database resources for analyst workflows.
- Amazon S3 with Object Lock: Enforces tamper-evident, 7-year retention compliance audits.
- AWS KMS & Secrets Manager: Secures data encryption (AES-256) and dynamic credential rotation.

## Rationale
This architecture decouples the high-performance Rust scoring engine from the analyst case management workspace, protecting the strict <50ms latency SLA under heavy load. Utilizing managed AWS serverless services ensures compliance and reliability while remaining maintainable by a 3-person engineering team within a €25,000 monthly budget.