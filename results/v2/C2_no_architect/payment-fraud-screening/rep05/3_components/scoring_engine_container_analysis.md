## Overview
Real-Time Payment Fraud Screening is a low-latency platform designed to evaluate card-not-present payment authorizations for fraud and manage suspicious cases. It ensures secure, auditable, and sub-50ms transaction processing within strict budgetary and compliance constraints.

## Key Elements
* Fraud Analyst (Internal User)
* Cardholder / End Customer (External User)
* API Gateway (AWS ECS Fargate)
* Scoring Engine Container (AWS ECS Fargate)
* Case Management Container (AWS ECS Fargate, AWS Cognito)
* Redis Cache (AWS ElastiCache Serverless)
* S3 Glacier Object Lock Storage (AWS S3 Glacier with Object Lock, AWS KMS)

## Relationships
* API Gateway -> Scoring Engine Container: Routes real-time scoring requests via internal VPC networking / mTLS
* Scoring Engine Container -> Redis Cache: Queries cached fallback ruleset during outages via isolated VPC subnet
* Scoring Engine Container -> S3 Glacier Object Lock Storage: Writes cryptographically signed audit logs via AWS KMS envelope encryption

## Technology Stack
* AWS ECS (Fargate): Container orchestration chosen for predictable sizing and minimal operational overhead for a 3-engineer team.
* AWS ElastiCache Serverless (Redis): Provides sub-millisecond fallback rule caching to meet the 50ms P99 latency SLA.
* AWS S3 Glacier with Object Lock & AWS KMS: Ensures tamper-evident, 7-year compliant audit logging meeting PCI-DSS Level 1 standards.
* Amazon CloudWatch & ECS Container Insights: Native metrics and structured JSON logging used to eliminate expensive APM licensing and respect the 25,000 EUR monthly budget.

## Rationale
The architecture utilizes serverless and managed AWS services to maintain high availability and PCI-DSS Level 1 compliance without exceeding the 25,000 EUR monthly budget or requiring a large operations team. Strict cryptographic controls, local circuit breakers, and container security guardrails ensure real-time performance and immutable auditability.