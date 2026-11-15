## Overview
- High-performance Go scoring engine for real-time payment fraud screening.
- Processes payment authorizations to return approve, decline, or review decisions under strict latency constraints.

## Key Elements
- HTTP/gRPC Ingress Handler
- Feature Extractor Component
- Scoring & Evaluation Core
- Rule Engine Hot-Reloader Component
- Audit Signer Component
- Memory Sanitizer Middleware

## Relationships
- AWS API Gateway & NLB -> HTTP/gRPC Ingress Handler [gRPC over mTLS]
- Feature Extractor Component -> Amazon ElastiCache (Redis OSS) [TCP]
- Audit Signer Component -> AWS KMS [AWS SDK]
- Go Scoring Engine -> Amazon SQS / EventBridge [AWS SDK]

## Technology Stack
- Go (Golang): Chosen for low latency and high concurrency to meet <50ms P99 at 3,000 RPS.
- AWS ECS on Fargate: Chosen to maintain persistent cryptographic signing contexts.
- Amazon ElastiCache (Redis OSS): Shared feature state caching to prevent DB drift.
- AWS KMS: Cryptographic signing for 7-year tamper-evident auditability.

## Rationale
- This architecture guarantees sub-50ms decision latencies while strictly enforcing PCI-DSS Level 1 compliance and a 1-minute fail-open availability SLA.
- It operates within a 25,000 EUR monthly budget and can be managed by a three-engineer team.