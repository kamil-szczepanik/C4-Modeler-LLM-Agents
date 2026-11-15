## Overview
[The system is a real-time payment fraud screening platform that evaluates card-not-present transactions for a mid-size payment processor and provides case management for fraud analysts. Its core purpose is to screen authorizations in real time while ensuring strict compliance, auditability, and uninterrupted checkout flows.]

## Key Elements
- Cardholder / End Customer
- Fraud Analyst
- Risk / Fraud Manager
- AWS API Gateway / ALB
- Scoring Engine (AWS ECS Fargate)
- Case Management API (AWS ECS Fargate)
- Rule & Model Registry (Amazon S3)
- Amazon DynamoDB
- Amazon Kinesis Data Streams & AWS S3 Firehose
- WORM Compliance Storage (Amazon S3 with Object Lock)
- External Identity Provider (IdP) & Tokenization Vault

## Relationships
- Cardholder to AWS API Gateway via HTTPS/JSON
- API Gateway to Scoring Engine via mTLS / gRPC
- Scoring Engine to Amazon DynamoDB and Amazon Kinesis Data Streams via AWS SDK
- Scoring Engine to Amazon S3 (Rule & Model Registry) via HTTPS
- Fraud Analyst to Case Management API via HTTPS/OAuth2
- Scoring Engine and Case Management to WORM Compliance Storage via S3 Firehose

## Technology Stack
- AWS ECS Fargate: Provides container orchestration without Kubernetes operational overhead to fit the 3-person team limit and €25k budget.
- Go or Rust: Implements the low-latency Scoring Engine to guarantee <50ms P99 decision latency.
- Amazon DynamoDB: Delivers low-latency storage for feature stores and case data.
- Amazon Kinesis Data Streams: Handles high-throughput, durable audit log streaming.
- Amazon S3 Object Lock: Ensures tamper-evident WORM compliance storage for 7-year audit retention.
- AWS KMS: Implements envelope encryption, secret management, and cryptographic rule artifact signatures.

## Rationale
[This architecture uses managed AWS services and local in-memory caching to achieve ultra-low latency and PCI-DSS compliance within tight operational constraints. It minimizes infrastructure complexity to support a three-engineer team within a 25,000 EUR monthly budget.]