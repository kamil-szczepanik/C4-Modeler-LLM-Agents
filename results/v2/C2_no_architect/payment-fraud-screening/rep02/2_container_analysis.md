## Overview
[Real-Time Payment Fraud Screening screens card-not-present payment authorizations for a mid-size payment processor and enables analysts to review suspicious transactions.]
[It provides real-time scoring, auditability, and case management while maintaining PCI-DSS Level 1 compliance.]

## Key Elements
- Cardholder / End Customer
- Fraud Operations Analyst
- Risk Manager / Quant
- Fraud Ops Team Lead / Administrator
- Scoring Container (AWS ECS Fargate)
- Case Management Container (AWS ECS Fargate)
- Application Load Balancer
- Amazon Aurora Serverless
- Amazon S3 with Object Lock
- AWS KMS

## Relationships
- Cardholder submits payment authorizations via HTTPS/TLS 1.3 to Application Load Balancer
- Application Load Balancer routes traffic to Scoring Container via ECS service connect / mTLS
- Scoring Container queries Amazon Aurora Serverless for transaction context
- Scoring Container streams decision logs to Amazon S3 via AWS KMS
- Fraud Operations Analyst accesses Case Management Container via AWS IAM Identity Center and Application Load Balancer
- Case Management Container reads/writes case data in Amazon Aurora Serverless

## Technology Stack
- AWS ECS Fargate: Container orchestration to minimize operational overhead for a 3-engineer team within budget
- Amazon Aurora Serverless: Relational database scaling dynamically for case management and transaction data
- Amazon S3 with Object Lock: Tamper-evident 7-year audit log storage satisfying regulatory compliance
- AWS KMS: Customer-managed keys securing decision logs and data at rest
- AWS IAM Identity Center: Hardware-backed MFA authentication for analysts and risk managers
- AWS App Mesh / ECS Service Connect: Enforcing strict mTLS between containers

## Rationale
[This architecture utilizes managed AWS services to operate within a fixed €25,000 monthly budget and a 3-engineer team while satisfying PCI-DSS Level 1 compliance.]
[It separates high-throughput, low-latency scoring from human-in-the-loop case management to guarantee sub-50ms P99 latency at 3,000 TPS.]