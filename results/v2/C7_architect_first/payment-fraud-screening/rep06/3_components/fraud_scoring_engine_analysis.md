## Overview
The Real-Time Payment Fraud Screening system screens card-not-present payment authorizations for fraud under 50ms P99 latency while supporting analyst reviews and 7-year tamper-evident audits. It operates within strict PCI-DSS Level 1 constraints on AWS for a mid-size payment processor.

## Key Elements
- API Handler (Go)
- Feature Aggregator (Go)
- Inference Orchestrator (Go with embedded ONNX Runtime)
- Explainability Engine (Go)
- Buffered Dispatcher (Go with BadgerDB)
- Amazon ElastiCache for Redis
- Amazon S3 with Object Lock (WORM)
- AWS ECS Fargate
- Amazon Aurora Serverless v2

## Relationships
- API Gateway -> API Handler: Routes authorization requests [gRPC/mTLS]
- API Handler -> Feature Aggregator: Requests feature vectors [In-memory]
- Feature Aggregator -> Amazon ElastiCache for Redis: Performs parallel feature lookups [TCP/TLS]
- Inference Orchestrator -> Explainability Engine: Calculates tree-path contribution scores [In-memory]
- Buffered Dispatcher -> Amazon S3: Batches encrypted audit logs [HTTPS/TLS]

## Technology Stack
- Go: Chosen for high concurrency and sub-50ms P99 latency performance.
- AWS ECS Fargate: Minimizes operational overhead for a three-engineer team within budget.
- ONNX Runtime: Enables in-memory ML inference without network hops.
- BadgerDB: Provides encrypted ephemeral storage for zero-loss audit queuing.
- Amazon S3 with Object Lock: Ensures tamper-evident, 7-year audit compliance cost-effectively.

## Rationale
This architecture uses an optimized single Go binary on AWS ECS Fargate to meet strict sub-50ms latency SLAs and budget limits. In-memory components and secure local queuing guarantee PCI-DSS compliance and zero-loss auditability without sacrificing availability.