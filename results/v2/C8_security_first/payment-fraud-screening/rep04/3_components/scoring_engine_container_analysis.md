## Overview
[The Real-Time Payment Fraud Screening system processes card-not-present payment authorizations to detect fraud and manage analyst reviews.]
[It ensures PCI-DSS compliance, 7-year auditability, and sub-50ms P99 latency under a fixed budget.]

## Key Elements
- Envoy Proxy: Ingress routing and mTLS termination.
- Scoring Engine Container (Go): Stateless core service processing real-time fraud scoring.
- API Router Component: Handles synchronous gRPC scoring requests.
- Model Evaluator Component: Executes compiled fraud models in memory with atomic pointer-swapping.
- Model Loader & Verifier Component: Background worker fetching, verifying, and preparing model artifacts.
- Local Heuristic Fallback Component: Rule-based fallback engine for timeouts or errors.
- Case Management API Container (Node.js/NestJS): Analyst review workflows.
- AWS S3 & AWS KMS: Model artifact storage and cryptographic verification.
- AWS QLDB: Tamper-evident 7-year audit ledger.
- Amazon ECS on AWS Fargate (ARM64/Graviton2): Container orchestration platform.

## Relationships
- Envoy Proxy -> Scoring Engine Container: Routes authorization requests [Internal gRPC over mTLS]
- API Router -> Model Evaluator: Invokes model evaluation [In-memory function call]
- API Router -> Local Heuristic Fallback: Invokes fallback on timeout/error [In-memory fallback]
- Model Loader & Verifier -> AWS S3 / KMS: Fetches and cryptographically verifies models [HTTPS / AWS SDK]
- Model Loader & Verifier -> Model Evaluator: Triggers atomic pointer swap [In-memory pointer update]
- Scoring Engine Container -> AWS QLDB: Emits immutable model and scoring audit events [Async Queue API]

## Technology Stack
- Go: Chosen for high-throughput, low-latency performance and minimal memory footprint.
- AWS Fargate (ARM64/Graviton2): Provides cost-effective, serverless container hosting within budget.
- AWS QLDB: Ensures tamper-evident, immutable audit trails for 7-year compliance.
- AWS KMS: Handles cryptographic signature verification for secure model hot-reloading.
- Amazon Aurora PostgreSQL & ElastiCache: Manages operational data and caching.

## Rationale
[Decomposing the Scoring Engine into decoupled synchronous evaluation and asynchronous verification components guarantees the 50ms P99 latency SLA while maintaining strict PCI-DSS and auditability constraints.]
[Leveraging Go, AWS Graviton2, and Fargate satisfies the strict 3,000 req/sec performance requirement within the 25,000 EUR monthly budget operated by a 3-engineer team.]