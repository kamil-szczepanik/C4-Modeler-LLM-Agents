## Overview
The system is a real-time payment fraud screening platform hosted on AWS in `eu-west-1` that evaluates card-not-present payment authorizations and manages analyst reviews. It ensures PCI-DSS Level 1 compliance and sub-50ms P99 decision latency while operating within a strict 25,000 EUR monthly budget.

## Key Elements
- **Users**: Fraud Analyst, Merchant Risk Manager, Compliance / Auditor Officer
- **External Systems**: Payment Gateway / Acquirer Systems, Card Networks / Tokenization Vaults, Core Banking / Ledger Systems
- **Containers**: AWS API Gateway, Real-Time Scoring Engine (ECS Fargate), Case Management Backend (ECS Fargate)
- **Data Stores & Brokers**: Amazon Aurora PostgreSQL, Amazon S3, Amazon ElastiCache (Redis), Amazon SQS

## Relationships
- **Payment Gateway** --(HTTPS/REST)--> **AWS API Gateway**
- **AWS API Gateway** --(HTTP/gRPC with mTLS)--> **Real-Time Scoring Engine**
- **Real-Time Scoring Engine** --(Redis Protocol)--> **Amazon ElastiCache (Redis)**
- **Real-Time Scoring Engine & Case Management** --(AWS SDK/SQS API)--> **Amazon SQS**
- **Case Management Backend** --(HTTPS with mTLS)--> **Amazon Aurora PostgreSQL**

## Technology Stack
- **AWS ECS Fargate**: Container orchestration for low-overhead, zero-downtime blue/green deployments.
- **Go / Java**: High-performance languages for the Real-Time Scoring Engine to meet the <50ms P99 latency SLA.
- **Amazon ElastiCache (Redis)**: In-memory feature store for rapid fraud rule evaluation.
- **Amazon Aurora PostgreSQL & Amazon S3**: Secure relational storage with cryptographic HMAC-SHA256 audit chaining and WORM storage.
- **AWS SQS**: Lightweight, managed asynchronous event messaging to fit within the 3-engineer operational capacity.

## Rationale
This architecture uses serverless and managed AWS services (ECS Fargate, SQS, ElastiCache) to meet strict sub-50ms latency and high-availability demands while minimizing operational overhead for a three-engineer team. Security controls, encryption, and tamper-evident audit logs ensure PCI-DSS Level 1 compliance within budget.