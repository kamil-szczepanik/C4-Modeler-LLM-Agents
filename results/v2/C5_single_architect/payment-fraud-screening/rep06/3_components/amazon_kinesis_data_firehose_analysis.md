## Overview
The Real-Time Payment Fraud Screening system screens card-not-present payment authorizations in real time to prevent fraud. It also provides case management for analysts to review suspicious transactions securely on AWS.

## Key Elements
* Fraud Analysts and Compliance Auditors (Users)
* Payment Gateway, Identity Provider, and Tokenization Service (External Systems)
* AWS API Gateway (REST)
* Scoring Engine (Go, AWS ECS Fargate)
* Case Management Backend (Node.js/Go, AWS ECS Fargate)
* Amazon DynamoDB and Amazon Aurora PostgreSQL
* Amazon Kinesis Data Firehose (Firehose Buffer Manager, Firehose Data Transformer via AWS Lambda, S3 Delivery Stream Writer)
* Amazon S3 Object Lock

## Relationships
* Payment Gateway -> AWS API Gateway: Sends payment authorization requests [HTTPS]
* Scoring Engine -> Amazon Kinesis Data Firehose: Sends audit logs [HTTPS / AWS SDK]
* Firehose Buffer Manager -> Firehose Data Transformer: Invokes record transformation [AWS Lambda API]
* S3 Delivery Stream Writer -> Amazon S3 Object Lock: Writes immutable log batches with SSE-KMS [AWS S3 API]
* Fraud Analysts -> AWS API Gateway: Accesses case management UI [HTTPS]

## Technology Stack
* AWS ECS Fargate: Runs containerized microservices without managing underlying servers, fitting a 3-engineer team.
* Amazon Kinesis Data Firehose with AWS Lambda: Batches and sanitizes audit logs natively before persistence.
* Amazon S3 Object Lock: Enforces WORM (Write Once, Read Many) storage for 7-year tamper-evident auditability.
* Amazon Aurora PostgreSQL and DynamoDB: Provides transactional and low-latency state management.

## Rationale
This serverless-leaning AWS architecture guarantees sub-50ms P99 latency while meeting strict PCI-DSS Level 1 compliance and 7-year auditability. Furthermore, managed services minimize operational overhead to suit a small three-engineer team within a 25,000 EUR monthly budget.