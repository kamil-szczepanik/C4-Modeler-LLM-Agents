## Overview
The system is a Real-Time Payment Fraud Screening Platform that screens card-not-present payment authorizations for fraud and manages analyst case reviews. It ensures high throughput, strict security, and regulatory compliance for mid-size payment processors.

## Key Elements
- Fraud Analyst & Risk Manager (Users)
- Payment Gateway / Acquirer, Corporate Identity Provider (IdP), Card Tokenization Provider, Notification Gateway (External Systems)
- API Gateway (AWS API Gateway - HTTP APIs)
- Scoring Engine Container (Go, ONNX runtime, Amazon ECS on AWS Fargate)
- Case Management Container (Next.js / Node.js, Amazon ECS on AWS Fargate)
- Data Stores & Messaging: Amazon RDS PostgreSQL, Amazon S3 (WORM Object Lock & Model Bucket), Amazon SQS / EventBridge, Amazon Kinesis / S3 Data Lake
- Analytics & Discovery: Amazon Athena, AWS Cloud Map

## Relationships
- Payment Gateway to API Gateway via mTLS
- API Gateway to Scoring Engine Container via gRPC over HTTP/2
- Scoring Engine Container to Amazon S3 (Model Bucket) via HTTPS with digital signature verification
- Case Management Container to Amazon RDS PostgreSQL via TLS
- Case Management Container to Amazon SQS / EventBridge via AWS SDK
- Athena to Amazon S3 WORM Bucket via SQL queries for audit reports

## Technology Stack
- AWS ECS on AWS Fargate: Chosen for zero-overhead container orchestration fitting a 3-engineer team and €25k budget.
- Go & ONNX Runtime: Selected for the Scoring Engine to achieve sub-10ms P99 latency at 3,000 TPS.
- Next.js (Node.js) & Amazon RDS PostgreSQL: Chosen for rapid Case Management UI development and relational case tracking.
- Amazon S3 with Object Lock & Athena: Implemented for tamper-evident, 7-year audit retention and cost-effective compliance reporting.

## Rationale
This architecture meets sub-50ms latency and high-throughput requirements using lightweight Go containers and Fargate while maintaining PCI-DSS Level 1 compliance. It operates securely within a €25,000 monthly budget managed by three engineers.