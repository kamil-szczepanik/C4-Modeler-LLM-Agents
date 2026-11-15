## Overview
The Real-Time Payment Fraud Screening system evaluates card-not-present payment authorizations to approve, decline, or flag suspicious transactions while ensuring PCI-DSS Level 1 compliance. It delivers sub-50ms fraud decisions and provides comprehensive auditability for compliance officers.

## Key Elements
- Ingress Router Component (Go/Rust)
- Feature Aggregator Component (Go/Rust)
- Execution & Scoring Component (Go/Rust)
- Audit & Persistence Dispatcher Component (Go/Rust)
- Fallback Circuit Breaker Component (Go/Rust)
- API Gateway / Ingress Container (AWS API Gateway or Envoy)
- Fraud Scoring Engine Container (Go or Rust)
- Case Management Container (Node.js/Python + React SPA on Amazon S3 / CloudFront)
- Model Registry Container (MLflow on Amazon ECS)
- Database & Storage (Amazon Aurora Serverless v2)
- Caching Layer (Amazon ElastiCache with Redis OSS)

## Relationships
- API Gateway / Ingress Container -> Fraud Scoring Engine Container [gRPC over AWS VPC internal networks via mTLS]
- Fraud Scoring Engine Container -> Caching Layer [Redis OSS Protocol over TLS]
- Fraud Scoring Engine Container -> Database & Storage [PostgreSQL Wire Protocol via AWS IAM authentication]
- Model Registry Container -> Fraud Scoring Engine Container [S3 memory caching and read-only S3 sync sidecar]
- Case Management Container -> Database & Storage [PostgreSQL Wire Protocol]

## Technology Stack
- Go or Rust: Selected for the fraud scoring engine to eliminate garbage collection pauses and achieve sub-50ms P99 latency.
- AWS ECS on Fargate: Chosen to operate containers without Kubernetes management overhead within budget.
- Amazon Aurora Serverless v2: Utilized for scalable transactional and audit data persistence.
- Amazon ElastiCache with Redis OSS: Deployed for low-latency feature lookups and rate limiting.
- MLflow on Amazon ECS: Implemented for zero-downtime model and rule registry management.

## Rationale
This architecture uses memory-safe compiled languages, asynchronous logging, and containerized serverless infrastructure to meet strict sub-50ms latency and high-throughput requirements within budget. Robust fallback mechanisms and automated security controls ensure PCI-DSS compliance and high availability.