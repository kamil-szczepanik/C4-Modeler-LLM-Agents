## Overview
The API Gateway / Ingestion Container serves as the secure edge proxy for the Real-Time Payment Fraud Screening system, handling external ingress, request validation, and routing. It screens payment authorizations in real time while enforcing strict PCI-DSS compliance and latency constraints.

## Key Elements
- API Gateway / Ingestion Container: AWS API Gateway and Envoy proxy
- High-Performance Scoring Engine: Internal downstream service
- Feature Store / Cache: Redis for idempotency and token caching
- External Systems: Payment Gateway / Acquirer

## Relationships
- Payment Gateway / Acquirer -> API Gateway / Ingestion Container: Sends payment authorization requests [HTTPS/TLS 1.3]
- API Gateway / Ingestion Container -> High-Performance Scoring Engine: Routes validated payloads [Internal VPC gRPC using Protocol Buffers]
- API Gateway / Ingestion Container -> Redis: Performs deduplication and idempotency checks [Internal TCP]

## Technology Stack
- AWS API Gateway & Envoy proxy: Provides edge routing, circuit breaking, and low-latency gRPC connection pooling
- Protocol Buffers: Minimizes serialization overhead to meet the 50 ms P99 latency target
- W3C Trace Context & AWS X-Ray: Enables distributed tracing for 7-year auditability
- Redis (Native Envoy Integration): Handles sliding-window idempotency checks and request deduplication
- GitOps & OPA/Rego: Automates configuration management and policy enforcement for a 3-engineer team

## Rationale
This architecture uses Envoy proxy and Protocol Buffers to achieve sub-50ms latency at 3,000 RPS within a strict budget. Edge-level security controls, strict payload validation, and GitOps automation ensure PCI-DSS Level 1 compliance while remaining maintainable for a three-engineer team.