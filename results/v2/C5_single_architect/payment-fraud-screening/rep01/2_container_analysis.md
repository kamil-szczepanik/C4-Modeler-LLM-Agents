## Overview
The Real-Time Payment Fraud Screening system evaluates card-not-present payment authorizations for fraud within strict latency bounds and provides a case management workflow for fraud analysts. It operates on AWS (`eu-west-1`) while maintaining PCI-DSS Level 1 compliance and a 7-year tamper-evident audit trail.

## Key Elements
- **Payment Gateway / Acquirer**: External system submitting authorization requests.
- **Tokenization / Vault Provider**: External system handling secure card data storage and tokenization.
- **Payment Analysts**: Users reviewing suspicious transactions via the UI.
- **API Gateway / Ingestion Service**: Go-based container handling incoming requests via HTTPS/gRPC.
- **Fraud Scoring Engine**: Rust-based container executing fraud rules and models.
- **Case Management Backend**: Node.js/Java container managing analyst review workflows.
- **Fraud Analyst UI**: React Single Page Application hosted on AWS S3 + CloudFront.
- **Audit & Decision Store**: PostgreSQL on AWS RDS providing tamper-evident storage.
- **AWS SQS / SNS**: Serverless messaging service for asynchronous audit logging and case routing.

## Relationships
- **Payment Gateway** sends authorization requests to **API Gateway** via HTTPS/gRPC.
- **API Gateway** invokes **Fraud Scoring Engine** via internal gRPC/REST and publishes events to **AWS SQS / SNS**.
- **Fraud Scoring Engine** reads/writes tamper-evident decision logs to **Audit & Decision Store** (PostgreSQL).
- **Fraud Analyst UI** communicates via HTTPS/REST with **Case Management Backend**.
- **Case Management Backend** interacts with **Audit & Decision Store** and consumes queue messages from **AWS SQS / SNS**.

## Technology Stack
- **Go**: Used for the API Gateway to ensure high-throughput request ingestion.
- **Rust**: Used for the Fraud Scoring Engine to guarantee predictable sub-50ms P99 latency without garbage collection pauses.
- **Node.js/Java**: Used for the Case Management Backend.
- **React**: Used for the Fraud Analyst UI, hosted on **AWS S3 + CloudFront**.
- **Amazon RDS (PostgreSQL)**: Selected for the Audit & Decision Store with encryption and WORM storage for 7-year compliance (R-06).
- **Amazon SQS / SNS**: Selected over MSK for serverless, low-overhead event streaming within the 3-engineer and budget constraints.
- **AWS ECS / Fargate**: Container orchestration platform for backend services.

## Rationale
This architecture uses serverless and fully managed AWS services to minimize operational overhead for a three-engineer team within a strict budget. Performance and compliance requirements are met through low-latency Rust services, secure tokenization, and immutable audit logs.