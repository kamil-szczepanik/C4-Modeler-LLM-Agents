## Overview
[System screens card-not-present payment authorizations for fraud in real-time, providing case management and explainable audit trails for analysts. Designed for a mid-size payment processor under strict PCI-DSS Level 1 compliance.]

## Key Elements
- Fraud Analyst & Risk Manager / Data Scientist
- Merchant / Payment Gateway System
- Scoring Engine Container (AWS ECS on Fargate, gRPC, HTTPS, TLS 1.3)
- Case Management Container (AWS ECS on Fargate, REST, mTLS)
- AWS S3 with Object Lock (WORM)
- AWS KMS

## Relationships
- Merchant / Payment Gateway System -> Scoring Engine Container: Submits payment authorization requests [gRPC/HTTPS with TLS 1.3]
- Case Management Container -> Scoring Engine Container: Queries and manages case details [internal REST/mTLS APIs]
- Scoring Engine Container -> AWS S3 (WORM): Stores cryptographically signed decisions and immutable audit logs [AWS SDK / HTTPS]
- Scoring Engine Container -> AWS KMS: Verifies model signatures and manages data encryption keys [AWS SDK]

## Technology Stack
- AWS ECS on Fargate: Runs containers within a fixed budget while supporting autoscaling
- gRPC / TLS 1.3: Ensures low-latency, secure communication for real-time scoring (<50ms P99)
- AWS S3 with Object Lock: Guarantees 7-year tamper-evident storage for regulatory compliance
- AWS KMS: Handles cryptographic signing of decisions and field-level data encryption (R-05, R-06)
- GitHub Actions: Automates zero-downtime model packaging and deployment pipelines (R-03)

## Rationale
[This architecture balances sub-50ms P99 latency and high availability with strict PCI-DSS Level 1 compliance and 7-year tamper-evident auditability. Leveraging managed AWS services keeps operations sustainable for a three-engineer team within the 25,000 EUR monthly budget.]