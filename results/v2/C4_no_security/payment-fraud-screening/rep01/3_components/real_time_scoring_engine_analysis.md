## Overview
The Real-Time Payment Fraud Screening system evaluates card-not-present payment authorizations for fraud under 50 ms to prevent checkout fraud while ensuring high availability. It processes high-throughput transactions on AWS while maintaining PCI-DSS Level 1 compliance and 7-year auditability.

## Key Elements
* HTTP/gRPC Ingress Router (Go container component)
* Feature Assembler (Go container component)
* Inference & Rule Executor (Go + ONNX Runtime C-API)
* Audit Dispatcher (Go container component)
* Model & Rule Synchronizer (Go background goroutine component)
* Amazon ElastiCache Redis (Feature Store)
* Amazon S3 (Audit Log and Model Storage)

## Relationships
* API Gateway -> HTTP/gRPC Ingress Router: Forwards payment authorizations [REST/HTTPS]
* Feature Assembler -> Amazon ElastiCache Redis: Retrieves transaction features [Redis Protocol]
* Inference & Rule Executor -> Model & Rule Synchronizer: Atomically swaps model references via `atomic.Value` [In-memory]
* Audit Dispatcher -> Amazon S3: Flushes asynchronous audit payloads [S3 API / HTTPS]

## Technology Stack
* Go: Chosen for ultra-low latency and minimal memory footprint to meet the <50 ms P99 requirement.
* ONNX Runtime C-API: Enables high-performance execution of compiled machine learning models.
* Amazon ElastiCache Redis: Provides low-latency, in-memory feature retrieval at 3,000 TPS.
* Amazon S3: Delivers cost-effective, tamper-evident storage for audit logs and model binaries.

## Rationale
This architecture achieves sub-50 ms P99 latency at 3,000 TPS within a 25,000 EUR monthly budget by utilizing single-service containerization with in-memory Go concurrency. Strict decoupling of asynchronous auditing, read-only Redis patterns, and atomic model hot-swapping ensure high availability and zero-downtime updates.