## Overview
The Real-Time Payment Fraud Screening system evaluates card-not-present payment authorizations to approve, decline, or flag transactions for review while providing analyst case management. It ensures PCI-DSS Level 1 compliance, sub-50ms P99 latency at 3,000 TPS, and 7-year tamper-evident auditability within a fixed AWS budget.

## Key Elements
- Fraud Analysts, Regulatory / Compliance Auditors
- Payment Gateway / Acquirer Systems, Identity Provider (IdP), External Tokenization/Vault Service
- AWS API Gateway (REST)
- Scoring Engine (Go, AWS ECS Fargate)
- Case Management Backend (Node.js/Go, AWS ECS Fargate)
- HTTP Handler / Router Component
- Rule Evaluator Component (In-memory AST)
- Model Scoring Component (Embedded ONNX Runtime / compiled decision trees)
- Audit Dispatcher Component (Worker pools)
- Amazon DynamoDB, Amazon Aurora PostgreSQL
- Amazon Kinesis Data Firehose, Amazon S3 with Object Lock

## Relationships
- Payment Gateway / Acquirer Systems -> AWS API Gateway: Inbound authorization requests [HTTPS/REST]
- AWS API Gateway -> Scoring Engine: Routes requests for scoring [HTTP/REST over TCP with connection pooling]
- Scoring Engine -> Amazon Aurora PostgreSQL / Amazon DynamoDB: Reads compiled rule definitions and model state [AWS SDK / `pgx` pool over TLS]
- Scoring Engine -> Amazon Kinesis Data Firehose: Sends asynchronous audit logs [HTTPS]
- Scoring Engine -> Amazon S3 Object Lock: Stores tamper-evident immutable audit trails [AWS SDK over HTTPS]

## Technology Stack
- Go (`net/http`): Selected for high-concurrency and low-latency execution in the Scoring Engine.
- ONNX Runtime / Compiled Decision Trees: Embedded in-memory model scoring to meet the <50ms P99 latency requirement.
- Amazon DynamoDB & Amazon Aurora PostgreSQL: Used for low-latency rule/model state retrieval and relational caching.
- Amazon Kinesis Data Firehose & Amazon S3 Object Lock: Implements WORM (Write Once, Read Many) storage to satisfy 7-year regulatory compliance.
- AWS ECS Fargate: Provides managed container orchestration within the 25,000 EUR monthly budget.

## Rationale
This architecture uses Go-based microservices with in-memory evaluation and connection pooling on AWS ECS Fargate to achieve sub-50ms latency at high throughput. Asynchronous audit dispatching and S3 Object Lock guarantee tamper-evident 7-year compliance without impacting real-time performance.