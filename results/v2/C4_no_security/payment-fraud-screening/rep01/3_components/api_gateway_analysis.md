## Overview
The system screens card-not-present payment authorizations for fraud in real-time and provides a case management interface for analysts. It ensures PCI-DSS Level 1 compliance while maintaining sub-50ms latency at 3,000 transactions per second within a fixed AWS budget.

## Key Elements
- Merchant / Payment Gateway
- External Identity Provider (IdP)
- API Gateway (AWS API Gateway / ALB, AWS WAF)
- Real-Time Scoring Engine (Go, AWS ECS Fargate, ONNX)
- Case Management Backend & UI (React, Node.js / Python, ECS Fargate)
- Feature Store (Amazon ElastiCache Redis)
- Audit Log Storage (Amazon S3, Amazon Athena)

## Relationships
- Merchant / Payment Gateway -> API Gateway: Sends payment authorizations [HTTPS / TLS 1.3]
- API Gateway -> Real-Time Scoring Engine: Forwards payment authorizations [gRPC over TLS]
- Case Management UI -> Case Management Backend: Manages review cases [HTTPS]
- Real-Time Scoring Engine -> Feature Store: Retrieves real-time fraud features [Redis Protocol]
- Audit Log Storage -> AWS S3 / Athena: Stores tamper-evident audit records [AWS SDK / HTTPS]

## Technology Stack
- AWS API Gateway & ALB: Managed edge routing, rate limiting, and TLS termination
- AWS ECS Fargate: Serverless container orchestration for low-overhead service management
- Go: High-performance backend execution for ultra-low latency real-time scoring
- Amazon ElastiCache Redis: In-memory data store for real-time feature retrieval
- Amazon S3 & Athena: Secure, durable audit log storage and query capabilities

## Rationale
The architecture combines managed AWS edge services with containerized Go microservices to meet strict sub-50ms latency and PCI-DSS compliance requirements. This lean design minimizes operational toil, enabling a three-engineer team to operate the platform reliably within a 25,000 EUR monthly budget.