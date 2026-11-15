## Overview
[The Fraud Scoring Engine evaluates real-time card-not-present payment authorizations to screen for fraud while enforcing strict compliance and performance SLAs.]

## Key Elements
- Request Handler Component (Rust, Axum/Tonic)
- Evaluation Pipeline Component (Rust, Wasm/AST rule evaluator)
- Audit Logger Component (Rust)
- Amazon EC2 (Graviton-based instances) with AWS Auto Scaling Groups
- Amazon ElastiCache Serverless (Redis)
- Amazon QLDB and S3 Object Lock buckets
- AWS KMS (Key Management Service)

## Relationships
- Amazon API Gateway / ALB -> Request Handler Component: Ingress scoring requests via gRPC over mTLS
- Request Handler Component -> Evaluation Pipeline Component: Passes masked payloads via lock-free `crossbeam` channels
- Evaluation Pipeline Component -> Amazon ElastiCache Serverless: Syncs models and rules via Redis protocol over mTLS
- Audit Logger Component -> Amazon QLDB / S3 Object Lock: Dispatches cryptographically signed decision payloads via AWS SDK over TLS

## Technology Stack
- Rust: Chosen for zero garbage collection pauses and predictable memory footprints to guarantee <50ms P99 latency
- AWS EC2 Graviton: Provides predictable microsecond-level CPU performance and eliminates virtualization overhead
- HashiCorp Packer: Automates the creation of immutable AMIs for deployment via Auto Scaling Groups
- AWS KMS: Handles asymmetric payload signing and envelope encryption for compliance

## Rationale
[This architecture guarantees high-throughput, low-latency performance using memory-safe Rust on Graviton instances while meeting stringent PCI-DSS compliance and 7-year auditability constraints within a fixed budget.]