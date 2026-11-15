## Overview
[The Real-Time Payment Fraud Screening system processes card-not-present authorizations for a mid-size payment processor to detect fraud in real time while providing a secure case management interface for analysts. It operates within AWS eu-west-1 under strict PCI-DSS Level 1 compliance, maintaining high availability and a 7-year immutable audit trail.]

## Key Elements
* Payment Processor Systems (External API Consumer)
* Fraud Analyst & Risk/Compliance Officer (Internal Users)
* Identity Provider (AWS IAM / OIDC)
* Real-Time Payment Fraud Screening Software System (AWS ECS/Lambda, DynamoDB, Kafka)
* Model Registry / Feature Store (AWS SageMaker / S3 with AWS Signer)
* Immutable Audit Storage (AWS S3 Object Lock with AWS KMS CMK)

## Relationships
* Payment Processor Systems -> Real-Time Payment Fraud Screening System: HTTPS / gRPC (Synchronous authorization scoring at 3,000 TPS)
* Fraud Analysts -> Real-Time Payment Fraud Screening System: HTTPS (Secure browser access for case management and review)
* Real-Time Payment Fraud Screening System -> Model Registry: HTTPS / S3 API (Zero-downtime dynamic rule and model fetching)
* Real-Time Payment Fraud Screening System -> Immutable Audit Storage: AWS SDK / S3 API (WORM-compliant decision logging)
* Users -> Identity Provider: HTTPS / OpenID Connect (Enterprise SSO and hardware-token MFA)

## Technology Stack
* AWS ECS / Lambda: Container and serverless compute chosen for cost efficiency within the €25k monthly budget and operational simplicity for a 3-person team.
* AWS DynamoDB & Kafka: Low-latency data storage and event streaming to maintain <50ms P99 decision latency.
* AWS SageMaker & S3: Machine learning and feature store infrastructure enabling zero-downtime model and rule updates.
* AWS S3 Object Lock & KMS: Tamper-evident, WORM-compliant storage meeting the 7-year regulatory audit mandate.
* AWS Signer: Cryptographic code-signing for dynamic model artifacts to prevent supply-chain poisoning.

## Rationale
[This architecture satisfies strict PCI-DSS Level 1 security and 7-year auditability requirements using robust AWS managed services while staying within a 25,000 EUR monthly budget. It leverages a 3-person engineering team efficiently through serverless and managed components, and ensures resilient, low-latency performance via fail-open integration policies.]