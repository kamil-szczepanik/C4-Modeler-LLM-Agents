## Overview
The Fraud Scoring Engine provides real-time, sub-50ms fraud detection for card-not-present payment authorizations. It securely evaluates transactions, provides explainable AI metrics, and maintains strict compliance for a mid-size payment processor.

## Key Elements
- **Rule Evaluation Engine**: Rust-based component executing compiled deterministic rules.
- **ML Scoring Runtime**: Embedded ONNX Runtime executing gradient-boosting models with SHAP explainability.
- **Feature Store Client**: In-memory LRU cache backed by Redis with AWS KMS encryption.
- **Audit Payload Formatter**: Zero-copy Rust channel (`crossbeam`) assembler for tamper-evident SHA-256 chains.
- **Infrastructure**: AWS ECS (Fargate) managed via Terraform within eu-west-1.

## Relationships
- **API Gateway / Ingestion Service** -> **Fraud Scoring Engine**: Delivers scoring payloads via gRPC with mTLS.
- **Rule Evaluation Engine & ML Scoring Runtime** -> **Feature Store Client**: Executes synchronous lookups via Redis.
- **Fraud Scoring Engine** -> **Amazon SQS**: Publishes signed audit payloads asynchronously.
- **Fraud Scoring Engine** -> **Amazon Aurora**: Persists immutable ledger records for 7-year audit retention.

## Technology Stack
- **Rust**: Selected for memory safety and zero garbage collection pauses to guarantee sub-50ms P99 latency.
- **AWS ECS (Fargate)**: Chosen to minimize operational toil for a three-engineer team within a 25,000 EUR monthly budget.
- **ONNX Runtime**: Embedded via C-bindings to run lightweight ML models directly within the scoring engine.
- **Redis (AWS ElastiCache)**: Provides low-latency feature lookups encrypted at rest with AWS KMS.
- **Amazon SQS & Aurora**: Decouples non-blocking audit logging while ensuring tamper-evident PCI-DSS compliance.

## Rationale
This architecture uses Rust and Fargate to meet strict sub-50ms P99 latency and PCI-DSS Level 1 compliance requirements without exceeding the 25,000 EUR budget. Asynchronous cryptographic hashing and SQS batching balance high-throughput availability with an immutable 7-year audit trail.