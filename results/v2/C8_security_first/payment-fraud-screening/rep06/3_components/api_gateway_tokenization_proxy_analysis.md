## Overview
[The system is a Real-Time Payment Fraud Screening engine deployed on AWS eu-west-1, designed to score card-not-present payment authorizations and manage fraud reviews.]
[Its core purpose is to deliver sub-50ms fraud decisions while ensuring PCI-DSS Level 1 compliance and 7-year tamper-evident auditability within a strict budget.]

## Key Elements
- API Gateway / Tokenization Proxy (Envoy Proxy on AWS ECS on Fargate)
- Edge Router Component (Envoy)
- Tokenization Filter Component (Native Envoy C++/Lua configuration with Format-Preserving Encryption)
- Payload Sanitizer Component
- Real-Time Scoring Engine (Go on AWS ECS on Fargate with Redis)
- Case Management API (Node.js / Java Spring Boot)
- Audit Log Sitter (Rust)
- Rule & Model Distribution Service (Python / FastAPI + S3)
- Event Broker (AWS MSK / Managed Kafka or AWS SQS)
- AWS Network Load Balancer (NLB)

## Relationships
- Merchant / Payment Gateway -> AWS Network Load Balancer: Sends payment authorizations [HTTPS (TLS 1.3)]
- AWS Network Load Balancer -> API Gateway / Tokenization Proxy: Forwards traffic [TCP]
- API Gateway / Tokenization Proxy -> Real-Time Scoring Engine: Routes requests for scoring [gRPC over AWS VPC private subnets with mTLS]
- Real-Time Scoring Engine -> Event Broker: Publishes scoring results and telemetry [Kafka/SQS]
- Audit Log Sitter -> AWS QLDB / S3 Object Lock: Writes tamper-evident logs [HTTPS]

## Technology Stack
- AWS eu-west-1: Target cloud region for compliance and infrastructure constraints.
- Envoy Proxy / AWS ECS on Fargate: Powers the edge gateway with auto-scaling to handle 3,000 TPS under a 3-engineer team.
- Format-Preserving Encryption (FPE): Enables low-latency stateless PAN tokenization without expensive HSM round-trips.
- gRPC with mTLS: Ensures secure, high-performance internal service-to-service communication.
- AWS X-Ray and JSON structured logging: Provides distributed tracing and observability.

## Rationale
[This architecture achieves P99 latency under 50ms at 3,000 TPS through localized tokenization, native Envoy filters, and stateless Fargate auto-scaling. It satisfies strict PCI-DSS Level 1 compliance, auditability, and a 1-minute fail-open availability requirement within the €25,000 monthly budget and 3-engineer operational limits.]