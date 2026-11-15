## Overview
The Real-Time Payment Fraud Screening system screens card-not-present payment authorizations in real time to prevent fraud. It also provides case management tools for fraud analysts to review suspicious transactions.

## Key Elements
- Fraud Analyst (User)
- Payment Gateway / Core Processing Platform (External System)
- AWS API Gateway / ALB (Container)
- Fraud Scoring Engine (Container, Go/Rust on AWS ECS Fargate)
- Case Management Service (Container, Node.js/TypeScript on AWS ECS Fargate)
- Amazon S3 Immutable Vault (Container, Amazon S3 with Object Lock)
- Vault Ingestion Interceptor (Component, Go on AWS Lambda)
- S3 Object Lock Manager (Component, AWS S3 Configuration)
- Audit Verification Worker (Component, Python on AWS Lambda)
- Access Control Enforcer (Component, AWS IAM / S3 Bucket Policies)

## Relationships
- Case Management Service -> Amazon S3 Immutable Vault: Archives audit logs and case data [HTTPS / AWS SDK (SigV4)]
- Case Management Service -> Vault Ingestion Interceptor: Submits immutable audit logs and case artifacts [HTTPS / AWS SDK (SigV4)]
- Vault Ingestion Interceptor -> S3 Object Lock Manager: Stores objects with retention policies [S3 API]
- Audit Verification Worker -> S3 Object Lock Manager: Reads and verifies payload hashes [S3 API (Read-Only)]

## Technology Stack
- AWS S3 with Object Lock in Compliance Mode: Ensures 7-year tamper-evident WORM storage for PCI-DSS compliance.
- AWS Lambda (Go/Python): Provides serverless, isolated execution for ingestion and verification.
- AWS IAM / S3 Bucket Policies: Enforces strict least-privilege access control.

## Rationale
This architecture ensures strict PCI-DSS Level 1 compliance and meets the 7-year tamper-evident auditability constraint using immutable storage and serverless components. It operates efficiently within the 25,000 EUR monthly budget.