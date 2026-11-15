## Overview
Real-Time Payment Fraud Screening screens card-not-present payment authorizations for fraud to protect merchant revenue while enforcing PCI-DSS compliance and 7-year auditability. The Real-Time Scoring Engine Container delivers sub-50ms P99 fraud scoring decisions at 3,000 TPS within a 25,000 EUR monthly budget.

## Key Elements
* Request Router & Token Masker (Rust): Validates schemas and strips PCI data.
* Feature Aggregator (Rust): Fetches real-time velocity metrics via Amazon ElastiCache Serverless.
* Inference Executioner (Rust with ONNX Runtime): Evaluates pre-compiled ML models and deterministic business rules.
* Circuit Breaker & Fallback Handler (Rust): Enforces 40ms timeouts and fails-open to "review".
* Audit & Feature Store (Amazon S3 with Object Lock): Stores 100% immutable audit logs and features for 7 years.

## Relationships
* API Gateway / Ingestion Service Container -> Request Router & Token Masker: Forwards authorization requests [gRPC over TLS]
* Feature Aggregator -> Amazon ElastiCache Serverless: Fetches real-time velocity metrics [RESP over TCP]
* Inference Executioner -> Audit & Feature Store: Writes audit logs, model versions, and feature explanations [AWS SDK / HTTPS]

## Technology Stack
* Rust: Chosen for memory safety and zero-cost abstractions to guarantee sub-50ms P99 latency.
* ONNX Runtime: Enables high-performance, in-process machine learning model inference.
* Amazon ElastiCache Serverless: Provides high-availability Redis caching within budget constraints.
* Amazon ECS Fargate: Runs serverless container workloads without manual infrastructure management.

## Rationale
Decomposing the scoring engine into optimized Rust components with local caching achieves the required 3,000 TPS at sub-50ms latency. Strict decoupling of audit logging from performance tracing ensures 100% compliance with 7-year retention rules within fixed cost limits.