## Overview
The Real-Time Payment Fraud Screening system screens card-not-present payment authorizations in real time and provides case management for fraud analysts. It ensures PCI-DSS compliance and immutable 7-year auditability on AWS within a fixed budget.

## Key Elements
- Fraud Analysts, Regulatory / Compliance Auditors
- Payment Gateway / Acquirer Systems, Identity Provider (IdP), External Tokenization/Vault Service
- AWS API Gateway (REST)
- Scoring Engine (Go, AWS ECS Fargate)
- Case Management Backend (Node.js/Go, AWS ECS Fargate)
- Amazon DynamoDB, Amazon Aurora PostgreSQL
- Amazon Kinesis Data Firehose
- Amazon S3 Object Lock: S3 Bucket with Object Lock (Compliance Mode), Bucket Lifecycle Policy Manager (AWS S3 Lifecycle), AWS KMS Encryption Key (AWS KMS)

## Relationships
- Payment Gateway -> AWS API Gateway: Submits authorization requests [HTTPS / JSON]
- Fraud Analysts -> AWS API Gateway: Manages suspicious payment cases [HTTPS / REST]
- AWS API Gateway -> Scoring Engine: Routes payment requests for evaluation [gRPC / Internal VPC]
- Scoring Engine -> Amazon DynamoDB: Fetches rules and caches fraud states [AWS SDK]
- Case Management Backend -> Amazon Aurora PostgreSQL: Stores analyst decisions and cases [PostgreSQL Wire Protocol]
- Scoring Engine -> Amazon Kinesis Data Firehose: Streams transaction decisions [AWS SDK]
- Amazon Kinesis Data Firehose -> S3 Bucket with Object Lock: Persists immutable audit logs [AWS S3 API / HTTPS]
- S3 Bucket with Object Lock -> AWS KMS: Encrypts and decrypts audit objects [AWS KMS API]
- Regulatory / Compliance Auditors -> S3 Bucket with Object Lock: Inspects audit logs [AWS Athena / S3 GET]

## Technology Stack
- AWS (eu-west-1): Target cloud infrastructure within budget
- Go and Node.js: High-performance backend services for low latency
- AWS ECS Fargate: Container orchestration minimizing operational overhead for 3 engineers
- Amazon DynamoDB and Aurora PostgreSQL: Scalable persistence layers
- AWS KMS (AES-256): Customer-managed keys ensuring PCI-DSS encryption
- Amazon S3 Object Lock (Compliance Mode): WORM storage enforcing 7-year immutable audit retention

## Rationale
This architecture uses managed AWS services to meet the strict sub-50ms latency and PCI-DSS requirements without exceeding the 25,000 EUR monthly budget. S3 Object Lock and KMS guarantee tamper-evident 7-year auditability while minimizing operational complexity for a three-engineer team.