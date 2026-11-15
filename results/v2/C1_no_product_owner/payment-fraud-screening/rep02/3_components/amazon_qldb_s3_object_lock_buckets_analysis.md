## Overview
The Real-Time Payment Fraud Screening system processes card-not-present payment authorizations to detect fraud within strict performance and compliance constraints. It screens transactions, manages review cases, and ensures tamper-evident auditability for financial regulators.

## Key Elements
- Fraud Scoring Engine (Go/Rust on Amazon ECS Fargate)
- Case Management Service (Node.js/Python on Amazon ECS Fargate)
- Transaction Ledger Component (Amazon QLDB)
- Evidence Archive Component (Amazon S3 with Object Lock)
- Audit Export & Verification Worker (AWS Lambda)
- Infrastructure Security & Storage (AWS KMS, Amazon CloudWatch, Amazon SQS)

## Relationships
- Fraud Scoring Engine -> Transaction Ledger Component: Appends decision journal [AWS SDK / QLDB Driver over TLS 1.3]
- Case Management Service -> Evidence Archive Component: Uploads case artifacts [AWS SDK over HTTPS]
- Audit Export & Verification Worker -> Transaction Ledger Component: Verifies hash chains [AWS SDK / QLDB Driver]
- Audit Export & Verification Worker -> Evidence Archive Component: Manages retention and exports [AWS SDK / S3 API]
- Audit Export & Verification Worker -> Amazon CloudWatch / Amazon SNS: Triggers alerts on verification failures [AWS SDK / HTTPS]

## Technology Stack
- Amazon ECS Fargate: Runs scoring and case management containers without server management, fitting the 3-engineer constraint.
- Amazon QLDB: Provides cryptographically verifiable immutability for decision journals.
- Amazon S3 Object Lock: Enforces Write-Once-Read-Many (WORM) compliance storage for 7 years.
- AWS KMS: Secures data encryption with customer-managed keys and annual rotation.
- AWS Lambda: Executes serverless audit verification and lifecycle management.

## Rationale
This architecture leverages managed AWS services to minimize operational overhead, matching the capacity of a three-engineer team. It guarantees strict PCI-DSS Level 1 compliance, sub-50ms P99 latency, and 7-year tamper-evident auditability within the €25,000 monthly budget.