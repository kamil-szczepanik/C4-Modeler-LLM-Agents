## Overview
[The Real-Time Payment Fraud Screening system processes card-not-present payment authorizations to approve, decline, or route transactions for review. It ensures high performance, PCI-DSS compliance, and auditable decision-making within a strict budget.]

## Key Elements
* API Handler Component (Go / net/http)
* Feature Aggregator Component
* Scoring Engine Component
* Audit Publisher Component
* Fallback Circuit Breaker Component
* Telemetry Interceptor Component
* Amazon API Gateway & Fallback Layer
* Amazon ECS Fargate
* Amazon DynamoDB
* Amazon SQS and SNS
* Amazon Aurora PostgreSQL
* Amazon S3 with Object Lock
* AWS KMS
* Fraud Analysts and Risk Operations Managers

## Relationships
* API Gateway & Fallback Layer -> API Handler Component: Internal routing of scoring requests via [REST/gRPC]
* Feature Aggregator Component -> Amazon DynamoDB: Reads and writes low-latency features via [VPC endpoints over AWS]
* Scoring Engine Component -> Feature Aggregator Component: Internal data consumption via [Go channels and context propagation]
* Audit Publisher Component -> Amazon SQS/SNS: Publishes asynchronous audit events via [AWS SDK]
* Real-Time Scoring Service -> Amazon S3: Dynamically loads cryptographically verified model binaries and rules via [HTTPS/AWS SDK]

## Technology Stack
* Go: Selected for the Real-Time Scoring Service to meet strict P99 latency (<50 ms at 3,000 TPS) without Go garbage collection overhead.
* AWS ECS Fargate: Container orchestration chosen to maintain low operational load for a 3-person team while fitting within the 25k EUR monthly budget.
* Amazon DynamoDB: Low-latency NoSQL data store used for the Feature Cache to achieve sub-15ms feature retrieval.
* Amazon SQS and SNS: Messaging infrastructure used by the Audit Publisher to decouple non-blocking audit event generation from the hot path.
* AWS KMS: Secures model decryption keys and audit signing keys with automated rotation and least-privilege IAM policies.

## Rationale
[This architecture guarantees sub-50ms P99 latency at 3,000 TPS while maintaining PCI-DSS Level 1 compliance and a 7-year audit trail. It respects strict operational and budget constraints by leveraging managed AWS services and asynchronous patterns.]