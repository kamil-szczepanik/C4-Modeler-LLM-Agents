## Overview
[Real-Time Payment Fraud Screening system for processing card-not-present authorizations, providing low-latency scoring and secure case management for fraud analysts. The system ensures PCI-DSS Level 1 compliance, explainable audit trails, and strict cost and operational constraints.]

## Key Elements
- Fraud Scoring Service (Python, FastAPI, ONNX Runtime, Amazon ECS Fargate)
- Case Management API (Amazon ECS Fargate)
- Amazon SQS Standard Queue & Amazon SQS Dead-Letter Queue (DLQ)
- Audit Event Producer Interface & Audit Message Batcher (Boto3 SDK)
- AWS Lambda (Audit Processor)
- Amazon S3 Object Lock & S3 Model Registry (Amazon S3)
- Amazon Aurora PostgreSQL
- AWS Key Management Service (AWS KMS CMK)
- Amazon CloudWatch & Amazon SNS (Fraud Operations Alerting)

## Relationships
- Fraud Scoring Service -> Amazon SQS: Publishes batched audit events using SendMessageBatch via HTTPS with IAM SigV4 [AWS SDK/Boto3]
- Amazon SQS -> AWS Lambda: Delivers audit events via AWS internal event source mapping with 20s long polling
- Amazon SQS -> Amazon SQS DLQ: Forwards unprocessable messages after max retries [AWS SDK]
- Amazon SQS DLQ -> Fraud Operations Alerting: Triggers CloudWatch alarms for messages persisting over 1 hour [AWS CloudWatch Alarm]
- Amazon SQS -> AWS KMS: Encrypts/decrypts audit payloads using Customer Managed Keys [AWS Internal API]

## Technology Stack
- Amazon SQS & SQS DLQ: Asynchronous decoupling with 14-day retention and 60s visibility timeout for zero operational toil
- AWS KMS (CMK): Fully managed encryption to satisfy PCI-DSS Level 1 compliance without operational overhead
- AWS Lambda: Serverless event processing fitting within the 3-engineer team capacity and budget
- Python / FastAPI / ONNX Runtime: High-performance scoring engine meeting the P99 < 50ms latency constraint

## Rationale
[This architecture leverages fully managed AWS serverless services to maintain high availability and PCI-DSS compliance while operating within a €25,000 monthly budget. Decoupling scoring from auditing via SQS and Lambda guarantees performance targets and tamper-evident 7-year audit retention for a three-engineer team.]