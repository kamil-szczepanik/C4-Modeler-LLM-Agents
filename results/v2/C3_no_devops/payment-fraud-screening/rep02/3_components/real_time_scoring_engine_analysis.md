## Overview
The Real-Time Scoring Engine screens card-not-present payment authorizations for fraud within sub-50ms latency at 3,000 TPS on AWS eu-west-1. It enforces strict PCI-DSS Level 1 compliance, explainable auditability, and business continuity.

## Key Elements
* **gRPC Inbound Listener:** Tonic/Rust implementation handling incoming screening requests.
* **Decision Logic Coordinator:** Orchestrates execution flow, rules, and circuit-breaker fallback logic.
* **Feature Assembler:** Retrieves features using async Redis client over TCP.
* **Model Evaluator:** Executes ONNX Runtime models via C-bindings with memory zeroization.
* **Audit Dispatcher:** Signs SQS audit payloads via HMAC-SHA256 and dispatches logs.

## Relationships
* **API Gateway / Ingestion Service -> gRPC Inbound Listener:** Forwards screening requests via gRPC with mTLS (TLS 1.3).
* **Decision Logic Coordinator -> Feature Assembler:** Retrieves features via Async TCP (Redis).
* **Decision Logic Coordinator -> Model Evaluator:** Evaluates models via FFI / C-bindings.
* **Decision Logic Coordinator -> Explainability Service:** Requests SHAP values via gRPC / REST.
* **Audit Dispatcher -> Amazon SQS:** Publishes tamper-evident audit logs via AWS SDK.

## Technology Stack
* **Rust:** Chosen over Python/FastAPI to eliminate GC pauses and ensure deterministic sub-50ms P99 latency.
* **Tonic & `ort` crate:** Rust gRPC framework and ONNX Runtime bindings for high-throughput model evaluation.
* **AWS ElastiCache Redis & PostgreSQL (RDS):** Low-latency feature store and metadata storage.
* **Amazon SQS & S3 Object Lock:** Asynchronous event transport and tamper-evident 7-year audit retention.
* **AWS Secrets Manager & AWS Cognito:** Secure secret rotation and service-to-service authentication.

## Rationale
This architecture uses Rust and ONNX Runtime to meet stringent <50ms P99 performance SLAs within a 3-engineer team and €25k/month budget. Strict security controls, mTLS, memory zeroization, and circuit-breaker fail-safes guarantee PCI-DSS compliance and 1-minute availability recovery.