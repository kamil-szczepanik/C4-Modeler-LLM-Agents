## Overview
[The system is a real-time payment fraud screening engine that evaluates card-not-present transactions for a mid-size payment processor. Its core purpose is to score authorizations in under 50 milliseconds while routing suspicious cases to fraud analysts and maintaining PCI-DSS Level 1 compliance.]

## Key Elements
- Payment Gateway / Acquirer
- Fraud Screening Engine (Go / Rust, AWS ECS Fargate)
- Case Management API (AWS ECS Fargate)
- Rule & Model Registry (Amazon S3)
- Amazon DynamoDB
- Amazon Kinesis Data Streams & AWS S3 Firehose
- Tokenization Vault
- Identity Provider (IdP)
- WORM Compliance Storage (Amazon S3 Object Lock)

## Relationships
- Payment Gateway / Acquirer -> Fraud Screening Engine: Sends payment authorization requests [HTTPS / REST]
- Fraud Screening Engine -> Tokenization Vault: Tokenizes and retrieves card data [gRPC / HTTPS]
- Fraud Screening Engine -> Amazon DynamoDB: Reads/writes user profiles and case states [AWS SDK]
- Fraud Screening Engine -> Amazon Kinesis Data Streams: Streams audit logs [AWS SDK / HTTPS]
- Amazon Kinesis Data Streams -> Amazon S3 Firehose: Buffers and forwards records [AWS internal protocol]
- Amazon S3 Firehose -> WORM Compliance Storage: Persists immutable audit logs [AWS SDK / S3 API]
- Case Management API -> Amazon DynamoDB: Manages analyst review cases [AWS SDK]
- Fraud Analysts -> Case Management API: Reviews suspicious payments [HTTPS / Web]

## Technology Stack
- AWS ECS Fargate: Hosts containerized microservices without managing underlying servers, fitting the 3-engineer team constraint.
- Amazon Kinesis Data Streams & AWS S3 Firehose: Provides scalable real-time audit logging with built-in batching to control S3 storage costs.
- Amazon DynamoDB: Delivers predictable single-digit millisecond latency required for sub-50ms fraud decisions.
- Amazon S3 Object Lock: Ensures tamper-evident, 7-year regulatory audit retention required for PCI-DSS compliance.
- AWS PrivateLink: Secures internal transport of sensitive data across AWS components without traversing the public internet.

## Rationale
[This architecture strictly balances the 25,000 EUR monthly budget and 3-engineer operational limit through fully managed AWS serverless and container services. It guarantees sub-50ms performance and unbreakable PCI-DSS Level 1 auditability using isolated streaming and immutable storage.]