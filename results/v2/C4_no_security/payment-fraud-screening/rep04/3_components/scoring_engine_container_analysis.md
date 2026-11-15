## Overview
The Real-Time Payment Fraud Screening system screens card-not-present payment authorizations for fraud prior to approval and provides a case management interface for fraud analysts. The system ensures PCI-DSS Level 1 compliance while maintaining sub-50ms P99 latency at 3,000 transactions per second.

## Key Elements
- API Handler Component: Go/Fiber or Rust/Axon managing inbound gRPC/REST requests.
- Feature Assembler Component: Concurrently fetches contextual velocity data.
- Inference Engine Component: Evaluates transactions using compiled decision trees or ONNX-runtime ML models.
- Audit Dispatcher Component: Asynchronously flushes immutable decision logs using a local ring-buffer durability pattern.
- Feedback Loop Receiver Component: Ingests analyst review outcomes from the Case Management container.
- Sidecar Model Deployment Pipeline: S3-backed model fetcher utilizing local shared volumes for atomic hot-reloading.

## Relationships
- API Gateway -> API Handler Component: Invokes real-time fraud scoring [gRPC/REST].
- API Handler Component -> Feature Assembler Component: Passes validated request payloads [In-memory Go Channels].
- Feature Assembler Component -> Amazon ElastiCache (Redis): Fetches cached velocity data [TCP/Redis Protocol].
- Feature Assembler Component -> Inference Engine Component: Passes assembled feature vectors [In-memory].
- Sidecar S3 Volume -> Inference Engine Component: Provides atomic model file updates [Local Shared Volume].
- Inference Engine Component -> Audit Dispatcher Component: Emits decisions and explanation payloads [In-memory Channel].
- Audit Dispatcher Component -> Amazon DynamoDB & AWS SQS: Flushes tamper-evident audit logs [AWS SDK / HTTPS].
- Case Management Container -> Feedback Loop Receiver Component: Sends analyst review outcomes [gRPC/REST].

## Technology Stack
- Go or Rust: Selected for core container implementation to guarantee sub-50ms P99 latency and high throughput.
- Amazon ECS: Container orchestration platform matching the 3-engineer team operational capacity and budget.
- Amazon ElastiCache (Redis) & Amazon DynamoDB: Low-latency data layer for velocity caching and transactional storage.
- AWS S3 & Sidecar Volumes: Enables zero-downtime model updates via atomic file-system watches.

## Rationale
This architecture achieves sub-50ms P99 latency at 3,000 TPS by utilizing in-memory Go channels, local model execution, and asynchronous audit dispatching. It satisfies strict compliance, explainability, and 7-year auditability mandates while remaining operable by a 3-engineer team within the 25,000 EUR monthly budget.