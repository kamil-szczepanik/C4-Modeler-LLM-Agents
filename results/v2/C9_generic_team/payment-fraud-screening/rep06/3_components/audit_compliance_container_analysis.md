## Overview
The Real-Time Payment Fraud Screening system evaluates card-not-present payment authorizations for fraud within strict latency and compliance constraints. It securely processes transactions, manages analyst reviews, and maintains tamper-evident audit records.

## Key Elements
- Fraud Analysts (Users)
- Payment Gateway (External System)
- API Gateway / Payment Gateway Integration Container (AWS ECS with Fargate)
- Tokenization/Masking Proxy Container (AWS ECS with Fargate)
- Real-Time Scoring Engine Container (AWS ECS with Fargate)
- Case Management Container (AWS ECS with Fargate)
- Model & Rule Registry Service Container (AWS ECS with Fargate)
- Audit & Compliance Container (AWS ECS with Fargate)
- Amazon ElastiCache (Redis)
- Amazon Aurora
- Amazon SQS / SNS
- Amazon S3 Object Lock

## Relationships
- Payment Gateway -> API Gateway: Submits payment authorizations via HTTPS/TLS 1.3
- API Gateway -> Tokenization/Masking Proxy Container: Forwards raw card data for tokenization via gRPC
- Tokenization/Masking Proxy Container -> Real-Time Scoring Engine Container: Passes tokenized requests via gRPC
- Real-Time Scoring Engine Container -> Amazon ElastiCache (Redis): Fetches low-latency fraud features via Redis protocol
- Real-Time Scoring Engine Container -> Amazon Aurora: Retrieves scoring models and transaction history via PostgreSQL wire protocol
- Real-Time Scoring Engine Container -> Amazon SQS / SNS: Publishes transaction decisions and audit events
- Amazon SQS / SNS -> Audit & Compliance Container: Supplies decision payloads for compliance logging via AWS SDK
- Audit & Compliance Container -> Amazon S3 Object Lock: Writes tamper-evident logs with 7-year WORM retention via AWS SDK

## Technology Stack
- AWS ECS with Fargate: Container orchestration chosen for serverless operational simplicity suited for a 3-engineer team.
- Amazon S3 Object Lock: Implements Write-Once-Read-Many (WORM) storage to meet strict 7-year PCI-DSS auditability.
- Amazon SQS / SNS: Asynchronous message decoupling ensuring fault-tolerant, at-least-once event processing.
- Amazon ElastiCache (Redis): In-memory data store providing sub-millisecond feature lookups for P99 latency under 50 ms.
- Amazon Aurora: Relational database for durable transactional storage of rules, models, and case management data.

## Rationale
This architecture leverages managed serverless AWS services to minimize operational overhead for a three-engineer team while easily scaling to meet high-throughput demands. Strict encryption, tokenization, and S3 Object Lock ensure full PCI-DSS compliance and tamper-evident 7-year auditability within a fixed budget.