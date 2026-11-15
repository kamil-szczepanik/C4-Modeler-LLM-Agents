## Overview
Real-Time Payment Fraud Screening screens card-not-present payment authorizations for a mid-size payment processor and enables fraud analysts to review suspicious transactions. It ensures sub-50ms P99 latency and full PCI-DSS Level 1 compliance under a fixed budget of 25,000 EUR per month.

## Key Elements
- API Gateway (Envoy)
- Real-Time Scoring Engine (Go, ONNX Runtime, AWS ECS Fargate)
- Scoring Orchestrator
- Feature Assembler
- Inference Executor
- Model Hot-Loader
- Rule Evaluator
- Audit Telemetry Emitter
- Redis (AWS ElastiCache)
- Amazon SQS
- AWS Aurora PostgreSQL

## Relationships
- API Gateway -> Scoring Orchestrator: Forwards scoring requests [gRPC over HTTP/2 with mTLS]
- Scoring Orchestrator -> Feature Assembler: Coordinates feature fetch [In-memory Go function call]
- Feature Assembler -> Redis (AWS ElastiCache): Retrieves features [TCP/RESP]
- Scoring Orchestrator -> Inference Executor: Executes model [In-memory CGO/ONNX]
- Scoring Orchestrator -> Rule Evaluator: Evaluates overrides [In-memory]
- Scoring Orchestrator -> Audit Telemetry Emitter: Enqueues audit log [Local channel / ring buffer]
- Audit Telemetry Emitter -> Amazon SQS: Publishes audit events [AWS SDK / SQS API]

## Technology Stack
- Go: Chosen for high concurrency and performance to achieve sub-50ms P99 latency.
- ONNX Runtime: Enables fast, in-memory machine learning model evaluation.
- AWS ECS Fargate: Provides managed container orchestration within budget constraints.
- AWS ElastiCache Redis: Delivers low-latency feature storage.
- Amazon SQS: Asynchronously buffers audit and telemetry events.

## Rationale
This architecture balances strict sub-50ms P99 performance requirements with robust 7-year auditability and PCI-DSS Level 1 compliance. Using stateless Go containers on AWS ECS Fargate ensures high availability and cost control for a three-engineer team.