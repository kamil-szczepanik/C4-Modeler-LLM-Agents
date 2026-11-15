## Overview
The Real-Time Payment Fraud Screening system evaluates card-not-present payment authorizations for a mid-size payment processor to prevent fraud while enabling manual case reviews. It operates within AWS eu-west-1, adhering strictly to PCI-DSS Level 1 compliance and a 25,000 EUR monthly budget.

## Key Elements
- Payment Gateway / Core Processing Platform
- Real-Time Payment Fraud Screening System (AWS ECS on Fargate, API Gateway)
- Fraud Analysts & Risk Operations
- Compliance & Audit Officer
- Card Networks / Tokenization Service
- AWS KMS & Secrets Manager
- Corporate Identity Provider (OIDC/SAML)

## Relationships
- Payment Gateway -> Fraud Screening System: Synchronous API requests over HTTPS/mTLS (REST/gRPC) for sub-50ms scoring (R-01, R-04)
- Fraud Analysts & Compliance Officers -> Fraud Screening System: Secure HTTPS via OIDC/SAML for case reviews and audit logs (R-02, R-06)
- Fraud Screening System -> Tokenization Service: Outbound API over HTTPS for token resolution and verification (R-05)
- Fraud Screening System -> AWS KMS: Internal AWS API calls with local data-key caching for encryption and cryptographic hashing (R-06)

## Technology Stack
- AWS ECS on Fargate: Chosen for zero-cluster-management overhead to support a 3-person engineering team.
- AWS KMS & AWS Encryption SDK: Utilized for envelope encryption, key rotation, and caching data-keys locally to maintain sub-50ms latency at 3,000 TPS.
- Amazon S3 with Object Lock and Glacier: Implemented for write-once-read-many (WORM) tamper-evident audit logs retained for 7 years.
- AWS CloudWatch and X-Ray: Standardized for structured logging and distributed tracing to monitor P99 latency within budget.

## Rationale
This serverless-container architecture meets strict PCI-DSS Level 1 security and 7-year auditability mandates without exceeding the 25,000 EUR monthly infrastructure budget. Utilizing managed AWS services minimizes operational toil for the three-engineer team while guaranteeing the sub-50ms P99 latency required at 3,000 transactions per second.