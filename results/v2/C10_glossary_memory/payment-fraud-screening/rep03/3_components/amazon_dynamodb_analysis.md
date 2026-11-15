## Overview
[The system provides real-time fraud screening for card-not-present payment authorizations, enabling automated risk decisions and analyst reviews. It ensures PCI-DSS Level 1 compliance while maintaining sub-50ms latency under high throughput.]

## Key Elements
- Cardholders / Merchants
- Fraud Analysts & Risk Managers
- Payment Gateway / Acquirer
- AWS Application Load Balancer (ALB)
- Scoring Engine (Java, Spring Boot, gRPC)
- Case Management Service (Node.js, React)
- Amazon DynamoDB
- AWS S3 Object Lock
- AWS Cognito
- AWS ECS on Fargate

## Relationships
- Payment Gateway / Acquirer -> AWS Application Load Balancer (ALB) (gRPC/HTTPS over mTLS)
- Fraud Analysts & Risk Managers -> AWS Cognito (OAuth2/OIDC)
- Fraud Analysts & Risk Managers -> Case Management Service (HTTPS, TLS 1.3)
- AWS Application Load Balancer (ALB) -> Scoring Engine (gRPC/HTTPS)
- AWS Application Load Balancer (ALB) -> Case Management Service (HTTPS)
- Scoring Engine -> Amazon DynamoDB (AWS SDK / HTTPS over AWS PrivateLink)
- Scoring Engine -> AWS S3 Object Lock (AWS API)

## Technology Stack
- AWS ECS on Fargate: Serverless container orchestration for zero infrastructure management by a three-engineer team.
- Amazon DynamoDB: Low-latency NoSQL feature store providing sub-10ms lookups via On-Demand billing.
- AWS PrivateLink: Encrypted network isolation ensuring database traffic never traverses the public internet.
- AWS S3 Object Lock: Tamper-evident 7-year audit storage replacing QLDB to reduce operational overhead.
- AWS Cognito: Managed identity provider handling OAuth2/OIDC and MFA securely.

## Rationale
[This architecture utilizes serverless and managed AWS services to satisfy strict PCI-DSS compliance and 7-year auditability constraints within a 25,000 EUR monthly budget. It empowers a three-engineer team to operate a high-throughput, low-latency financial system with minimal operational overhead.]