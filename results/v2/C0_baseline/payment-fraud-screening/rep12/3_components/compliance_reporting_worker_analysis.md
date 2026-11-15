## Overview
Real-Time Payment Fraud Screening screens card-not-present payment authorizations for mid-size payment processors before approval, while providing a case management system for fraud analysts. The system ensures PCI-DSS Level 1 compliance and 7-year auditability on AWS within a 25,000 EUR monthly budget.

## Key Elements
- Fraud Analysts and Risk Managers
- Compliance Officers and Auditors
- Amazon API Gateway
- Real-Time Scoring Engine (Go microservice on AWS ECS EC2)
- Case Management System Frontend (React SPA on Amazon S3 + Amazon CloudFront)
- Case Management System API (Node.js / Express API on AWS ECS)
- Compliance Reporting Worker (AWS Lambda in Python)
- Amazon DynamoDB
- Amazon SQS / Amazon Kinesis
- Amazon S3 with Object Lock
- AWS KMS
- Amazon CloudWatch

## Relationships
- Case Management System Frontend -> Amazon API Gateway: HTTPS / REST API
- Amazon API Gateway -> Real-Time Scoring Engine: Internal VPC routing
- Real-Time Scoring Engine -> Amazon DynamoDB: Persists authorization inputs and decision logs [AWS SDK / HTTPS]
- Compliance Reporting Worker -> Amazon S3: Reads daily Parquet audit files [AWS SDK / S3 GetObject]
- Compliance Reporting Worker -> AWS KMS: Generates asymmetric cryptographic signatures (`ECC_NIST_P256`) [AWS KMS Sign API]
- Compliance Reporting Worker -> Amazon S3 with Object Lock: Stores signed daily compliance digests with 7-year retention tags [HTTPS / PutObject]
- Compliance Reporting Worker -> Amazon CloudWatch: Emits operational metrics and logs [AWS SDK / HTTPS]

## Technology Stack
- AWS Lambda (Python 3.11): Serverless execution for cost-effective batch compliance reporting under budget constraints.
- Amazon S3 with Object Lock: Implements tamper-evident, unalterable 7-year storage for regulatory audit logs.
- AWS KMS: Provides asymmetric cryptography (`ECC_NIST_P256`) for cryptographically signing compliance digests securely.
- Amazon DynamoDB & Kinesis Firehose: Streams and persists high-throughput payment decision logs into flat Parquet files.
- Terraform / AWS CDK: Infrastructure-as-Code for reproducible deployments and prevention of configuration drift.

## Rationale
The serverless, event-driven AWS architecture keeps operational overhead minimal for a three-engineer team while easily scaling to handle high-volume transaction logging. Strict IAM boundaries, KMS asymmetric signing, and S3 Object Lock natively satisfy the stringent PCI-DSS Level 1 security and 7-year tamper-evident auditability requirements within the fixed financial budget.