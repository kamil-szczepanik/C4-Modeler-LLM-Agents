## Overview
[Real-Time Payment Fraud Screening Container evaluates card-not-present payment authorizations to detect fraud with sub-50ms latency. It provides zero-downtime model updates and tamper-evident audit logging for financial compliance.]

## Key Elements
- API Gateway / Ingress Container
- Real-Time Scoring Container
- AWS SQS / Kinesis
- Amazon S3
- AWS Secrets Manager / Parameter Store

## Relationships
- API Gateway / Ingress Container -> Real-Time Scoring Container: Evaluates payment authorizations synchronously [gRPC / REST]
- Real-Time Scoring Container -> AWS SQS / Kinesis: Dispatches decision events asynchronously [AWS SDK]
- Real-Time Scoring Container -> Amazon S3: Hot-reloads machine learning models [HTTPS]

## Technology Stack
- Blue-green model swapping pattern: Achieves zero-downtime model updates via atomic pointer swaps in memory
- Circuit breaker and graceful fallback mechanism: Ensures high availability by failing open during downstream outages
- Stateless, share-nothing architecture: Simplifies horizontal autoscaling and failure recovery
- Prometheus-compatible histograms: Provides lightweight local metrics scraping for low infrastructure overhead

## Rationale
[This architecture uses memory-resident models and stateless container design to meet strict sub-50ms latency and high availability SLAs. The lightweight telemetry and shared-nothing approach keep operations manageable for a three-engineer team within the fixed budget.]