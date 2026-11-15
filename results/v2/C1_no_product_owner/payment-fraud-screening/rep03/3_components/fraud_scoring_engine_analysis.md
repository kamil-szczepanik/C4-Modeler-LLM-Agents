## Overview
[The system is a real-time payment fraud screening engine that evaluates card-not-present authorizations and manages analyst reviews to ensure PCI-DSS Level 1 compliance.]
[It provides sub-50ms latency scoring, zero-downtime model updates, and 7-year tamper-evident auditability within a strict budget.]

## Key Elements
- **API Handler Component (Go)**: Ingress validation, serialization, and PAN tokenization/sanitization gate.
- **Feature Aggregator Component (Go)**: Asynchronously fetches real-time velocity counters with Redis timeout fallback.
- **Scoring Executor Component (Go)**: Evaluates rules and executes local WASM models within strict latency bounds.
- **Audit Dispatcher Component (Go)**: Signs audit payloads and pushes events asynchronously to SQS.
- **In-Memory Model Cache Component (Go)**: Hot-swaps cryptographically verified WASM binaries atomically.
- **Infrastructure Services**: AWS Fargate on Amazon ECS, Amazon ElastiCache Multi-AZ Redis, Amazon RDS PostgreSQL, Amazon SQS, AWS Secrets Manager, and AWS IAM.

## Relationships
- **AWS ALB -> API Handler**: Forwards screening requests via gRPC over mTLS.
- **API Handler -> Feature Aggregator / Scoring Executor**: Passes sanitized payloads via in-memory Go channels.
- **Feature Aggregator -> Amazon ElastiCache Multi-AZ Redis**: Reads/writes real-time features using the Redis Protocol.
- **Scoring Executor -> In-Memory Model Cache**: Hot-swaps compiled WASM binaries via atomic background tickers.
- **Audit Dispatcher -> Amazon SQS**: Publishes signed audit events using the SQS API.
- **Scoring Executor -> Amazon RDS PostgreSQL**: Reads/writes transactional and audit data using the PostgreSQL Wire Protocol with IAM.
- **Containers -> AWS Secrets Manager**: Retrieves runtime secrets, certificates, and cryptographic verification keys via AWS SDK.

## Technology Stack
- **Go (Golang)**: Chosen for high concurrency and deterministic low-latency execution to meet the P99 <50ms SLA.
- **WebAssembly (WASM)**: Enables locally embedded, high-performance scoring model execution without network overhead.
- **Amazon ECS on AWS Fargate**: Provides serverless container orchestration, removing OS patching toil for the 3-engineer team while scaling for 3,000 TPS.
- **Amazon ElastiCache Multi-AZ Redis**: Delivers sub-millisecond feature store lookups for velocity counters.
- **Amazon RDS PostgreSQL**: Stores transactional and audit data securely with IAM authentication.
- **AWS Secrets Manager & IAM**: Secures cryptographic keys, model verification signatures, and enforces ephemeral role-based access.

## Rationale
[This serverless Go and WASM architecture achieves sub-50ms latency at 3,000 TPS while maintaining strict PCI-DSS security boundaries and 7-year tamper-evident auditability.]
[Using AWS Fargate and managed ElastiCache within a single AWS region (eu-west-1) fits the €25,000 monthly budget and operational constraints of a 3-engineer team.]