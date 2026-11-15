## Overview
[A real-time payment fraud screening system that evaluates card-not-present transactions for a mid-size payment processor, providing instant authorization decisions and case management for fraud analysts while ensuring strict regulatory compliance.]

## Key Elements
- Payment Gateway / Acquirer
- Fraud Analysts
- Compliance Auditors
- Card Schemes / External Credit Bureaus
- AWS API Gateway
- AWS Application Load Balancer (ALB)
- AWS Fargate (Scoring Engine & Case Management Containers)
- Amazon DynamoDB
- Amazon S3 with Object Lock
- AWS Secrets Manager
- AWS Signer

## Relationships
- Payment Gateway to AWS API Gateway via gRPC / TLS 1.3 (mTLS) for authorization requests
- Fraud Analysts to ALB via HTTPS/Browser for Case Management UI
- Fargate containers to Amazon DynamoDB via AWS PrivateLink for transaction state
- Fargate containers to Amazon S3 via AWS SDK for decision and audit logs
- Fargate containers to External Credit Bureaus via HTTPS/REST for data enrichment
- System to Amazon S3 Object Lock via AWS SDK for 7-year tamper-evident audit logs

## Technology Stack
- AWS Fargate: Selected over AWS Lambda to eliminate cold starts and guarantee sub-50ms P99 latency
- Amazon DynamoDB: Chosen for low-latency state management and predictable scaling
- Amazon S3 with Object Lock: Implemented to satisfy immutable 7-year auditability constraints
- AWS Signer: Utilized for cryptographic verification of zero-downtime model and rule updates
- AWS Secrets Manager: Used for secure credential management and automated rotation

## Rationale
[This architecture leverages managed serverless container infrastructure on AWS to meet high throughput and sub-50ms latency constraints while strictly bounding PCI-DSS scope. It maintains high availability, automated zero-downtime model updates, and immutable audit logs within a fixed €25,000 monthly budget operated by a three-person engineering team.]