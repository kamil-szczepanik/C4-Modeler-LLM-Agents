## Overview
This system provides real-time payment fraud screening and case management for card-not-present transactions, ensuring sub-50ms latency and strict PCI-DSS Level 1 compliance. It enables fraud analysts to review suspicious payments while maintaining an immutable, tamper-evident audit trail for 7 years.

## Key Elements
* Payers, Fraud Analysts, and Risk Managers/Quants (Users)
* Payment Gateway/Acquirer, Core Banking/Card Network Systems, and Identity Provider (External Systems)
* AWS API Gateway / ALB (Ingress)
* Real-Time Scoring Engine (Containerized microservice on Amazon EC2 with auto-scaling)
* Case Management Backend (ECS Fargate service built with Node.js/TypeScript)
* Case Management UI (React Single-Page App hosted in Amazon S3 via CloudFront)
* Data & State: Redis (ElastiCache), PostgreSQL (RDS), and Amazon S3 with KMS and Object Lock
* Messaging & Security: Amazon SQS/EventBridge, AWS Secrets Manager, and AWS App Mesh / Istio

## Relationships
* Payers interact with the Payment Gateway, which forwards authorization requests via HTTPS/gRPC to AWS API Gateway.
* AWS API Gateway communicates with the Real-Time Scoring Engine over mTLS, utilizing a local fallback circuit breaker for availability.
* Real-Time Scoring Engine performs sub-millisecond feature lookups against Redis (ElastiCache).
* Fraud Analysts access the Case Management UI (CloudFront/S3), which communicates with the Case Management Backend (ECS Fargate) via HTTPS/OAuth2/OIDC.
* Case Management Backend reads/writes transactional case data to PostgreSQL (RDS).
* Scoring decisions, model versions, explanations, and analyst overrides are streamed via Amazon SQS/EventBridge and stored in Amazon S3 with Object Lock for 7-year auditability.

## Technology Stack
* Real-Time Scoring Engine: Go or Rust on Amazon EC2 for predictable memory and P99 latency < 50ms.
* Case Management Backend: Node.js/TypeScript on AWS ECS Fargate for rapid analyst tooling.
* Frontend: React hosted on Amazon S3 and delivered via Amazon CloudFront.
* Database & Caching: Amazon RDS (PostgreSQL) with row-level encryption and Amazon ElastiCache (Redis).
* Storage & Compliance: Amazon S3 with KMS and Object Lock (compliance mode) for 7-year audit retention.
* Networking & Security: AWS API Gateway/ALB, AWS App Mesh/Istio for mTLS, and AWS Secrets Manager.
* Deployment & Observability: AWS CodeDeploy (blue/green deployments), AWS CloudWatch, Prometheus, and Grafana.

## Rationale
This architecture isolates the high-throughput scoring engine on EC2 to guarantee sub-50ms P99 latencies under high transaction volume. Serverless and managed AWS components minimize operational overhead to fit a 3-person engineering team and a 25,000 EUR monthly budget while satisfying stringent PCI-DSS Level 1 and 7-year auditability requirements.