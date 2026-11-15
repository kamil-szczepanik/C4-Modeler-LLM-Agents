## Overview
The Real-Time Payment Fraud Screening system evaluates card-not-present payment authorizations for fraud under strict PCI-DSS Level 1 compliance constraints. It provides real-time scoring within 50ms and case management capabilities for fraud analysts in AWS region eu-west-1.

## Key Elements
- **Fraud Analyst**: Primary business user reviewing suspicious transactions.
- **API Gateway / Ingress Container**: AWS ECS Fargate container handling incoming HTTP REST traffic.
- **Scoring Engine Container**: AWS ECS Fargate container executing fraud scoring logic.
- **SageMaker Real-Time Endpoint**: Isolated AWS SageMaker model inference backend in a private subnet.
- **Amazon SQS & DLQ**: Asynchronous message queue with Dead-Letter Queue for audit logging.
- **Amazon QLDB / Amazon S3 Object Lock**: Tamper-evident storage for 7-year audit compliance.
- **GitHub Actions**: CI/CD pipeline automating blue/green zero-downtime deployments.

## Relationships
- API Gateway / Ingress Container -> Scoring Engine Container: Routes scoring requests [REST over internal VPC using TLS 1.3/mTLS]
- Scoring Engine Container -> SageMaker Real-Time Endpoint: Invokes model inference [AWS SDK over VPC interface endpoints]
- Scoring Engine Container -> Amazon SQS: Offloads audit logs asynchronously [AWS SDK with AWS KMS encryption]
- Amazon SQS -> Amazon QLDB / S3 Object Lock: Persists tamper-evident decision logs [AWS SDK]

## Technology Stack
- **AWS ECS Fargate**: Compute platform chosen for zero-server management, fitting the 3-engineer team constraint.
- **AWS SageMaker Real-Time Endpoints**: ML hosting selected over Serverless to eliminate cold starts and meet the 50ms P99 latency SLA (R-04).
- **Amazon SQS & QLDB**: Decoupled asynchronous architecture chosen to protect decision latency while guaranteeing 7-year auditability (R-06).
- **AWS Secrets Manager**: Secure credential injection ensuring zero hardcoded secrets for PCI-DSS Level 1 compliance (R-05).
- **GitHub Actions & AWS ECS**: Automation toolchain enabling zero-downtime model updates (R-03) within a 25,000 EUR monthly budget.

## Rationale
This architecture balances ultra-low latency (50ms P99) and stringent security constraints through decoupled asynchronous logging and dedicated model endpoints. It remains operable by a 3-engineer team within a fixed 25,000 EUR monthly budget by leveraging serverless and managed AWS services.