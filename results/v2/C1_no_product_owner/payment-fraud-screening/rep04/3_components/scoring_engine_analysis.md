## Overview
- Real-time payment fraud screening system that evaluates card-not-present payment authorizations for a mid-size payment processor.
- Screens 3,000 transactions per second with sub-50ms P99 latency while maintaining PCI-DSS Level 1 compliance and 7-year tamper-evident auditability.

## Key Elements
- API Ingress Controller (Go): Handles incoming gRPC requests and schema validation.
- Feature Fetcher (Go): Queries Redis with strict timeouts.
- Circuit Breaker & Fallback Manager (Go): Enforces 15ms timeouts and provides local default feature profiles.
- Inference Executor (Go): Executes Wasm-compiled scoring models with cryptographic signature verification.
- Audit Logger (Go): Batches decisions using ring-buffers, hash-chaining, and AWS KMS envelope signing.
- Infrastructure: AWS ECS on Fargate, Aurora PostgreSQL, Amazon ElastiCache (Redis), Amazon S3 (Model Registry), AWS KMS, and AWS API Gateway.

## Relationships
- API Gateway -> API Ingress Controller: Routes payment authorization requests [gRPC over HTTP/2 with mTLS, TLS 1.3]
- API Ingress Controller -> Feature Fetcher: Requests account velocity features [In-memory Go channels]
- Feature Fetcher -> Circuit Breaker & Fallback Manager: Delegates feature resolution [In-memory Go interface]
- Circuit Breaker & Fallback Manager -> Redis / Amazon ElastiCache: Performs feature lookups [TCP with aggressive timeouts]
- Model Registry & Feature Fetcher -> Inference Executor: Feeds Wasm bytecode and hydrated context [In-memory]
- Inference Executor -> Audit Logger: Dispatches decision payload [In-memory Go channels]
- Audit Logger -> Aurora PostgreSQL: Persists hash-chained, KMS-signed audit logs [Encrypted TCP]

## Technology Stack
- Go: Chosen for the Scoring Engine components to achieve sub-50ms P99 latency and low memory footprint.
- WebAssembly (Wasm): Enables zero-downtime model hot-reloading without heavy Python runtimes.
- AWS ECS on Fargate: Provides immutable container deployments to minimize operational overhead for a three-engineer team.
- Amazon Aurora Serverless v2: Auto-scales database workloads to stay under the 25k EUR monthly budget.
- AWS KMS: Provides envelope signing keys for cryptographically sealing tamper-evident audit logs.

## Rationale
- The architecture combines compiled Go services, WebAssembly hot-reloading, and asynchronous ring-buffer logging to meet strict 3,000 TPS and <50ms latency targets.
- Serverless and managed AWS services reduce operational complexity to fit within the constraints of a three-engineer team and a 25,000 EUR monthly budget.