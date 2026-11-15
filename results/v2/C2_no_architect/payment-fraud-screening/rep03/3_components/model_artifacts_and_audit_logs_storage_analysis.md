## Overview
[Real-Time Payment Fraud Screening System screens card-not-present payment authorizations to detect fraud and manage reviews. It ensures PCI-DSS Level 1 compliance and 7-year auditability within a 25,000 EUR monthly budget on AWS eu-west-1.]

## Key Elements
- Fraud Analyst, Risk Manager / Data Scientist, Compliance & Audit Officer
- Payment Gateway / Processing Engine
- Amazon API Gateway and Application Load Balancer (ALB)
- Scoring Engine (AWS ECS Fargate)
- Case Management UI & Backend (AWS ECS Fargate)
- Serverless Tasks (AWS Lambda)
- Model Artifacts and Audit Logs Storage (Amazon S3)
- Ledger Database (AWS QLDB)
- Security and Management Services (AWS IAM, AWS Secrets Manager, AWS KMS, AWS CodePipeline, AWS CloudWatch & X-Ray)

## Relationships
- Scoring Engine -> Model Artifacts and Audit Logs Storage: Downloads cryptographically verified ML model artifacts [TLS 1.3]
- Scoring Engine -> Model Artifacts and Audit Logs Storage: Persists decision logs and inputs into WORM storage via Amazon Kinesis Data Firehose [AWS KMS Encryption]
- Risk Managers / Data Scientists -> Model Artifacts and Audit Logs Storage: Deploys model artifacts [AWS CodePipeline] and queries historical logs [Amazon Athena]

## Technology Stack
- AWS ECS Fargate: Provides scalable, containerized execution for scoring and case management engines within budget.
- Amazon S3 with Object Lock: Delivers WORM storage for 7-year tamper-evident audit logs and model artifacts.
- Amazon Kinesis Data Firehose: Batches and buffers high-throughput decision logs to prevent S3 latency and throttling.
- Amazon Athena and Lake Formation: Enables secure, read-only analytics queries over S3 data for data scientists with column-level controls.
- AWS KMS: Encrypts data at rest using Customer Managed Keys with automated rotation and Cross-Region Replication support.

## Rationale
[The architecture combines serverless containers and immutable cloud storage to achieve sub-50ms decision latencies at scale. It rigorously enforces PCI-DSS compliance and 7-year auditability while respecting strict budget and team constraints.]