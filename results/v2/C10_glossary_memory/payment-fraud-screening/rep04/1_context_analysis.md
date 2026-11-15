## Overview
[The system is a real-time payment fraud screening platform that evaluates card-not-present transactions for a mid-size payment processor and provides case management for fraud analysts. Its core purpose is to screen authorizations, block fraudulent transactions, and maintain immutable audit logs while complying with PCI-DSS Level 1.]

## Key Elements
- [Payment Processor / Merchant Systems]
- [Fraud Analyst]
- [Risk Operations Manager / Data Scientist]
- [Payment Gateway / Processor Core]
- [Identity Provider (IdP)]
- [API Gateway / Ingress (AWS API Gateway / ALB)]
- [Scoring Engine (AWS ECS Fargate)]
- [Case Management Backend (AWS Lambda / DynamoDB)]
- [Audit & Compliance Store (Amazon S3 Object Lock / Amazon QLDB)]
- [Rule & Model Registry (S3 / DynamoDB)]

## Relationships
- [Customer Systems to API Gateway via REST / gRPC]
- [Fraud Analyst to Case Management via HTTPS / OIDC]
- [Payment Gateway to Scoring Engine via gRPC / mTLS]
- [Scoring Engine to Audit Store via AWS SDK / KMS]
- [Case Management to DynamoDB via AWS PrivateLink]

## Technology Stack
- [AWS Cloud Infrastructure: Chosen for managed services within the 25k EUR monthly budget and EU-West-1 regional residency]
- [AWS ECS Fargate: Selected for Scoring Engine to eliminate Lambda cold starts and guarantee sub-50ms P99 latency]
- [Amazon DynamoDB: Used for case management and rule metadata due to sub-millisecond retrieval performance]
- [Amazon S3 Object Lock & Amazon QLDB: Deployed for tamper-evident, 7-year audit logging to meet compliance mandates]
- [AWS KMS: Used for data-at-rest encryption with customer-managed keys for card data protection]

## Rationale
[This architecture satisfies strict PCI-DSS Level 1 and 7-year auditability requirements while maintaining a sub-50ms P99 latency at 3,000 TPS. Furthermore, the serverless and managed container design fits the operational constraints of a three-engineer team within a 25,000 EUR monthly budget.]