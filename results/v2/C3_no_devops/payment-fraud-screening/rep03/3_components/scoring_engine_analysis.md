## Overview
The Scoring Engine provides real-time fraud screening for payment authorizations while maintaining strict regulatory compliance. It evaluates transactions with sub-50ms latency to protect merchants from card-not-present fraud.

## Key Elements
- API Router / HTTP Listener (Rust)
- In-Memory Rule & Model Evaluator (Rust, WebAssembly)
- Hot-Reload Coordinator (Rust)
- Audit Dispatcher (Rust)
- Telemetry Emitter (Rust)
- Amazon SQS
- Amazon S3
- Audit Ledger

## Relationships
- API Gateway / Application Load Bearing -> API Router: Ingress payment authorization requests [Synchronous gRPC/REST, mTLS]
- Hot-Reload Coordinator -> Amazon S3: Fetches signed WebAssembly modules and model weights [HTTPS, TLS 1.3]
- Audit Dispatcher -> Amazon SQS / Audit Ledger: Publishes signed tamper-evident decision logs [Asynchronous JSON, HTTPS/TLS 1.3]
- Telemetry Emitter -> Amazon SQS: Flushes aggregated decision metrics [Asynchronous event streaming]

## Technology Stack
- Rust: Chosen for memory safety, deterministic performance, and zero-cost abstractions to meet sub-50ms latency constraints.
- WebAssembly (Wasmtime): Used for executing scoring rules locally in a memory-bounded sandbox with hot-reload capabilities.
- AWS ECS Fargate: Provides container orchestration within budget constraints without managing underlying servers.
- AWS KMS: Utilized for hardware-backed cryptographic signing of audit payloads to guarantee compliance.

## Rationale
This architecture uses local in-memory evaluation and asynchronous logging to prevent database bottlenecks on the hot path, ensuring sub-50ms performance at scale. Cryptographic verification, memory zeroing, and strict sandboxing satisfy PCI-DSS Level 1 and 7-year audit requirements without exceeding the budget.