## Overview
[The Go Fraud Scoring Engine screens card-not-present payment authorizations in real-time to detect fraud before approval and provides audit trails for analysts. It is built to meet strict PCI-DSS compliance and high-performance requirements within budget constraints.]

## Key Elements
* API Handler Component (Go / gRPC)
* Rule Engine Component (Go / Embedded DSL)
* Velocity Counter Component (Go / Redis Client)
* Model Scorer Component (Go / ONNX Runtime C bindings)
* Audit Logger Component (Go / Async Batch Writer)
* Config & Model Synchronizer Component (Go / S3 Sync)
* Circuit Breaker Wrapper (Go / Memory)
* Amazon ElastiCache (Redis)
* Amazon Aurora Serverless v2
* Amazon S3

## Relationships
* API Handler -> Rule Engine & Model Scorer: In-process function calls via Go channels/memory
* Velocity Counter -> Amazon ElastiCache (Redis): Evaluates sliding-window rate limits via TCP
* Audit Logger -> Amazon Aurora Serverless v2: Persists audit data and transaction records via TLS
* Config & Model Synchronizer -> Amazon S3: Fetches rules and ONNX models via HTTPS with AWS SigV4

## Technology Stack
* Go / gRPC: Selected for high-throughput, low-latency execution matching P99 performance targets
* ONNX Runtime C bindings: Executes pre-compiled machine learning models efficiently in-memory
* Amazon ECS Fargate: Provides serverless container orchestration within operational constraints
* Amazon ElastiCache (Redis): Enables real-time velocity checks and sliding-window rate limits
* AWS KMS: Ensures tamper-evident audit logging through cryptographic envelope signatures

## Rationale
[This architecture leverages in-memory execution and asynchronous batching to consistently achieve sub-50ms P99 latencies under heavy throughput. It strictly isolates sensitive payment data and enforces tamper-evident auditing to satisfy PCI-DSS Level 1 compliance.]