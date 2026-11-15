## Overview
The Real-Time Payment Fraud Screening system processes card-not-present payment authorizations in real-time, executing fraud scoring and analyst case management for a mid-size payment processor. It ensures high availability, strict PCI-DSS compliance, and auditable 7-year tamper-evident decision logging.

## Key Elements
- Fraud Analyst, Risk Manager / Data Scientist, Merchant Support (Users)
- Merchant / Payment Gateway System (External System)
- Scoring Engine Container (CDE private subnet)
- Case Management Container (Isolated external subnet)
- AWS ECS on Fargate (Container Orchestration)
- Amazon S3 Glacier & AWS S3 Object Lock (Data Retention & Audit storage)
- AWS KMS & AWS QLDB (Security & Tamper-Evident Ledger)

## Relationships
- Merchant / Payment Gateway to Scoring Engine Container via gRPC/HTTPS with TLS 1.3
- Scoring Engine Container to AWS QLDB and S3 via AWS SDK (mTLS)
- Fraud Analyst to Case Management Container via HTTPS (OAuth 2.0 / OIDC JWT)
- Case Management Container to Scoring Engine via internal REST/mTLS APIs
- AWS CloudWatch to PagerDuty via Webhooks for real-time alerting

## Technology Stack
- AWS ECS on Fargate: Selected for lightweight container orchestration suited to a 3-engineer team within budget.
- AWS QLDB & S3 Object Lock: Ensures tamper-evident, WORM-compliant 7-year audit retention (R-06).
- AWS KMS: Provides AES-256 encryption at rest for tokenized card data (R-05).
- AWS Distro for OpenTelemetry (ADOT): Monitors P99 latency below 50 ms at 3,000 TPS.

## Rationale
This architecture fits the requirements by strictly isolating the Cardholder Data Environment to contain PCI-DSS scope while leveraging serverless Fargate to stay under the 25,000 EUR monthly budget. Automated fail-open mechanics with strict PagerDuty alerts guarantee low latency and high availability without compromising security.