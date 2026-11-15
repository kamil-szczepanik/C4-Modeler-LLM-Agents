## Overview
[The system is a real-time payment fraud screening platform that evaluates card-not-present transactions for fraud and supports analyst reviews. Its core purpose is to provide sub-50ms fraud decisions while maintaining strict PCI-DSS Level 1 compliance and 7-year auditability.]

## Key Elements
* Fraud Scoring Engine (Java/Spring Boot, AWS ECS Fargate, ONNX/LightGBM)
* Feature Store / Cache Container (Amazon ElastiCache Redis OSS & Amazon DynamoDB)
* Feature Sync Worker (Python / AWS Lambda)
* Transactional Database (Amazon Aurora PostgreSQL)
* Asynchronous Messaging (Amazon SQS & Amazon SNS)
* Case Management Service (Node.js/Python, AWS ECS Fargate)
* Analyst Frontend (Amazon S3 + Amazon CloudFront SPA)
* Audit Storage (Amazon S3 with Object Lock)

## Relationships
* Fraud Scoring Engine -> In-Memory Cache (ElastiCache Redis OSS): Fetches hot velocity aggregates [RESP over TLS]
* Fraud Scoring Engine -> Feature Metadata Store (Amazon DynamoDB): Fetches pre-computed profile features [HTTPS]
* Feature Sync Worker (AWS Lambda) -> In-Memory Cache (Redis): Updates rolling counters [RESP over TLS]
* Feature Sync Worker (AWS Lambda) -> Feature Metadata Store (DynamoDB): Upserts baseline profiles asynchronously [HTTPS]
* Amazon SQS -> Feature Sync Worker (AWS Lambda): Triggers asynchronous feature updates [HTTPS]

## Technology Stack
* AWS ECS Fargate: Provides serverless container orchestration within the 25,000 EUR monthly budget
* Amazon ElastiCache Redis OSS: Delivers ultra-low latency real-time rolling aggregates
* Amazon DynamoDB: Stores user profiles and static feature vectors with point-in-time recovery
* AWS Lambda: Executes serverless asynchronous feature synchronization
* Amazon Aurora PostgreSQL: Serves as the transactional database for persistence

## Rationale
[This architecture guarantees sub-50ms P99 decision latency by decoupling the hot scoring path from batch ingestion using asynchronous SQS-driven updates. It respects the 25,000 EUR monthly budget and 3-engineer constraint while fulfilling PCI-DSS compliance and 7-year auditability.]