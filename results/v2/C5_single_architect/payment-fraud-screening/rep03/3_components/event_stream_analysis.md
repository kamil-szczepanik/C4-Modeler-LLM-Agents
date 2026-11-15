## Overview
The Real-Time Payment Fraud Screening system evaluates card-not-present payment authorizations to detect and review fraud prior to approval. It ensures PCI-DSS Level 1 compliance, sub-50ms P99 latency at 3,000 TPS, and 7-year tamper-evident auditability within a fixed 25,000 EUR monthly AWS budget.

## Key Elements
- Fraud Analysts (Users)
- Payment Switch / Core Processing, Merchant / Payment Gateway, Identity Provider (IdP), Model Training Environment (External Systems)
- API Gateway (AWS API Gateway)
- Scoring Engine (Go, AWS ECS Fargate, Embedded Model Runtime)
- Case Management API (Node.js / Python, AWS ECS Fargate)
- Data Store (Amazon Aurora PostgreSQL)
- Event Stream (Amazon Kinesis Data Streams with Kinesis Data Firehose)
- Long-Term Audit Storage (Amazon S3)

## Relationships
- Merchant / Payment Gateway -> API Gateway: Submits payment authorization requests [HTTPS / REST]
- API Gateway -> Scoring Engine: Forwards authorization requests for real-time scoring [gRPC / Internal VPC]
- Scoring Engine -> Data Store: Reads rules/models and writes transaction logs [PostgreSQL Wire Protocol / TCP]
- Scoring Engine -> Event Stream: Publishes asynchronous decision events [AWS Kinesis SDK / HTTPS]
- Event Stream -> Amazon S3: Streams decision data via Kinesis Data Firehose for audit logging [AWS Internal HTTPS / IAM]
- Fraud Analysts -> Case Management API: Reviews suspicious payments and manages cases [HTTPS / REST]
- Case Management API -> Data Store: Reads and updates case data [PostgreSQL Wire Protocol / TCP]

## Technology Stack
- AWS (eu-west-1): Target cloud provider ensuring managed scalability within budget constraints
- Go: Used for the Scoring Engine to achieve low sub-50ms P99 latency at high throughput
- Node.js / Python: Used for the Case Management API to enable rapid feature delivery by a 3-engineer team
- Amazon Aurora PostgreSQL: Provides ACID compliance for relational case management and transaction data
- Amazon Kinesis Data Streams & Firehose: Provides partitioned event streaming and log replay capabilities for auditability and model updates

## Rationale
The architecture combines Go-based microservices on AWS ECS Fargate with Kinesis streaming to process 3,000 TPS under 50ms while maintaining strict audit trails. Serverless and managed AWS services minimize operational overhead, allowing a three-engineer team to operate the system securely and reliably within the 25,000 EUR budget.