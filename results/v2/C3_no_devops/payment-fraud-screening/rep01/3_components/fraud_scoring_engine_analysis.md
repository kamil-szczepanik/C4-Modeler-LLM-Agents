## Overview
The Fraud Scoring Engine is a high-performance Go microservice that screens card-not-present payment authorizations for fraud within 50ms P99 latency while ensuring PCI-DSS Level 1 compliance and 7-year auditability. It evaluates transactions in real time, generates explainable risk scores, and gracefully handles outages to protect merchant revenue.

## Key Elements
- API Router & Fallback Handler (Go `net/http`)
- Feature Aggregator (Go concurrent routines)
- Scoring Evaluator with Feature Contribution Formatter (Go in-memory engine)
- Audit Publisher (Go SDK with HMAC-SHA256)
- External Systems: AWS API Gateway / NLB, AWS ElastiCache for Redis (Feature Store), Amazon SQS (Message Queue), AWS KMS

## Relationships
- AWS API Gateway / NLB -> API Router & Fallback Handler: Invokes scoring evaluation [mTLS / gRPC or HTTP/2]
- API Router & Fallback Handler -> Feature Aggregator: Concurrently fetches features [Go channels / In-memory function calls]
- Feature Aggregator -> AWS ElastiCache for Redis: Queries real-time features [Low-latency TCP / Redis Protocol]
- Scoring Evaluator -> Audit Publisher: Dispatches decision metadata and risk drivers [Buffered Go channel]
- Audit Publisher -> Amazon SQS: Publishes signed decision payloads [AWS SDK for Go over HTTPS]

## Technology Stack
- Go (Golang): Chosen for zero-garbage-collection predictability and ability to meet <50ms P99 latency at 3,000 TPS under a constrained memory footprint.
- AWS ElastiCache for Redis: Provides low-latency TCP data access for real-time feature aggregation.
- Amazon SQS with AWS KMS: Secures and buffers asynchronous audit logs with envelope encryption and tamper-evident signing.
- mTLS & TLS 1.3: Enforces strict transport security across all internal and external container boundaries.

## Rationale
This architecture uses Go's concurrency model and in-memory evaluation to meet stringent performance requirements without exceeding the 25,000 EUR monthly infrastructure budget. Layered security controls, tokenization boundaries, and explicit memory sanitization achieve PCI-DSS Level 1 compliance and tamper-evident 7-year auditability.