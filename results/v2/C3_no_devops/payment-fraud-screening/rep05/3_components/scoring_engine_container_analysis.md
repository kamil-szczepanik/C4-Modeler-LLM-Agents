## Overview
The Real-Time Payment Fraud Screening system evaluates card-not-present payment authorizations to detect fraud and manage analyst reviews. It operates within AWS eu-west-1, ensuring PCI-DSS Level 1 compliance, sub-50ms P99 latency, and tamper-evident 7-year auditability.

## Key Elements
* Fraud Analysts & Compliance Officers (Users)
* Payment Processors & Merchants (External Systems)
* AWS API Gateway / Envoy
* Scoring Engine Container (Rust on AWS ECS Fargate)
* Amazon ElastiCache (Redis Feature Store)
* Immutable Audit Storage (AWS QLDB / S3 Object Lock)
* Rule & Model Distribution Service (AWS SQS + S3)
* AWS Secrets Manager

## Relationships
* AWS API Gateway / Envoy -> Scoring Engine Container: Forwards payment authorization requests [mTLS / HTTP/2]
* Scoring Engine Container -> Amazon ElastiCache: Fetches real-time transaction features [TLS-encrypted TCP/Redis]
* Rule & Model Distribution Service -> Scoring Engine Container: Supplies cryptographically verified Wasm rules [gRPC/S3]
* Scoring Engine Container -> Immutable Audit Storage: Flushes signed decision and explainability payloads asynchronously [HTTPS/REST]

## Technology Stack
* Rust: Chosen for the Scoring Engine Container to guarantee deterministic memory usage and sub-50ms P99 latency.
* AWS ECS Fargate: Provides isolated, managed container execution with strict runtime hardening (read-only root filesystem, dropped capabilities).
* Amazon ElastiCache (Redis): Delivers ultra-low latency feature retrieval over TLS-encrypted connections.
* WebAssembly (Wasm): Enables zero-downtime rule and scoring model updates with cryptographic signature verification.
* AWS Secrets Manager: Secures cryptographic keys for Wasm validation and audit signing via IAM task roles.

## Rationale
This architecture uses memory-safe Rust running on AWS ECS Fargate to reliably process 3,000 TPS under 50ms without garbage collection pauses. Enforcing mTLS, Wasm signature verification, and immutable audit logging satisfies strict PCI-DSS Level 1 compliance and 7-year auditability within a 3-engineer team and 25,000 EUR monthly budget.