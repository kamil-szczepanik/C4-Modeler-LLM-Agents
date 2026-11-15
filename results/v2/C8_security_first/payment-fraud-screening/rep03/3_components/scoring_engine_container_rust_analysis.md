## Overview
This system provides real-time fraud screening for card-not-present payment authorizations to ensure PCI-DSS compliance while maintaining ultra-low latency. It evaluates transactions against scoring models, manages suspicious cases for analysts, and supports secure zero-downtime updates.

## Key Elements
- AWS Application Load Balancer (ALB) / Ingress Router
- Scoring Engine Container (Rust) (API Router, Feature Aggregator, Scoring Engine Core, Model Manager, Audit Dispatcher)
- Audit Logger Sidecar Container
- Amazon ElastiCache (Redis)
- Amazon Aurora Serverless v2
- Amazon S3 with Object Lock

## Relationships
- AWS Application Load Balancer (ALB) -> Scoring Engine Container (Rust): Routes real-time scoring requests via [gRPC / HTTP/REST with mTLS]
- Scoring Engine Container (Rust) -> Amazon ElastiCache (Redis): Performs feature store lookups via [gRPC / TCP with TLS 1.3]
- Scoring Engine Container (Rust) -> Audit Logger Sidecar Container: Sends audit logs via [Unix Domain Sockets (UDS)]
- Scoring Engine Container (Rust) -> Model Registry: Fetches cryptographically verified model updates via [HTTPS]

## Technology Stack
- Rust, Axum, Tokio: Selected for ultra-low latency execution and memory safety in the scoring engine.
- Amazon ElastiCache (Redis): Provides high-throughput, sub-millisecond feature store lookups.
- Amazon S3 with Object Lock: Ensures tamper-evident, 7-year regulatory audit log retention.
- OpenTelemetry & Prometheus: Delivers distributed tracing and tail-latency observability.
- AWS Fargate: Runs containerized workloads efficiently within the 25k EUR monthly budget.

## Rationale
The architecture combines a high-performance Rust core with low-latency Redis lookups to achieve sub-50ms P99 latency at 3,000 TPS. Strict memory hardening, cryptographic model verification, and Unix Domain Sockets ensure PCI-DSS Level 1 compliance and auditable security for a small engineering team.