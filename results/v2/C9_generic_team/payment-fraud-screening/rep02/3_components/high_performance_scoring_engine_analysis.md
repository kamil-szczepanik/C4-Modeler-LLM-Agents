## Overview
The High-Performance Scoring Engine screens real-time card-not-present payment authorizations for fraud within strict latency and compliance constraints. It evaluates transactions using hot-reloadable models while maintaining high availability and auditability.

## Key Elements
- High-Performance Scoring Engine (AWS ECS on Fargate container using Clean Architecture / Ports and Adapters)
- Feature Store (Redis with local in-memory LRU cache)
- API Gateway / Ingestion Container (Envoy proxy / AWS API Gateway)
- Async Event Bus (AWS SQS / EventBridge)
- Model & Rule Registry Container
- Audit & Compliance Storage (AWS S3 with Object Lock and Parquet format)

## Relationships
- API Gateway -> High-Performance Scoring Engine: Routes authorization requests [gRPC over internal VPC]
- High-Performance Scoring Engine -> Feature Store: Fetches transaction features [Redis Protocol with strict 15ms timeout budget]
- High-Performance Scoring Engine -> Async Event Bus: Publishes transaction decisions and audit events [AWS SDK / JSON over SQS]
- High-Performance Scoring Engine -> Audit & Compliance Storage: Persists immutable input snapshots and model versions [AWS SDK / HTTPS]

## Technology Stack
- AWS ECS on Fargate: Provides scalable, containerized execution with predictable resource bounds and cost control within the 25,000 EUR budget.
- gRPC & Protocol Buffers: Ensures low-latency communication (<50ms P99) and strict schema validation between services.
- Redis & Local LRU Cache: Delivers sub-millisecond feature retrieval while protecting against downstream latency spikes.
- OpenTelemetry: Enables distributed tracing and high-priority metrics for rapid MTTR by a three-person engineering team.
- AWS S3 with Object Lock: Guarantees tamper-evident, 7-year retention for regulatory compliance (R-06).

## Rationale
This architecture uses containerized microservices with strict timeout budgeting, fail-fast startup gates, and fallback mechanisms to meet sub-50ms latency and 99.99% availability constraints. Clean architecture principles and automated contract testing ensure maintainability and zero-downtime deployments for a lean three-person engineering team within a fixed budget.