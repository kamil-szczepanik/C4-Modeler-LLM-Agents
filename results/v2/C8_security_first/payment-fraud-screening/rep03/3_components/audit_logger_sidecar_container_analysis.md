## Overview
[The system is a real-time payment fraud screening platform that evaluates card-not-present transactions for fraud and provides case management for human analysts. Its core purpose is to screen authorizations in real time while maintaining strict PCI-DSS compliance and immutable 7-year audit trails.]

## Key Elements
- Fraud Operations Analysts & Risk Managers
- Payment Gateway / Merchant Systems
- AWS Application Load Balancer (ALB) / Ingress Router
- Scoring Engine Container (Rust)
- Case Management Container (Python / FastAPI)
- Audit Logger Sidecar Container (Rust)
- Amazon ElastiCache (Redis)
- Amazon Aurora Serverless v2
- Amazon S3 with Object Lock (Compliance Mode)

## Relationships
- Payment Gateway -> AWS ALB: Sends payment authorization requests [HTTPS / JSON]
- AWS ALB -> Scoring Engine Container (Rust): Routes scoring requests [HTTP/2 / gRPC]
- Scoring Engine Container -> Amazon ElastiCache (Redis): Fetches real-time features [Redis Protocol over TLS]
- Scoring Engine Container -> Amazon Aurora Serverless v2: Queries historical data [PostgreSQL Wire Protocol over TLS]
- Scoring Engine Container -> Audit Logger Sidecar Container: Forwards audit payloads [gRPC over UNIX Domain Sockets]
- Audit Logger Sidecar Container -> Amazon S3 with Object Lock: Streams signed audit logs [AWS SDK via HTTPS / TLS 1.3]
- Fraud Analysts -> Case Management Container: Reviews flagged transactions [HTTPS]

## Technology Stack
- **Compute & Routing:** AWS Application Load Balancer (ALB), Kubernetes (EKS) for container orchestration, optimized for EU West 1.
- **Scoring Engine:** Rust (Axum, Tokio) for high-throughput, low-latency processing (<50ms P99 at 3,000 TPS).
- **Audit Logger Sidecar:** Rust (tokio, aws-sdk-s3) with an in-memory ring buffer and encrypted `emptyDir` spill-to-disk buffer.
- **Case Management:** Python / FastAPI for analyst workflows.
- **Data & Caching:** Amazon Aurora Serverless v2 (SQL/TLS) and Amazon ElastiCache (Redis) for low-latency feature stores.
- **Storage & Security:** Amazon S3 with Object Lock (Compliance Mode) for tamper-evident 7-year audit retention and local host disk encryption (LUKS).

## Rationale
[This architecture strictly satisfies PCI-DSS Level 1 and tamper-evident audit mandates (R-06) via isolated UNIX domain sockets, cryptographic signing, and S3 Object Lock. It meets high-performance throughput and latency constraints (R-04) using a lightweight Rust sidecar and in-memory buffering while staying well within the €25,000 monthly infrastructure budget for a three-engineer team.]