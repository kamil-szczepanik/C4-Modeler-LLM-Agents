## Overview
[The system is a real-time payment fraud screening platform that evaluates payment authorizations and manages suspicious transactions. Its core purpose is to prevent fraud while ensuring regulatory compliance and sub-50ms decision latency.]

## Key Elements
- Fraud Analyst, Fraud Operations Manager, Risk Rule Author, Data Scientist, Regulatory / Compliance Auditor
- Payment Gateway / Acquirer
- AWS ALB (API Gateway)
- Fraud Scoring Engine (Java/Spring Boot container on AWS ECS Fargate with embedded ONNX Runtime)
- Case Management API & UI (Go/Node.js backend container and React SPA frontend)
- Rule/Model Authoring Service
- Amazon SQS
- Amazon DynamoDB
- AWS S3 Object Lock

## Relationships
- Payment Gateway calls AWS ALB via gRPC/HTTPS over TLS
- AWS ALB routes traffic to the Fraud Scoring Engine and tokenizes PANs
- Fraud Scoring Engine persists decisions to Amazon DynamoDB and sends messages via Amazon SQS
- Amazon SQS routes async cases to the Case Management API
- Rule/Model Authoring Service publishes updates via Amazon SQS
- Fraud Scoring Engine and audit pipelines archive data to AWS S3 Object Lock using AWS KMS CMKs

## Technology Stack
- AWS ECS Fargate: Container orchestration for zero-downtime blue/green deployments
- ONNX Runtime (XGBoost): Embedded ML inference engine for sub-50ms P99 latency
- Amazon DynamoDB: Hot data store for low-latency state and rule lookups
- Amazon S3 Object Lock: Tamper-evident storage for 7-year audit compliance
- Amazon SQS: Asynchronous message bus for case routing without MSK operational overhead
- AWS ALB: TLS termination, request routing, and fail-safe circuit breaker health checks

## Rationale
[This architecture fits the requirements by leveraging managed AWS serverless and container services to respect the 3-engineer limit and €25k/month budget. It guarantees sub-50ms P99 latency via embedded ML runtimes while strictly bounding PCI-DSS scope and enforcing 7-year auditability.]