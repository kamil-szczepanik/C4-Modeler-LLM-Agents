## Overview
The system is a real-time payment fraud screening platform that evaluates card-not-present payment authorizations to prevent fraud and manage suspicious reviews. It ensures strict regulatory compliance, low-latency scoring, and robust tamper-evident auditing within a fixed infrastructure budget.

## Key Elements
- Fraud Analyst (User)
- Payment Gateway / Acquirer (External System)
- API Gateway / Ingestion Container (AWS API Gateway / Envoy proxy)
- High-Performance Scoring Engine (AWS ECS on Fargate)
- Feature Store (Redis)
- Async Event Bus (AWS EventBridge / SQS)
- Case Management Web Application (AWS ECS on Fargate)
- Model & Rule Registry Container (Container Service)
- Audit & Compliance Storage (AWS S3 with Object Lock and Parquet format)
- Configuration & Secrets Management (AWS Secrets Manager / Parameter Store)

## Relationships
- Payment Gateway / Acquirer -> API Gateway / Ingestion Container: Sends authorization requests [HTTPS/REST]
- API Gateway / Ingestion Container -> High-Performance Scoring Engine: Forwards authorization requests [gRPC]
- High-Performance Scoring Engine <-> Feature Store: Fetches and updates user features [Redis Protocol]
- High-Performance Scoring Engine -> Async Event Bus: Publishes scoring decisions and audit logs [AWS SQS/SNS]
- Async Event Bus -> Audit & Compliance Storage: Streams immutable audit records [AWS SQS/SNS]
- Fraud Analyst -> Case Management Web Application: Reviews suspicious transactions [HTTPS]
- Case Management Web Application -> High-Performance Scoring Engine: Updates case statuses and feedback [HTTPS/REST]

## Technology Stack
- Cloud Infrastructure: AWS (Region: eu-west-1) chosen for managed scalability and compliance features.
- Compute: AWS ECS on Fargate for containerized microservices without server management overhead.
- Storage & Audit: AWS S3 with Object Lock (Compliance Mode) and Parquet format for tamper-evident 7-year retention.
- Query & Analytics: Amazon Athena with Partition Projection and predefined views for cost-controlled serverless querying.
- In-Memory Data Store: Redis for sub-millisecond feature retrieval supporting P99 < 50ms latency.
- Messaging: AWS SQS/SNS with Dead-Letter Queues (DLQ) for asynchronous decoupled event processing.
- Infrastructure as Code: Terraform with prevent-destroy guards to secure compliance configurations.

## Rationale
This architecture uses serverless and managed AWS services to minimize operational overhead for a three-engineer team while keeping costs within the 25,000 EUR monthly budget. S3 Object Lock and Athena ensure strict PCI-DSS Level 1 compliance and 7-year tamper-evident auditability without sacrificing query performance.