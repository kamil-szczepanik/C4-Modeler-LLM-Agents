## Overview
The Real-Time Payment Fraud Screening system evaluates card-not-present payment authorizations to prevent fraud while enabling compliance-driven review workflows. It delivers high-performance risk decisions with strict P99 latency controls and tamper-evident auditability.

## Key Elements
- Real-Time Scoring Engine (Go, AWS EC2)
- Rule Evaluation Component (Go)
- Feature Aggregator Component (Go)
- Model & Rule Registry Component (Go)
- Explainability Engine Component (Go)
- Audit Trail Emitter (Go)
- Amazon ElastiCache (Redis)
- Amazon SQS
- Amazon S3

## Relationships
- AWS API Gateway -> Real-Time Scoring Engine: Routes authorization traffic [HTTP/gRPC with mTLS]
- Real-Time Scoring Engine -> Amazon ElastiCache (Redis): Retrieves velocity counters and features [Redis Protocol with TLS/AUTH]
- Model & Rule Registry Component -> Amazon S3: Downloads immutable rules and model weights [HTTPS]
- Audit Trail Emitter -> Amazon SQS: Pushes cryptographically signed decision payloads [AWS SDK/SQS API]

## Technology Stack
- Go: Selected for zero-garbage-collection pauses to meet the sub-50ms latency requirement.
- AWS EC2: Replaced Fargate to eliminate cold starts and guarantee predictable CPU performance.
- Amazon ElastiCache (Redis): Provides high-speed in-memory feature storage for low-latency rule evaluation.
- AWS KMS: Used by the Audit Trail Emitter to cryptographically sign decision payloads for tamper-evidence.
- Amazon S3: Stores versioned machine learning models and fraud rules for zero-downtime hot-reloading.

## Rationale
This architecture uses Go binaries on provisioned AWS EC2 instances to consistently achieve sub-50ms P99 latency at 3,000 TPS. Furthermore, it incorporates asynchronous audit logging, cryptographic model verification, and automated fail-open circuits to satisfy strict PCI-DSS Level 1 compliance and budget constraints.