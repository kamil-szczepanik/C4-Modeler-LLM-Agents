## Overview
[The Real-Time Payment Fraud Screening system screens card-not-present payment authorizations for fraud in real time while providing case management and auditability. It processes authorizations with sub-50ms latency at 3,000 TPS on AWS within a €25,000 monthly budget.]

## Key Elements
* Fraud Analyst and Risk Manager / Data Scientist
* AWS ALB / API Gateway
* Real-Time Scoring Engine container (Go, Amazon ECS Fargate)
* API Handler Component, Feature Aggregator Component, Scoring Evaluator Component, Audit Logger Component, Fallback Circuit Breaker Component
* Amazon ElastiCache (Redis)
* Amazon S3 with Object Lock and AWS KMS
* AWS Kinesis Data Streams / Amazon SQS

## Relationships
* AWS ALB / API Gateway -> API Handler Component: Routes HTTP/2 scoring requests
* Feature Aggregator Component -> Amazon ElastiCache (Redis): Retrieves real-time feature vectors via RESP
* Audit Logger Component -> AWS Kinesis Data Streams / Amazon SQS: Batch-streams decision payloads via HTTPS
* Audit Logger Component -> Amazon S3 with Object Lock and AWS KMS: Writes tamper-evident logs via HTTPS
* Fallback Circuit Breaker Component -> Scoring Evaluator Component: Manages in-memory fallback routing states locally

## Technology Stack
* Go / net/http: High-performance, memory-efficient runtime for API handling and scoring
* Amazon ECS Fargate: Container orchestration with pre-provisioned baseline tasks to handle 3,000 TPS under budget
* Amazon ElastiCache (Redis): In-memory data store for ultra-low latency feature retrieval
* AWS Kinesis Data Streams / Amazon SQS: Asynchronous messaging to decouple audit logging from the critical path
* Amazon S3 with Object Lock and AWS KMS: Tamper-evident, cryptographically secured 7-year audit log storage

## Rationale
[This architecture uses containerized Go components and in-memory Redis caching to consistently achieve sub-50ms P99 latency at 3,000 TPS. Asynchronous Kinesis batching and an in-memory fallback circuit breaker ensure PCI-DSS compliance and high availability within budget for a three-person engineering team.]