## Overview
The Real-Time Payment Fraud Screening system evaluates card-not-present payment authorizations for fraud under strict latency constraints before approval. It simultaneously provides case management for fraud analysts to review suspicious transactions safely and efficiently.

## Key Elements
- Ingress Coordinator (Rust `tonic`/`axum`)
- Feature Assembler (`redis-rs`, Amazon ElastiCache Redis, Amazon DynamoDB)
- Model Executor (Wasmtime sandbox, WebAssembly scoring models)
- Audit Dispatcher (`aws-sdk-rust`, Amazon Kinesis Data Streams, Amazon Kinesis Firehose)
- Model Registry Client (AWS KMS, Amazon S3)
- Container Infrastructure (Amazon ECS Fargate, AWS API Gateway, Internal ALB)

## Relationships
- AWS API Gateway -> Scoring Engine: Routes screening requests [Internal ALB / gRPC]
- Scoring Engine -> Feature Store & Cache: Performs low-latency feature lookups [TCP/TLS with mTLS]
- Model Registry Client -> Model Storage: Fetches signed Wasm binaries [HTTPS / TLS 1.3]
- Audit Dispatcher -> Audit & Streaming Pipeline: Emits decision payloads [AWS SDK / HTTP/2]

## Technology Stack
- Rust (Tokio): Chosen for memory safety and zero garbage collection pauses to guarantee sub-50ms P99 latency.
- Amazon ECS Fargate: Provides a managed container runtime within the fixed 25,000 EUR monthly infrastructure budget.
- WebAssembly (Wasm) via Wasmtime: Enables isolated, secure model execution and zero-downtime hot-reloading via atomic pointers (`ArcSwap`).
- Amazon ElastiCache Redis & DynamoDB: Deliver high-throughput, low-latency feature retrieval.
- Amazon S3 with Object Lock: Ensures tamper-evident, 7-year audit retention.

## Rationale
This architecture uses Rust on ECS Fargate to reliably achieve sub-50ms latency at high throughput within a lean 3-engineer team constraint. Strict zero-trust networking, memory zeroization, and sandboxed Wasm execution ensure full PCI-DSS Level 1 compliance and auditable security.