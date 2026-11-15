## Overview
The Fraud Scoring Engine evaluates real-time card-not-present payment authorizations to detect fraud within strict performance and compliance constraints. It processes high-throughput transactions with low latency while maintaining immutable audit trails and zero-downtime model updates.

## Key Elements
- **API Controller**: Spring WebFlux service managing HTTP/2 ingress and timeouts.
- **Feature Aggregator**: Jedis client querying Amazon ElastiCache Redis and Amazon DynamoDB for real-time velocity metrics.
- **Inference Executor**: Microsoft ONNX Runtime executing embedded LightGBM models.
- **Decision Explainer**: Native Java component generating SHAP-lite feature attributions synchronously.
- **Audit Logger**: Spring Events and Amazon SQS publisher emitting immutable decision records.
- **Model & Rule Hot-Reloader**: Custom file watcher polling Amazon S3 for dynamic in-memory model swapping.
- **Circuit Breaker & Fallback Manager**: Resilience4j handler enforcing sub-millisecond degradation policies.

## Relationships
- **AWS ALB -> API Controller**: Receives authorization requests via HTTP/2 over TLS.
- **API Controller -> Circuit Breaker & Fallback Manager**: Wraps scoring invocation in-memory.
- **Circuit Breaker & Fallback Manager -> Feature Aggregator**: Fetches user and card velocity features via TCP/Redis.
- **Feature Aggregator & API Controller -> Inference Executor**: Passes assembled feature vectors via in-memory execution.
- **Model & Rule Hot-Reloader -> Amazon S3**: Polls for model binaries and rule artifacts via HTTPS.
- **Inference Executor -> Decision Explainer**: Forwards raw scores and feature contributions in-memory.
- **Decision Explainer -> Audit Logger**: Submits enriched decision records asynchronously via Spring Events.
- **Audit Logger -> Amazon SQS**: Publishes audit payloads via HTTPS.

## Technology Stack
- **AWS ECS Fargate**: Serverless container runtime optimized for a three-engineer team budget.
- **Java / Spring WebFlux**: Reactive runtime chosen for non-blocking I/O and low P99 latency.
- **Microsoft ONNX Runtime**: Embedded inference engine providing sub-millisecond model evaluation.
- **Amazon ElastiCache Redis & DynamoDB**: Low-latency data stores for velocity counters and profiles.
- **Resilience4j**: Lightweight fault tolerance library ensuring graceful degradation within 1 minute.
- **Amazon S3**: Object storage utilized for tamper-evident audit logs via Object Lock and model version hosting.

## Rationale
This architecture achieves sub-50ms P99 latency at scale by utilizing reactive Java and embedded in-memory ONNX inference without network hops. It ensures strict compliance and availability through asynchronous immutable auditing, hot-reloadable models, and robust circuit breakers operating within a cost-effective AWS serverless footprint.