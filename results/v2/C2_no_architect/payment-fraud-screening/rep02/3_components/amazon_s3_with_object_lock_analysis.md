## Overview
The system screens card-not-present payment authorizations in real-time for fraud and provides case management for analysts. It operates on AWS within a 25,000 EUR monthly budget, ensuring PCI-DSS Level 1 compliance and 7-year auditability.

## Key Elements
- Cardholder / End Customer
- Fraud Operations Analyst & Risk Manager
- AWS Application Load Balancer (ALB)
- Scoring Container & Case Management Container (AWS ECS Fargate)
- Database (Amazon Aurora Serverless)
- Audit Storage (Amazon S3 with Object Lock)
- Security & Access (AWS KMS, AWS IAM Identity Center)

## Relationships
- Cardholder -> AWS ALB: Submits payment authorization requests [HTTPS / TLS 1.3]
- AWS ALB -> Scoring Container: Routes scoring traffic [HTTP/2]
- Scoring Container -> Amazon S3 with Object Lock: Streams decision logs [AWS SDK / TLS 1.3 / VPC Gateway Endpoints]
- Scoring Container -> Amazon Aurora Serverless: Reads fraud rules and models [PostgreSQL Protocol / TLS]
- Fraud Operations Analyst -> AWS ALB: Reviews flagged cases [HTTPS]

## Technology Stack
- AWS ECS Fargate: Runs scoring and case management containers with minimal operational overhead for a 3-engineer team.
- Amazon S3 with Object Lock: Enforces 7-year tamper-evident audit storage in Compliance Mode.
- AWS KMS: Provides customer-managed encryption keys for data protection.
- Amazon Aurora Serverless: Scales relational database capacity dynamically to fit the 25,000 EUR monthly budget.
- AWS IAM Identity Center: Secures least-privilege role access for internal auditors and analysts.

## Rationale
This architecture uses serverless and managed AWS services to minimize operational burden for a three-engineer team while meeting strict P99 latency and PCI-DSS requirements. S3 Object Lock and KMS guarantee tamper-evident 7-year auditability within fixed cost constraints.