## Overview
The Real-Time Payment Fraud Screening system screens card-not-present payment authorizations for fraud in under 50 milliseconds while providing robust case management for fraud analysts. It operates on AWS within a strict €25,000 monthly budget, maintaining PCI-DSS Level 1 compliance and 7-year tamper-evident auditability.

## Key Elements
- **Users**: Fraud Analysts
- **External Systems**: Payment Gateway / Core Ledger, Identity Provider / IdP, Compliance Archive / AWS S3 Object Lock
- **Containers**: API Gateway / Envoy, Fraud Scoring Engine, Case Management Backend, Model & Rule Registry Service, Analyst UI, Asynchronous Audit Worker, Redis Cluster / Amazon ElastiCache, PostgreSQL / Amazon Aurora, Amazon SQS / SNS, AWS Secrets Manager / Parameter Store
- **Asynchronous Audit Worker Components**: Event Consumer Component, Batch Processor Component, Audit Formatter Component, S3 Exporter Component, DLQ Handler Component

## Relationships
- **API Gateway / Envoy** -> **Fraud Scoring Engine**: Routes authorization requests [gRPC / TLS]
- **Fraud Scoring Engine** -> **Redis Cluster / Amazon ElastiCache**: Fetches rules and caches evaluation data [Redis Protocol / TCP]
- **Case Management Backend** -> **PostgreSQL / Amazon Aurora**: Persists analyst reviews and case data [JDBC / TLS]
- **Asynchronous Audit Worker** -> **AWS S3 Object Lock**: Writes tamper-evident audit logs [HTTPS]
- **Event Consumer Component** -> **Batch Processor Component**: Passes batched SQS messages [Internal Function Call]
- **Batch Processor Component** -> **Audit Formatter Component**: Delegates individual event formatting and hashing [Internal Function Call]
- **Batch Processor Component** -> **S3 Exporter Component**: Passes formatted and hashed audit batches [Internal Function Call]
- **S3 Exporter Component** -> **AWS S3 Object Lock**: Executes WORM-compliant storage operations [HTTPS / AWS SDK]
- **Audit Formatter Component** -> **DLQ Handler Component**: Routes unprocessable audit payloads on failure [Internal Function Call]
- **DLQ Handler Component** -> **Amazon SQS / SNS**: Forwards dead-letter audit events [HTTPS / AWS SDK]

## Technology Stack
- **AWS eu-west-1**: Selected as the target cloud provider and region for infrastructure hosting.
- **Go / AWS Lambda**: Powers the Asynchronous Audit Worker for zero-idle cost and low cold-start latency.
- **Java / Spring Boot**: Implements the Case Management Backend for enterprise service stability.
- **Python / FastAPI / S3**: Powers the Model & Rule Registry Service for seamless machine learning model updates.
- **React / AWS S3 / CloudFront**: Delivers the Analyst UI frontend with global edge caching.
- **Amazon Aurora (PostgreSQL)**: Provides managed, relational persistence for application state.
- **Amazon ElastiCache (Redis)**: Delivers sub-millisecond caching for rules and scoring context.
- **AWS S3 Object Lock**: Enforces WORM (Write Once, Read Many) compliance for 7-year audit requirements.

## Rationale
This architecture guarantees P99 decision latencies below 50 ms at 3,000 requests per second by utilizing in-memory caching and high-performance gRPC services. Serverless components and managed AWS infrastructure ensure full PCI-DSS compliance and 7-year tamper-evident audit logging while strictly respecting the €25,000 monthly budget.