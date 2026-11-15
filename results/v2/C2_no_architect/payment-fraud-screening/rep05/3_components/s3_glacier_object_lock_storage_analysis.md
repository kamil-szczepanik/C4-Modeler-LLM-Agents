## Overview
Real-Time Payment Fraud Screening screens card-not-present payment authorizations for fraud at 3,000 requests per second and manages suspicious cases. It ensures PCI-DSS Level 1 compliance and 7-year tamper-evident auditability on AWS.

## Key Elements
- Scoring Engine Container (AWS ECS on Fargate)
- Case Management Container (AWS ECS on Fargate, AWS Cognito)
- API Gateway (AWS ECS on Fargate)
- Redis Cache (AWS ElastiCache Serverless)
- S3 Glacier Object Lock Storage (AWS S3 Glacier Flexible Archive with Object Lock, AWS KMS)
- Amazon Kinesis Firehose (Managed batching)
- Fraud Analyst (User)
- Payment Gateway (External System)

## Relationships
- Scoring Engine Container -> S3 Glacier Object Lock Storage: Writes cryptographically signed audit logs via Amazon Kinesis Firehose [TLS 1.3, AWS KMS]
- Fraud Analyst -> Case Management Container: Reviews suspicious payments [HTTPS]
- API Gateway -> Scoring Engine Container: Routes authorization requests [gRPC / REST]
- Scoring Engine Container -> Redis Cache: Retrieves rules and session data [Redis Protocol]

## Technology Stack
- Compute: AWS ECS with AWS Fargate for zero-server management by a 3-engineer team
- Storage & Audit: AWS S3 Glacier Flexible Archive with Object Lock (COMPLIANCE mode) and AWS KMS for 7-year tamper-evident retention
- Ingestion & Batching: Amazon Kinesis Firehose to batch high-frequency logs and reduce API costs
- Caching: AWS ElastiCache Serverless for low-latency rule and session lookups
- Authentication: AWS Cognito for secure analyst access management

## Rationale
This architecture uses serverless and managed AWS services to maintain ultra-low operational overhead suitable for a three-engineer team. Strict encryption, WORM storage, and batching satisfy PCI-DSS Level 1 and 7-year audit requirements within the 25,000 EUR monthly budget.