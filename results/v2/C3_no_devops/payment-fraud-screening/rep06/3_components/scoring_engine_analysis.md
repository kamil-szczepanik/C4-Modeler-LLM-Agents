## Overview
- Real-time payment fraud screening system for card-not-present transactions, ensuring sub-50ms latency and PCI-DSS Level 1 compliance on AWS.
- Processes 3,000 authorizations per second while maintaining immutable, 7-year tamper-evident audit logs.

## Key Elements
- Scoring API Controller (`Go / net/http`): Handles ingress gRPC/HTTP2, token stripping, and circuit breaking.
- Feature Aggregator Component: Concurrently fetches real-time features from Amazon ElastiCache Redis.
- Evaluation Engine Component: Evaluates rules and ML models in-memory using atomic pointer swaps.
- Audit Dispatcher Component: Signs decision payloads via AWS KMS and publishes to Amazon EventBridge.
- Rule Synchronizer Sub-Component: Cryptographically verifies and hot-reloads models from the Rule & Model Distribution Service.

## Relationships
- API Gateway / Ingress Router -> Scoring API Controller: Enforces mTLS within private subnets via gRPC/HTTP2 over TLS 1.3.
- Feature Aggregator -> Amazon ElastiCache Redis: Fetches low-latency features using RESP protocol over private VPC with TLS and IAM auth.
- Audit Dispatcher -> Amazon EventBridge: Streams cryptographically signed audit payloads asynchronously using HTTPS via AWS SDK with SigV4.
- Rule Synchronizer -> Rule & Model Distribution Service: Ingests signed scoring rules and models in the background.

## Technology Stack
- Go (`net/http`): Chosen for low memory footprint, zero GC pauses, and high throughput to maintain <50ms P99 latency.
- Amazon ElastiCache Redis: In-memory store for sub-millisecond feature retrieval under high transaction volume.
- Amazon EventBridge: Serverless event bus for decoupled, reliable asynchronous audit event streaming.
- AWS KMS: Provides envelope encryption for cryptographic signing of tamper-evident audit payloads (R-06).
- ECS Fargate: Serverless container compute minimizing operational overhead for a 3-engineer team.

## Rationale
- The stateless Go-based architecture with in-memory evaluation guarantees the strict P99 latency constraint of 50ms at 3,000 TPS.
- Cryptographic signing via AWS KMS and atomic pointer hot-reloading satisfy PCI-DSS compliance, 7-year auditability, and zero-downtime model updates.