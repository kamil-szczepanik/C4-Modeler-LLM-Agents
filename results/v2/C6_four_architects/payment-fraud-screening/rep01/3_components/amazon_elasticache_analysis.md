## Overview
Real-Time Payment Fraud Screening screens card-not-present payment authorizations for fraud prior to approval and provides case management for suspicious transactions. It operates under strict PCI-DSS Level 1 compliance and a 50 ms latency threshold on AWS.

## Key Elements
- Real-Time Scoring Engine (Go on AWS ECS Fargate)
- ML Inference Service (Python with ONNX Runtime on AWS ECS Fargate)
- Case Management Backend (Go/Node.js on AWS ECS Fargate)
- Fraud Analyst Frontend (Amazon CloudFront and S3)
- Amazon ElastiCache (Redis Feature Store)
- Amazon DynamoDB
- Amazon S3 Object Lock
- Amazon EventBridge

## Relationships
- Real-Time Scoring Engine -> Amazon ElastiCache: Fetches customer velocity profiles [TCP (RESP), TLS]
- Real-Time Scoring Engine -> ML Inference Service: Requests fraud scores [gRPC, TLS]
- Case Management Backend -> Amazon DynamoDB: Persists audit trails and case data [HTTPS]
- Backup & Snapshot Agent -> Amazon S3 Object Lock: Exports point-in-time RDB snapshots [HTTPS]

## Technology Stack
- AWS ECS Fargate: Container orchestration chosen for zero-server management by a 3-engineer team.
- Go and Python: Go for high-throughput, low-latency API scoring; Python with ONNX for ML inference.
- Amazon ElastiCache (Redis): In-memory feature store for sub-millisecond feature lookups.
- Amazon DynamoDB: NoSQL database for flexible case storage and tamper-evident audit logging.
- Amazon S3 Object Lock: WORM storage ensuring 7-year immutable audit retention.

## Rationale
This architecture uses serverless and managed AWS services to minimize operational overhead for a three-engineer team while easily scaling to handle 3,000 TPS. In-memory caching and optimized runtimes guarantee P99 latencies under 50 ms to meet strict performance and compliance requirements.