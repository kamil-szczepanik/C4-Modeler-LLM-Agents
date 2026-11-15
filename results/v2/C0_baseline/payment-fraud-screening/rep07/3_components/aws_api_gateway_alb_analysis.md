## Overview
The system provides real-time payment fraud screening for a mid-size payment processor and case management for fraud analysts. It ingests and evaluates authorization requests while maintaining strict compliance, performance, and budget constraints.

## Key Elements
- Payers and Fraud Analysts (Users)
- Payment Gateway/Acquirer and Identity Provider (External Systems)
- AWS API Gateway / ALB (Ingress Layer)
- Real-Time Scoring Engine (Amazon EC2, Go/Rust)
- Case Management Backend (AWS ECS Fargate, Node.js/TypeScript)
- Case Management UI (Amazon S3, Amazon CloudFront, React)
- Redis Cache (Amazon ElastiCache)
- PostgreSQL Database (Amazon RDS)
- Audit Storage (Amazon S3 with KMS and Object Lock)
- Messaging Bus (Amazon SQS / EventBridge)

## Relationships
- Payment Gateway/Acquirer -> AWS API Gateway / ALB: Forwards authorization requests [HTTPS/gRPC]
- AWS API Gateway / ALB -> Real-Time Scoring Engine: Communicates scoring requests using local circuit breaker [mTLS]
- Case Management UI -> AWS API Gateway / ALB: Sends management and review traffic [HTTPS]
- AWS API Gateway / ALB -> Case Management Backend: Routes administrative and review APIs [HTTPS]

## Technology Stack
- AWS ALB: Handles high-throughput payment ingestion for sub-50ms latency.
- AWS API Gateway: Manages case management APIs and IdP integrations.
- Amazon EC2: Hosts the real-time scoring engine for optimal CPU performance.
- AWS ECS Fargate: Runs containerized case management backend with low operational overhead.
- Amazon S3 with Object Lock: Stores tamper-evident audit logs to meet 7-year compliance.

## Rationale
This architecture uses managed AWS services to minimize maintenance overhead for a three-engineer team within a strict 25,000 EUR monthly budget. The split ingress topology separates high-throughput payment traffic from management APIs to guarantee sub-50ms P99 latency and PCI-DSS Level 1 compliance.