## Overview
The system is a Real-Time Payment Fraud Screening platform that evaluates card-not-present payment authorizations to prevent fraud and manage analyst reviews. It provides sub-50ms decision latency while ensuring PCI-DSS Level 1 compliance and 7-year tamper-evident auditability.

## Key Elements
- Fraud Scoring Engine (Go service with embedded ONNX runtime)
- Consumer Worker Pool (AWS Lambda / ECS Fargate)
- Amazon MSK Serverless (Kafka cluster with `payment-audit-events` topic)
- Amazon Aurora Serverless v2
- Amazon S3
- AWS KMS (Customer Managed Keys)

## Relationships
- Fraud Scoring Engine -> Amazon MSK Serverless: Streams asynchronous audit logs via `Kafka protocol` over `TLS 1.3` using `AWS IAM` authentication
- Amazon MSK Serverless -> Consumer Worker Pool: Polls streaming data via `Kafka consumer poll protocol` over `TLS 1.3`
- Consumer Worker Pool -> Amazon Aurora Serverless v2: Persists batch records via `PostgreSQL tabular wire protocol` over `TLS`
- Consumer Worker Pool -> Amazon S3: Persists batch records via `HTTPS (AWS SDK)`

## Technology Stack
- Amazon MSK Serverless: Managed event streaming with automatic scaling to handle peak traffic without exceeding budget
- AWS ECS Fargate & Lambda: Compute for the Consumer Worker Pool to process stream data without managing underlying servers
- AWS KMS: Encryption at rest using customer-managed keys with automated 365-day key rotation
- Terraform & GitHub Actions: Infrastructure-as-Code and GitOps workflow for automated deployments and drift detection

## Rationale
This architecture decouples the synchronous fraud scoring hot-path from asynchronous audit logging, ensuring P99 decision latency remains under 50ms. Utilizing serverless AWS components enforces strict PCI-DSS compliance and data tokenization within a 25,000 EUR monthly budget operated by a three-engineer team.