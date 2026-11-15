## Overview
[The system is a Real-Time Payment Fraud Screening API Gateway designed to screen card-not-present payment authorizations and protect mid-size payment processing revenue. Its core purpose is to validate incoming payment requests, strip sensitive card data, and enforce strict performance and security constraints.]

## Key Elements
- Payment Gateway / Acquirer
- AWS API Gateway (REST)
- Token Masking Engine (Rust Native Plugin / Edge Middleware)
- AWS Network Load Balancer (NLB)
- Fraud Scoring Engine (Amazon ECS on EC2)

## Relationships
- Payment Gateway / Acquirer -> AWS API Gateway (REST): Sends payment authorization requests [HTTPS, TLS 1.3]
- AWS API Gateway (REST) -> Token Masking Engine: Invokes in-memory request sanitization [Synchronous Edge Execution]
- Token Masking Engine -> AWS Network Load Balancer (NLB): Forwards sanitized payloads [mTLS, AWS Certificate Manager Private CA]
- AWS Network Load Balancer (NLB) -> Fraud Scoring Engine: Routes traffic to ECS tasks [mTLS, TCP]

## Technology Stack
- AWS API Gateway (REST): Manages ingress routing, rate limiting, and JWT validation within cost limits
- Rust Native Plugin: Executes zero-cold-start, in-memory token masking to meet <50ms P99 latency at 3,000 RPS
- TLS 1.3 / mTLS: Enforces strict cryptographic transport security and PCI-DSS compliance boundaries
- AWS CloudWatch & X-Ray: Provides distributed tracing and latency monitoring for operational guardrails

## Rationale
[This architecture satisfies strict PCI-DSS Level 1 and performance requirements by delegating data sanitization to a fast Rust edge plugin while keeping the infrastructure footprint manageable for a three-engineer team. By avoiding stateful edge logic, it ensures high availability and cost efficiency within the 25,000 EUR monthly budget.]