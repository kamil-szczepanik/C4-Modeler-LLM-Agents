## Overview
The Real-Time Payment Fraud Screening System evaluates card-not-present payment authorizations for fraud in under 50 milliseconds while providing case management for analysts. It operates within AWS eu-west-1, adhering to PCI-DSS Level 1 compliance and a 7-year tamper-evident audit mandate.

## Key Elements
* Payment Gateway / Core Ledger (External Actor)
* Fraud Analyst (External Actor)
* Card Schemes / Identity Providers (External Actors)
* Compliance / Auditor (External Actor)
* Ingress API Gateway & Tokenization Container
* Real-Time Scoring Engine Container
* Case Management Container
* S3 Object Lock Audit Storage

## Relationships
* Payment Gateway → Fraud Screening System via gRPC over TLS 1.3 (mTLS)
* Fraud Analyst → Fraud Screening System via HTTPS (OIDC/SAML)
* Fraud Screening System → Card Schemes / External APIs via HTTPS REST
* Compliance / Auditor → S3 Audit Storage via HTTPS / AWS IAM
* Internal Containers → Internal Containers via mTLS

## Technology Stack
* AWS ECS/Fargate (Container orchestration for low operational overhead with 3 engineers)
* AWS S3 with Object Lock in Compliance Mode (Tamper-evident 7-year audit log retention)
* AWS KMS Customer Managed Keys (Data-at-rest encryption for PCI-DSS compliance)
* AWS ECR & AWS Signer (Container vulnerability scanning and image signing)
* gRPC over TLS 1.3 (Sub-50ms P99 latency at 3,000 TPS)

## Rationale
Managed AWS services minimize operational toil for a three-engineer team while satisfying strict PCI-DSS Level 1 constraints. Aggressive data tiering and serverless architecture maintain costs below the €25,000 monthly budget.