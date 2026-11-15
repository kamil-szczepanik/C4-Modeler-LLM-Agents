## Overview
The Scoring Engine is an internal component of the Real-Time Payment Fraud Screening system that evaluates card-not-present payment authorizations for fraud to support secure payment processing. It provides sub-50ms fraud scoring, dynamic model updates, and immutable audit logging while maintaining PCI-DSS Level 1 compliance.

## Key Elements
- **API Handler Component (Go):** Manages ingress traffic via HTTP/2, tokenization boundary checks, and circuit-breaker fallback logic.
- **Model Evaluator Component (Go with WebAssembly/ONNX runtime):** Executes in-memory fraud scoring and computes explainability feature weights.
- **Model Hot-Swapper Component (Go):** Background loader that verifies cryptographic signatures and hot-swaps ONNX models without downtime.
- **Feature Store Cache Component (In-memory/Go LRU):** Retrieves real-time velocity counters for transaction evaluation.
- **Audit Dispatcher Component (Go):** Cryptographically signs decision payloads and dispatches them asynchronously.

## Relationships
- **API Handler -> Model Evaluator / Feature Store Cache:** Executes synchronous calls [HTTP/2 / In-Memory] to score requests and fetch velocity data.
- **Model Hot-Swapper -> Model Evaluator:** Securely loads cryptographically verified model binaries into memory [Function Call].
- **Model Evaluator -> Audit Dispatcher:** Passes explainability feature vectors and decision inputs [In-Memory].
- **Audit Dispatcher -> Amazon SQS / SNS:** Publishes signed, tamper-evident audit payloads [AWS SDK / HTTPS].

## Technology Stack
- **Go:** Chosen for high-throughput, low-latency concurrency and minimal memory footprint.
- **ONNX / WebAssembly:** Selected for executing high-performance, in-memory machine learning inference within strict latency bounds.
- **Amazon ECS on AWS Fargate:** Utilized to containerize components within a fixed infrastructure budget and small engineering team.
- **AWS KMS & S3:** Used for secure storage and cryptographic validation of signed model artifacts.

## Rationale
This architecture uses an in-memory Go and ONNX design to achieve sub-50ms P99 latency at 3,000 requests per second. It ensures PCI-DSS Level 1 compliance, zero-downtime model updates, and robust 7-year auditability within a 25,000 EUR monthly budget operated by three engineers.