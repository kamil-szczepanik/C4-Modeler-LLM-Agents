## Overview
The Scoring Engine is a real-time payment fraud screening container that evaluates card-not-present transactions for a mid-size payment processor. It provides sub-50ms P99 latency decisions (approve, decline, review) while maintaining strict PCI-DSS Level 1 compliance and a 7-year auditability mandate.

## Key Elements
- Scoring Engine Container (Go, AWS ECS Fargate)
- Request Handler Component (Go, gRPC)
- Model Evaluator Component (ONNX Runtime, Dual-Buffer Registry)
- Feature Aggregator Component (Concurrent Redis Pipeline)
- Audit Dispatcher Component (Amazon SQS, AWS SDK)
- Redis Cluster (Feature Store)
- Amazon SQS & S3 (Audit Queue and Storage)

## Relationships
- API Gateway / Network Load Balancer (NLB) -> Scoring Engine: Route payment evaluation requests [gRPC over HTTP/2, mTLS]
- Scoring Engine -> Redis Cluster: Perform in-memory feature lookups [TCP, TLS 1.3]
- Scoring Engine -> Amazon SQS: Emit asynchronous, KMS-signed audit events [AWS SDK, HTTPS]
- Scoring Engine -> Amazon S3: Persist tamper-evident audit logs [Amazon Kinesis Firehose]

## Technology Stack
- Go: Chosen for high-throughput concurrency and minimal garbage collection overhead to satisfy sub-50ms P99 latency.
- AWS ECS Fargate: Container orchestration matching the 25,000 EUR monthly budget without idle server management.
- Redis Cluster: In-memory cache providing sub-15ms feature aggregation and velocity checks.
- ONNX Runtime: Embedded machine learning execution engine enabling zero-downtime model hot-swapping via atomic pointer swaps.
- Amazon SQS & S3 with S3 Object Lock: Guarantees tamper-evident, 7-year regulatory audit retention.

## Rationale
This architecture balances ultra-low latency processing at 3,000 TPS with strict PCI-DSS Level 1 security and tamper-evident auditability. Decoupling real-time scoring from asynchronous auditing ensures the system meets its availability and performance constraints within the fixed infrastructure budget.