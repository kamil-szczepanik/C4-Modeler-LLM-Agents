## Overview
The Real-Time Payment Fraud Screening system screens card-not-present payment authorizations in real time and provides case management for fraud analysts. It operates on AWS to meet strict PCI-DSS compliance and 7-year auditability constraints.

## Key Elements
- Payment Gateway / Acquirer Systems
- AWS API Gateway (REST)
- Scoring Engine (Go, AWS ECS Fargate)
- Case Management Backend (Node.js/Go, AWS ECS Fargate)
- Amazon Aurora PostgreSQL (Components: Case Management Schema, Audit Log & Tamper-Evident Ledger, Model Registry Schema)
- Amazon DynamoDB
- Amazon S3 with Object Lock
- Amazon Kinesis Data Firehose

## Relationships
- Payment Gateway -> AWS API Gateway: Submits authorization requests via [HTTPS / REST]
- AWS API Gateway -> Scoring Engine: Invokes real-time fraud checks via [gRPC / HTTP/2]
- Scoring Engine -> Model Registry Schema: Polls active rule and model metadata via [TCP / PostgreSQL Wire Protocol]
- Case Management Backend -> Case Management Schema: Reads and writes case data via [TCP / PostgreSQL Wire Protocol]
- Case Management Backend -> Audit Log & Ledger: Appends immutable compliance logs via [TCP / PostgreSQL Wire Protocol]
- Scoring Engine -> Amazon S3 Object Lock: Writes tamper-evident decision logs via [HTTPS / AWS SDK]

## Technology Stack
- AWS ECS Fargate: Container orchestration chosen for low operational overhead with a 3-engineer team.
- Amazon Aurora PostgreSQL: Relational database utilizing `pgaudit` and Row-Level Security for PCI-DSS compliance and auditability.
- Amazon S3 with Object Lock: WORM storage for immutable 7-year audit retention.
- Go: High-performance language for the Scoring Engine to achieve <50ms P99 latency.

## Rationale
This architecture utilizes serverless and managed AWS services to remain within the 25,000 EUR monthly budget while supporting a 3-engineer team. Native database features like `pgaudit` and S3 Object Lock fulfill stringent PCI-DSS and 7-year auditability mandates without excessive operational complexity.