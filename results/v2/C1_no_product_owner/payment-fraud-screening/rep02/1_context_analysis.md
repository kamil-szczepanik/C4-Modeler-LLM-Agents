## Overview
The Real-Time Payment Fraud Screening System screens card-not-present payment authorizations for fraud prior to approval and provides a case management interface for fraud analysts. It is operated by a 3-engineer team in AWS region `eu-west-1` within a 25,000 EUR/month budget while maintaining PCI-DSS Level 1 compliance.

## Key Elements
* **Payment Gateway / Acquirer Systems**: External system initiating payment authorization requests.
* **Fraud Screening System**: Core AWS-hosted distributed platform scoring requests and managing fraud cases.
* **Fraud Analysts**: Users reviewing suspicious transactions and updating rules.
* **Card Networks / Tokenization Vaults**: External system providing token resolution and cardholder data.
* **Audit / Compliance Archive**: External WORM storage retaining immutable decision logs for 7 years.
* **Identity Provider (IdP)**: External system managing analyst credentials and multi-factor authentication.

## Relationships
* **Payment Gateway -> Fraud Screening System**: Submits tokenized authorization requests via REST/gRPC over TLS 1.3 with a <50ms P99 SLA and fail-open circuit breaker.
* **Fraud Analysts -> Fraud Screening System**: Reviews cases and updates rules via HTTPS.
* **Fraud Analysts -> Identity Provider**: Authenticates using OIDC/OAuth 2.0 and FIDO2/WebAuthn MFA over HTTPS.
* **Fraud Screening System -> Audit / Compliance Archive**: Stores tamper-evident decision logs using AWS S3 Object Lock.

## Technology Stack
* **Compute & API**: AWS Lambda and API Gateway for serverless, auto-scaled, low-maintenance execution meeting the P99 latency SLA.
* **Storage**: AWS DynamoDB for low-latency operational data and AWS S3 Object Lock for immutable 7-year audit compliance.
* **Security & Auth**: AWS IAM, Cognito, KMS, and AWS Secrets Manager for least-privilege access, cryptographic model verification, and credential management.
* **Observability & CI/CD**: AWS X-Ray and CloudWatch for managed distributed tracing; Terraform and AWS CodePipeline for GitOps-driven zero-downtime deployments.

## Rationale
Serverless and managed AWS services eliminate infrastructure maintenance overhead, enabling a 3-engineer team to reliably operate a high-throughput, low-latency system within a fixed budget. Strict tokenization boundaries, automated immutable archiving, and cryptographic verification ensure full PCI-DSS Level 1 compliance and 7-year auditability.