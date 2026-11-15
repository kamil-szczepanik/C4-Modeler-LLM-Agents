## Overview
The Real-Time Payment Fraud Screening system evaluates card-not-present payment authorizations to prevent fraud while maintaining sub-50ms latency. It ensures PCI-DSS Level 1 compliance and 7-year auditability within a fixed budget and small engineering team.

## Key Elements
* Fraud Operations Manager, Fraud Analysts, and Auditors / Regulators
* Payment Gateway / Merchants
* AWS API Gateway
* Fraud Scoring Engine (Go / Rust) containing API Controller, Feature Assembler, Evaluation Core, and Telemetry Publisher
* Case Management & Rules Service (Node.js / Go)
* Audit & Evidence Worker (Go)
* AWS ElastiCache (Redis)
* Amazon SQS
* AWS S3 with Object Lock and Glacier Deep Archive

## Relationships
* Payment Gateway / Merchants -> AWS API Gateway: Submits payment authorization requests [HTTPS/REST]
* AWS API Gateway -> Fraud Scoring Engine: Routes payment requests for scoring [gRPC / Protobuf]
* Fraud Scoring Engine -> AWS ElastiCache (Redis): Queries real-time features with a 30ms timeout [Redis Protocol]
* Fraud Scoring Engine -> Amazon SQS: Publishes decision events asynchronously [AWS SDK]
* Audit & Evidence Worker -> AWS S3: Stores tamper-evident audit trails [AWS SDK]

## Technology Stack
* Go / Rust: Powers the Fraud Scoring Engine for sub-50ms P99 latency at 3,000 TPS.
* AWS ECS with AWS Fargate: Runs containers with minimal operational overhead for a 3-engineer team.
* AWS ElastiCache (Redis): Provides high-throughput, low-latency real-time feature lookups.
* Amazon SQS: Decouples scoring from downstream auditing and metrics to protect the critical path.
* AWS S3 with Object Lock: Ensures tamper-evident, 7-year regulatory auditability.

## Rationale
This architecture uses Go and Rust on AWS Fargate to achieve high performance and low operational complexity within budget constraints. Decoupling real-time scoring from asynchronous auditing ensures strict latency SLAs and robust compliance.