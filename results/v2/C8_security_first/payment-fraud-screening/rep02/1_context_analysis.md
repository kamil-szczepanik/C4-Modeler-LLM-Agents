## Overview
[The Real-Time Payment Fraud Screening System evaluates card-not-present payment authorizations for fraud before approval and provides case management for suspicious transactions. Its core purpose is to deliver sub-50ms fraud decisions at 3,000 TPS while maintaining PCI-DSS Level 1 compliance and 7-year auditability.]

## Key Elements
* Payment Gateway / Acquirer
* Cardholder / Customer
* Fraud Analyst & Risk Manager
* Real-Time Payment Fraud Screening System
* Payment Network / Card Brands (Visa/Mastercard)
* Core Ledger / Compliance Archive

## Relationships
* Payment Gateway to Screening System via gRPC/REST over mTLS
* Fraud Analyst and Risk Manager to Screening System via HTTPS and OAuth 2.0 / OIDC
* Screening System to Core Ledger / Compliance Archive via AWS S3 Object Lock / QLDB

## Technology Stack
* AWS Fargate / ECS: Chosen for container orchestration to reduce operational overhead for a 3-engineer team
* Go / Rust: Selected for stateless microservices to ensure sub-50ms P99 latency at 3,000 TPS
* AWS S3 Object Lock / QLDB: Implemented for immutable, tamper-evident 7-year audit retention
* AWS KMS: Utilized for tokenization and cardholder data encryption at rest

## Rationale
[This architecture uses serverless containers and managed AWS services to minimize infrastructure complexity, fitting the €25k monthly budget and 3-engineer operational limit. Strict adherence to mTLS, tokenization, and WORM storage satisfies PCI-DSS Level 1 and 7-year auditability constraints.]