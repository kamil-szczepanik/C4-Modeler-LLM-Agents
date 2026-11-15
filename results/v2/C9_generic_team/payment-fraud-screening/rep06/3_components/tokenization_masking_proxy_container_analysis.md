## Overview
The Real-Time Payment Fraud Screening system evaluates card-not-present payment authorizations to prevent fraud and manage analyst reviews. It ensures PCI-DSS Level 1 compliance while maintaining sub-50ms P99 latency and strict 7-year auditability.

## Key Elements
- Tokenization/Masking Proxy Container (AWS ECS with Fargate)
- AWS KMS for envelope encryption and vault-backed tokenization
- Amazon ElastiCache (Redis) for local in-memory caching
- AWS Secrets Manager for secret injection
- AWS X-Ray for distributed tracing

## Relationships
- API Gateway / Payment Gateway Integration Container -> Tokenization/Masking Proxy Container: Forwards requests for PAN scrubbing [Internal API / TLS 1.3]
- Tokenization/Masking Proxy Container -> Real-Time Scoring Engine Container: Forwards scrubbed transaction data [Internal API / TLS 1.3]
- Tokenization/Masking Proxy Container -> AWS KMS: Performs vault-backed tokenization and envelope encryption [AWS API]

## Technology Stack
- AWS ECS with Fargate: Provides isolated, scalable container execution within budget
- AWS KMS: Offloads key rotation and ensures PCI-DSS compliance without custom cryptography
- Amazon ElastiCache (Redis): Minimizes latency via in-memory caching for recurring token lookups
- AWS Secrets Manager: Secures runtime configuration injection directly into task definitions

## Rationale
This architecture uses managed AWS services and stateless proxy processing to meet PCI-DSS Level 1 compliance and a 50ms P99 latency target. It remains operable by a three-engineer team within a €25,000 monthly budget.