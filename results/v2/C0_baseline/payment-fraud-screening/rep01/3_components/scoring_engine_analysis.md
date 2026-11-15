## Overview
The Scoring Engine evaluates card-not-present payment authorizations for fraud in real-time while ensuring strict PCI-DSS Level 1 compliance and 7-year auditability. It processes requests with sub-50ms P99 latency within a 25,000 EUR monthly AWS budget constraint.

## Key Elements
- **API Handler**: Go-based component using gRPC for inbound validation, correlation ID injection, and PAN data stripping.
- **Rule Evaluator**: Component for executing in-memory deterministic fraud rules via bytecodes.
- **Model Runner**: Component for evaluating lightweight probabilistic models using ONNX Runtime in Go with cryptographically signed artifact verification via AWS KMS.
- **Audit Logger**: Component that asynchronously batches and sends tamper-evident JSON audit payloads via internal Go channels.
- **Infrastructure Services**: AWS ECS Fargate on Graviton2 (ARM64), Amazon SQS, AWS Firehose, and Amazon S3 with Object Lock.

## Relationships
- **API Gateway -> API Handler**: Communicates scoring requests securely using gRPC with mTLS.
- **Model Runner -> AWS KMS**: Verifies cryptographic signatures of model artifacts retrieved from S3 prior to execution.
- **Audit Logger -> AWS SQS**: Asynchronously dispatches audit payloads using the AWS SDK for Go.
- **AWS SQS -> AWS Firehose -> Amazon S3**: Transports and archives immutable audit logs with S3 Object Lock compliance mode.

## Technology Stack
- **Go**: Chosen for high-throughput, low-latency execution and optimal price-performance on ARM64.
- **AWS ECS Fargate on Graviton2 (ARM64)**: Provides scalable, cost-effective container orchestration without Lambda provisioning limits.
- **ONNX Runtime**: Enables fast in-memory probabilistic machine learning evaluations.
- **AWS KMS & S3 Object Lock**: Ensures cryptographic model verification and tamper-evident 7-year audit data retention.

## Rationale
This architecture uses ECS Fargate on Graviton2 and Go to consistently achieve sub-50ms P99 latency at 3,000 TPS within the strict 25,000 EUR budget. Cryptographic verification, strict PAN sanitization, and immutable S3 Object Lock ensure full compliance with PCI-DSS Level 1 and 7-year auditability constraints.