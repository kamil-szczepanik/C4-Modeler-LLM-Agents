## Overview
The Real-Time Payment Fraud Screening system screens card-not-present payment authorizations for fraud under 50 ms latency and manages analyst reviews. It ensures PCI-DSS Level 1 compliance and 7-year tamper-evident auditability within a fixed budget.

## Key Elements
- API Router & Token Handler: Go component terminating gRPC and sanitizing card data.
- Feature Aggregator: Go component fetching data using Redis pipelining (`errgroup`).
- Decision Orchestrator: Go component coordinating ML inference and zero-downtime rules.
- Audit Logger & Cryptographic Signer: Go component signing decisions via AWS KMS.
- Metrics & Tracing Interceptor: Go middleware using `zerolog` for zero-allocation telemetry.
- ML Inference Service: Python with ONNX Runtime on AWS ECS Fargate.
- Amazon ElastiCache: Redis caching layer for fast feature lookups.
- Amazon DynamoDB: Operational database for transaction and authorization data.
- Amazon S3 Object Lock: Tamper-evident storage for 7-year audit compliance.

## Relationships
- AWS API Gateway -> API Router & Token Handler: Routes authorization requests [gRPC]
- API Router & Token Handler -> Feature Aggregator: Invokes feature lookup [In-memory Go calls]
- Feature Aggregator -> Amazon ElastiCache: Fetches user and card features [TCP (RESP)]
- Decision Orchestrator -> ML Inference Service: Requests model scoring [Internal gRPC over HTTP/2]
- Audit Logger & Cryptographic Signer -> Amazon DynamoDB: Persists audit records [HTTPS (AWS SDK v2)]
- Audit Logger & Cryptographic Signer -> Amazon S3 Object Lock: Archives signed payloads [HTTPS (AWS SDK v2)]

## Technology Stack
- Go: Chosen for high-throughput, low-latency microservices and minimal GC overhead.
- AWS ECS Fargate: Container orchestration matching the 3-engineer operational capacity.
- ONNX Runtime: High-performance machine learning model execution.
- Amazon DynamoDB: Scalable operational storage with persistent HTTPS connection pooling.
- Amazon S3 Object Lock: Write-once-read-many (WORM) storage for regulatory 7-year audit trails.
- AWS KMS: Hardware-backed cryptographic signing for tamper-evident audit logging.

## Rationale
This component architecture uses in-memory Go primitives and connection pooling to consistently achieve sub-50ms P99 latency at 3,000 TPS. AWS serverless and container services keep operational overhead minimal for a three-engineer team while satisfying strict PCI-DSS and auditability mandates.