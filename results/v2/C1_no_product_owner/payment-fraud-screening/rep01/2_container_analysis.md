## Overview
The Real-Time Payment Fraud Screening system evaluates card-not-present payment authorizations to detect fraud and routes suspicious cases to analysts. It ensures PCI-DSS compliance, <50ms P99 latency, and auditable decision logging within budget.

## Key Elements
- **API Gateway & Routing Layer**: AWS API Gateway and ALB handling ingress and tokenization hand-offs.
- **Real-Time Scoring Service**: Go container on Amazon ECS on EC2 processing synchronous authorizations via gRPC.
- **Case Management Backend**: Java Spring Boot container on Amazon ECS on Fargate managing analyst review workflows.
- **Data & Audit Stores**: Amazon DynamoDB (with AWS KMS and DynamoDB Streams) for tamper-evident audit logs and feature store; Amazon RDS PostgreSQL for case management.
- **Messaging & Eventing**: Amazon SQS, SNS, and EventBridge decoupling real-time scoring from asynchronous auditing and case creation.

## Relationships
- **Payment Gateway to API Gateway**: Ingests authorization requests over HTTPS.
- **API Gateway to Real-Time Scoring Service**: Forwards requests using gRPC for low-latency evaluation.
- **Real-Time Scoring Service to DynamoDB**: Writes cryptographically hashed, immutable decision payloads via AWS KMS.
- **Real-Time Scoring Service to SQS**: Asynchronously publishes review cases and audit events.
- **SQS to Case Management Backend**: Triggers analyst workflows for suspicious transactions.

## Technology Stack
- **Go**: Used for the Real-Time Scoring Service to guarantee P99 latency below 50ms at 3,000 TPS.
- **Amazon ECS on EC2**: Provides predictable CPU pinning and avoids cold-start virtualization overhead for the hot path.
- **Amazon ECS on Fargate**: Runs the async Case Management Backend to minimize operational overhead for a 3-engineer team.
- **Amazon DynamoDB & AWS KMS**: Delivers low-latency storage with cryptographic hashing and WORM backups for 7-year tamper-evident auditability.
- **AWS Secrets Manager**: Eliminates static secrets by injecting credentials dynamically at runtime.

## Rationale
This architecture uses Go on ECS EC2 for predictable, ultra-low latency transaction screening while leveraging serverless queues and Fargate for cost-effective case management. Strict separation of concerns, in-memory PAN handling, and cryptographic audit logging fulfill PCI-DSS Level 1 and 7-year audit requirements within a 25,000 EUR monthly AWS budget.