## Overview
[System screens card-not-present payment authorizations for fraud in real-time and provides case management for analysts. Core purpose is scoring transactions to approve, decline, or review them under strict PCI-DSS Level 1 compliance.]

## Key Elements
- Fraud Analysts and Risk Operations Managers (Users)
- API Gateway & Fallback Layer (Amazon API Gateway)
- Real-Time Scoring Service (Go, AWS ECS Fargate)
- Case Management Backend (Node.js/TypeScript, AWS ECS Fargate)
- Feature Cache (Amazon DynamoDB)
- Audit and Case Data Store (Amazon Aurora PostgreSQL)
- Messaging & Event Bus (Amazon SNS and Amazon SQS with FIFO/DLQ)
- Audit Storage (Amazon S3 with Object Lock Compliance Mode)

## Relationships
- Payment Gateway / Acquirer Systems -> API Gateway & Fallback Layer: Sends authorization requests [HTTPS / REST over TLS 1.3]
- API Gateway & Fallback Layer -> Real-Time Scoring Service: Forwards authorization requests [gRPC / TLS 1.3]
- Real-Time Scoring Service -> Feature Cache: Queries account velocity and risk features [AWS SDK / TLS 1.3]
- Real-Time Scoring Service -> Audit Event Publisher (SNS): Asynchronously publishes decision payloads [HTTPS / AWS SigV4]
- Audit Event Publisher (SNS) -> Audit Buffer Queue (SQS): Delivers event copies [SQS Subscriptions]
- Audit Buffer Queue (SQS) -> Audit Storage (S3): Batches immutable logs [AWS Lambda / S3 API]
- Case Management Backend -> Audit Event Publisher (SNS): Publishes case review events [HTTPS / AWS SigV4]

## Technology Stack
- AWS (eu-west-1): Cloud provider meeting regional compliance and low latency targets.
- Go & Node.js on AWS ECS Fargate: Containerized runtimes balancing low-latency execution and maintainability.
- Amazon DynamoDB: Low-latency feature caching for sub-50ms scoring SLAs.
- Amazon Aurora PostgreSQL: Relational storage for audit and case data.
- Amazon SNS and SQS: Decoupled, serverless asynchronous messaging.
- Amazon S3 Object Lock: Tamper-evident 7-year audit log retention.

## Rationale
[This architecture satisfies the strict sub-50ms latency and 7-year auditability requirements while operating within a 25,000 EUR monthly budget. The serverless, decoupled design enables a three-person engineering team to maintain the system securely under PCI-DSS Level 1 constraints.]