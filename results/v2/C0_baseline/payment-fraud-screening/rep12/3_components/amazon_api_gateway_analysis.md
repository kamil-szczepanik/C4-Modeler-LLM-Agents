## Overview
The system screens card-not-present payment authorizations for fraud in real-time and provides case management for human analysts. It is operated by a three-engineer team on AWS under a 25,000 EUR monthly budget.

## Key Elements
- Amazon API Gateway HTTP API
- Real-Time Scoring Engine (Go microservice on AWS ECS EC2)
- Case Management System API (Node.js / Express on ECS)
- AWS WAFv2 WebACL
- Amazon CloudWatch
- AWS Secrets Manager

## Relationships
- Payment Processor -> Amazon API Gateway: Sends authorization requests [HTTPS / TLS 1.3 with mTLS]
- Fraud Analysts -> Amazon API Gateway: Accesses case management [HTTPS / JSON with OAuth 2.0 / OIDC JWT]
- Amazon API Gateway -> Real-Time Scoring Engine: Proxies payment transactions [Internal gRPC over mTLS via AWS PrivateLink / VPC Link]
- Amazon API Gateway -> Case Management System API: Routes analyst requests [HTTPS / JSON]
- Amazon API Gateway -> Amazon CloudWatch: Streams structured JSON access logs [AWS SDK]

## Technology Stack
- Amazon API Gateway HTTP APIs: Chosen for lower latency (<50ms P99) and 70% lower cost than REST APIs.
- AWS PrivateLink / VPC Link: Secures internal transit between API Gateway and ECS containers.
- AWS WAFv2: Provides edge rate-limiting and DDoS protection.
- AWS Secrets Manager: Secures JWT keys and mTLS trust store parameters.

## Rationale
This architecture uses serverless edge routing to minimize operational overhead for a three-engineer team while meeting strict <50ms P99 latency and PCI-DSS compliance constraints. It maintains high availability and strict auditability within a 25,000 EUR monthly AWS budget.