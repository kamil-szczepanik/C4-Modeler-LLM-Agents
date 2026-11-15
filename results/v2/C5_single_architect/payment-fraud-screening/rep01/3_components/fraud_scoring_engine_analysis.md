## Overview
The Fraud Scoring Engine is a low-latency Rust-based container that evaluates 3,000 payment authorizations per second for fraud. It ensures sub-50ms P99 responses while securely executing rules and machine learning models on AWS.

## Key Elements
- **Scoring API Controller**: Rust (`tonic` gRPC) component managing incoming requests.
- **Rule Execution Engine**: Rust compiled evaluation component for deterministic fraud rules.
- **Model Ingestion & Hot-Swap Coordinator**: Rust (`arc-swap`, ONNX Runtime via `ort`) component for zero-downtime model updates.
- **Feature Assembler**: Rust (`tokio` async) component coordinating parallel data gathering.
- **In-Memory Feature Cache Client**: Rust (`redis-rs`) component for low-latency feature retrieval.
- **Decision Publisher**: Rust (`aws-sdk-sqs`) component for asynchronous event dispatch.

## Relationships
- `Scoring API Controller` -> `Feature Assembler`: Gathers context [in-process async]
- `Feature Assembler` -> `In-Memory Feature Cache Client`: Fetches velocity features [TCP/RESP]
- `Rule Execution Engine` -> `Model Ingestion & Hot-Swap Coordinator`: Evaluates rules against active models [in-process lock-free read]
- `Scoring API Controller` -> `Decision Publisher`: Dispatches audit events [async channel]
- `Decision Publisher` -> `AWS SQS`: Enqueues audit logs [HTTPS/AWS API]

## Technology Stack
- **Rust**: Chosen for memory safety, predictable performance, and concurrency control.
- **tonic gRPC**: Provides high-throughput, low-latency inter-service communication.
- **ONNX Runtime (`ort`)**: Enables fast, cross-platform execution of machine learning scoring models.
- **AWS SQS**: Decouples non-critical audit persistence from the strict 50ms latency budget.
- **Redis (`redis-rs`)**: Delivers sub-millisecond in-memory caching for cardholder velocity features.

## Rationale
This component architecture utilizes Rust and asynchronous processing to comfortably handle 3,000 TPS under a 50ms latency constraint. Asynchronous SQS integration preserves the performance budget while satisfying strict 7-year auditability and PCI-DSS compliance requirements.