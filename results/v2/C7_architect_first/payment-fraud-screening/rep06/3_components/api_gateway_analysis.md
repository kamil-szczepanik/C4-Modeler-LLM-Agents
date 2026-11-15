## Overview
[The system is a real-time payment fraud screening platform that evaluates payment authorizations and manages fraud analyst reviews. Its core purpose is to prevent fraudulent transactions while maintaining strict latency and compliance standards.]

## Key Elements
- Payment Gateway / Acquirer Systems
- AWS API Gateway + AWS WAF
- Edge Tokenizer & Sanitizer (AWS Lambda)
- Fraud Scoring Engine (ECS Fargate / gRPC)
- AWS CloudWatch & OpenTelemetry
- Amazon S3 with Object Lock

## Relationships
- Payment Gateway -> AWS API Gateway + AWS WAF: Submits encrypted payment payloads [HTTPS/mTLS]
- AWS API Gateway + AWS WAF -> Edge Tokenizer & Sanitizer: Invokes synchronous payload validation [Internal AWS Runtime]
- Edge Tokenizer & Sanitizer -> Fraud Scoring Engine: Forwards sanitized payloads [gRPC]
- AWS API Gateway + AWS WAF -> Amazon S3 with Object Lock: Ships execution logs [HTTPS]

## Technology Stack
- AWS API Gateway & AWS WAF: Edge routing, TLS 1.3 termination, rate limiting, and DDoS protection within budget.
- AWS Lambda: Edge tokenization and PAN data sanitization to enforce PCI-DSS compliance.
- gRPC: Low-latency internal communication protocol supporting sub-50ms P99 requirements.
- Amazon S3 with Object Lock: Provides tamper-evident 7-year audit log retention.

## Rationale
[This architecture leverages managed AWS services to minimize operational toil for a three-engineer team while satisfying strict PCI-DSS Level 1 constraints and a €25k monthly budget. Decoupling edge tokenization and utilizing gRPC ensures sub-50ms P99 latency and high availability.]