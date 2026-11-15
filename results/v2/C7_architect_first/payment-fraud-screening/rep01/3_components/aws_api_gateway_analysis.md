## Overview
[The AWS API Gateway component ingests and securely routes real-time payment authorization traffic for fraud screening while enforcing strict perimeter security and compliance. It acts as the high-performance entry point for incoming card-not-present payment requests before they reach scoring engines.]

## Key Elements
- HTTP API Route Resolver (Amazon API Gateway): Terminates TLS 1.3 and enforces native JSON schema validation.
- Edge Rate Limiter & WAF (AWS WAF): Mitigates DDoS attacks and enforces rate limits.
- Upstream Integration: Payment Gateway / Acquirer Systems sending authorization requests.
- Downstream Integration: Real-Time Scoring Engine hosted on AWS ECS Fargate.

## Relationships
- Payment Gateway / Acquirer Systems -> HTTP API Route Resolver: Sends payment authorization requests [HTTPS/REST]
- HTTP API Route Resolver -> Real-Time Scoring Engine: Routes validated authorization traffic [gRPC with mTLS via VPC Private Link]
- HTTP API Route Resolver -> AWS WAF: Inspects incoming payloads for malicious traffic [Internal AWS Integration]

## Technology Stack
- Amazon API Gateway (HTTP APIs): Selected for lower latency, zero compute overhead, and cost efficiency.
- AWS WAF: Provides managed core rule sets and custom rate-based rules for volumetric protection.
- Terraform / AWS CDK: Used for GitOps-based infrastructure deployment and configuration management.
- AWS Secrets Manager: Manages automated rotation of mTLS client certificates and secrets.

## Rationale
[This serverless edge architecture eliminates cold-start overhead to consistently meet the P99 latency target below 50 ms at 3,000 TPS. Furthermore, it strictly enforces PCI-DSS Level 1 compliance and data minimization while operating efficiently within the fixed monthly budget.]