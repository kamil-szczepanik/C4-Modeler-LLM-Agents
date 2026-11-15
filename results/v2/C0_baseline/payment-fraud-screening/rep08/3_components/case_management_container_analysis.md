## Overview
Real-Time Payment Fraud Screening screens card-not-present payment authorizations of a mid-size payment processor for fraud, empowering fraud analysts to review suspicious payments. The system operates on AWS in the eu-west-1 region while maintaining PCI-DSS Level 1 compliance.

## Key Elements
- Fraud Analysts & Risk Managers (Users)
- API Gateway & Routing Layer (AWS API Gateway / ALB)
- Case Management Container (Node.js/React SPA backend)
  - Case API Service (Node.js/Express)
  - Case Workflow Controller (Node.js)
  - Data Access Repository (TypeScript/Prisma)
  - Masking & Tokenization Service (Node.js utility)
- Aurora Serverless v2 (PostgreSQL)
- Audit & Event Store Container (Amazon DynamoDB & S3)
- Messaging Backbone (Amazon SQS / SNS)
- Model Storage & Management (Amazon S3 & AWS Secrets Manager)

## Relationships
- Fraud Analysts & Risk Managers -> Case API Service: Reviews cases and manages fraud workflow [HTTPS (OAuth2/OIDC, JSON)]
- Case API Service -> Masking & Tokenization Service: Strips/masks sensitive PAN data [In-process function call]
- Case API Service -> Data Access Repository: Reads/writes case state [Prisma Client over TCP/TLS 1.3]
- Data Access Repository -> Aurora Serverless v2 (PostgreSQL): Encrypted state persistence [TCP/TLS (Prisma, pgcrypto)]
- Case Workflow Controller -> Messaging Backbone: Publishes case resolution events [AWS SDK (SNS/SQS)]
- Case Workflow Controller -> Audit & Event Store Container: Emits signed state-change audit logs [AWS SDK (DynamoDB API)]

## Technology Stack
- Node.js & React: Powers the Case Management backend and analyst SPA for rapid workflow delivery.
- TypeScript & Prisma: Provides type-safe database access and simplifies relational case histories.
- Aurora Serverless v2 (PostgreSQL): Automatically scales compute and drops base costs to fit within the €25,000 monthly budget while supporting pgcrypto for compliance.
- AWS Fargate Spot: Eliminates OS patching overhead to accommodate the three-engineer team constraint.
- AWS KMS & Secrets Manager: Enforces application-layer encryption and dynamic credential rotation to satisfy security mandates.

## Rationale
This architecture balances strict PCI-DSS Level 1 compliance and 7-year auditability with the operational constraints of a three-engineer team and a €25,000 monthly budget. Serverless and auto-scaling components minimize administrative overhead while ensuring high availability and low operational complexity.