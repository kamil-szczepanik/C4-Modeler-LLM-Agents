## Overview
The Real-Time Scoring Engine Container screens payment authorizations for fraud within strict latency SLAs while maintaining PCI-DSS compliance. It evaluates transactions concurrently and publishes decisions asynchronously within budget and operational constraints.

## Key Elements
- Real-Time Scoring Engine Container (AWS ECS with Fargate)
- Model & Rule Registry Service Container
- Amazon ElastiCache (Redis)
- Amazon SQS / SNS
- AWS CloudWatch

## Relationships
- Tokenization/Masking Proxy Container -> Real-Time Scoring Engine Container: Forwards scrubbed transaction data [gRPC / Protocol Buffers]
- Real-Time Scoring Engine Container -> Amazon ElastiCache (Redis): Queries local cache for fast transaction evaluation [Redis Protocol]
- Real-Time Scoring Engine Container -> Amazon SQS / SNS: Publishes scoring decisions asynchronously [AWS SDK]
- Model & Rule Registry Service Container -> Real-Time Scoring Engine Container: Supplies immutable scoring models and rules [gRPC]

## Technology Stack
- Rust or Go: Selected for predictable, low-latency garbage collection and high CPU core utilization via event-loop execution.
- gRPC with Protocol Buffers: Chosen for zero-copy binary serialization and strict schema validation.
- Amazon ECS with Fargate: Enables stateless scale-out within the 25,000 EUR monthly infrastructure budget.
- OpenTelemetry: Provides low-overhead distributed tracing for latency bottleneck isolation.
- AWS CloudWatch: Monitors real-time saturation metrics and container health for autoscaling.

## Rationale
This architecture uses stateless compute containers and in-memory caching to achieve sub-50ms P99 latency at 3,000 TPS. It ensures operational simplicity, strict determinism, and robust auditability suitable for a three-person engineering team.