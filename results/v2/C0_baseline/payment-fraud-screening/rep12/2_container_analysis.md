## Overview
Real-Time Payment Fraud Screening engine processing card-not-present transactions for a mid-size payment processor. It provides sub-50ms fraud scoring and case management review capabilities.

## Key Elements
* Fraud Analysts & Risk Managers (Users)
* Amazon API Gateway (Ingress & WAF)
* Real-Time Scoring Engine (Go microservice on AWS ECS EC2)
* Case Management System (React SPA on S3 + CloudFront, Node.js/Express API on ECS)
* Compliance Reporting Worker (AWS Lambda)
* Data & Storage: Amazon DynamoDB, Amazon S3 with Object Lock
* Messaging & Fallback: Amazon SQS / Amazon Kinesis, API Gateway Circuit Breakers
* Security & Observability: AWS KMS (CMK), AWS Secrets Manager, Amazon CloudWatch

## Relationships
* Users to Amazon API Gateway: HTTPS / TLS 1.3
* API Gateway to Real-Time Scoring Engine: Internal gRPC over mTLS
* Scoring Engine to Amazon DynamoDB: AWS SDK over TLS 1.3
* Scoring Engine to Amazon SQS / Kinesis: Asynchronous event publishing over TLS 1.3
* Compliance Reporting Worker to Amazon S3 Object Lock: HTTPS via AWS SDK

## Technology Stack
* AWS ECS on EC2: Provides predictable P99 latency (<50ms) and cost control within budget.
* Go: Chosen for high-throughput, low-latency microservice scoring.
* Amazon DynamoDB: Delivers sub-millisecond feature store and case data lookups.
* Amazon S3 with Object Lock: Ensures tamper-evident, 7-year immutable audit retention.
* AWS Lambda: Eliminates operational overhead for scheduled compliance reporting.
* AWS KMS & Secrets Manager: Secures card data, audit logs, and runtime credentials.

## Rationale
This architecture uses serverless components and managed AWS services to minimize operational toil for a 3-engineer team while respecting a €25k monthly budget. Dedicated ECS EC2 instances and Go microservices guarantee sub-50ms performance and strict PCI-DSS Level 1 compliance.