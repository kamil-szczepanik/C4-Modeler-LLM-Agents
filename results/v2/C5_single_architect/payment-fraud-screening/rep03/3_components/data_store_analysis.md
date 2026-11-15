## Overview
The Real-Time Payment Fraud Screening system screens card-not-present payment authorizations in real time and provides a case management interface for fraud analysts. It runs on AWS in the `eu-west-1` region to meet stringent PCI-DSS Level 1 and 7-year auditability requirements.

## Key Elements
- **Payment Switch / Core Processing & Merchant Gateway**: External systems initiating authorization requests.
- **Fraud Analysts**: Human users reviewing suspicious payments via case management.
- **API Gateway**: AWS API Gateway (REST/HTTP) ingress point.
- **Scoring Engine**: Go application hosted on AWS ECS Fargate with an embedded model runtime.
- **Case Management API**: Node.js/Python application on AWS ECS Fargate for analyst workflows.
- **Data Store (Amazon Aurora PostgreSQL)**: Composed of Transactional Database, Audit Ledger, Model & Feature Store Schema, and Connection Pooler (PgBouncer/Aurora Proxy).
- **Event Stream**: Amazon SQS.

## Relationships
- **Merchant Gateway -> API Gateway**: Submits payment authorizations via HTTPS/REST.
- **API Gateway -> Scoring Engine**: Forwards authorization payloads via gRPC/HTTP2.
- **Scoring Engine -> Connection Pooler**: Writes decisions and audit logs via TCP (PostgreSQL Wire Protocol).
- **Case Management API -> Connection Pooler**: Manages review cases via TCP (PostgreSQL Wire Protocol).
- **Scoring Engine -> Event Stream**: Publishes asynchronous audit events via AWS SDK/SQS.

## Technology Stack
- **AWS ECS Fargate**: Minimizes operational overhead for the 3-engineer team.
- **Amazon Aurora PostgreSQL**: Unifies transactional data, audit logs, and feature storage within budget.
- **PgBouncer / Aurora Proxy**: Prevents connection exhaustion under 3,000 TPS load.
- **Go**: Ensures P99 decision latency below 50 ms.

## Rationale
This architecture uses managed AWS services to remain within the 25,000 EUR monthly budget while supporting a 3-engineer team. Cryptographic hash-chaining in PostgreSQL satisfies 7-year tamper-evident auditability without specialized ledger costs.