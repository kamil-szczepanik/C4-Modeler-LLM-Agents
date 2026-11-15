## Overview
The system is a real-time payment fraud screening platform deployed on AWS eu-west-1, designed to screen card-not-present payment authorizations and manage fraud reviews. It ensures PCI-DSS Level 1 compliance and 7-year tamper-evident auditability while maintaining strict performance and budget constraints.

## Key Elements
- Fraud Analyst, Risk Manager / Data Scientist, Compliance & Audit Officer (Users)
- Payment Gateway / Processing Engine (External System)
- Amazon API Gateway and Application Load Balancer (AWS API Gateway, ALB)
- Scoring Engine and Case Management UI & Backend (AWS ECS Fargate containers)
- Serverless Tasks (AWS Lambda container)
- Model Artifacts and Audit Logs Storage (Amazon S3)
- Ledger Database (AWS QLDB)
- Security and Management Services (AWS IAM, AWS Secrets Manager, AWS KMS, AWS CodePipeline, AWS CloudWatch & X-Ray)

## Relationships
- Payment Gateway to AWS API Gateway/ALB via HTTPS/TLS 1.3 for real-time authorization requests.
- Scoring Engine to Amazon S3 via HTTPS/TLS 1.3 to fetch fraud models.
- Serverless Tasks (AWS Lambda) to Amazon S3 via HTTPS/TLS 1.3 for asynchronous Model & Rule Sync.
- Serverless Tasks (AWS Lambda) to AWS QLDB via HTTPS/TLS 1.3 with DLQ support for Audit & Compliance Dispatch.
- Case Management Backend to AWS ECS Fargate via internal VPC networking.

## Technology Stack
- AWS Lambda: Executes asynchronous tasks (Model Sync, Audit Dispatch) with pay-per-use scaling to maintain the 25k EUR/month budget.
- AWS ECS Fargate: Hosts real-time scoring and case management containers for scalable, serverless container orchestration.
- AWS QLDB: Provides tamper-evident ledger storage to satisfy 7-year auditability requirements.
- Amazon S3: Stores encrypted model artifacts and audit logs with server-side encryption.
- AWS KMS: Encrypts data at rest with automatic key rotation.
- AWS Secrets Manager: Manages dynamic configurations and keys securely at runtime.
- AWS CloudWatch & X-Ray: Provides centralized logging, metrics, and distributed tracing.

## Rationale
This architecture uses serverless compute and managed AWS services to handle 3,000 TPS under a 50ms latency limit while strictly enforcing PCI-DSS compliance and a 25,000 EUR monthly budget. Asynchronous AWS Lambda tasks isolate heavy audit logging and model synchronization from the critical real-time payment path.