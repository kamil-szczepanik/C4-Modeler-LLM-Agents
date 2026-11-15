## Overview
The Real-Time Payment Fraud Screening system screens card-not-present payment authorizations for a mid-size payment processor in AWS (eu-west-1) to approve, decline, or review transactions. It ensures strict compliance (PCI-DSS Level 1, 7-year tamper-evident auditability, <50ms P99 latency at 3,000 TPS) within a 25,000 EUR monthly budget operated by three engineers.

## Key Elements
- **Users**: Fraud Analyst, Risk Operations Manager, End Customer (Payer), Merchant
- **Containers**: API Gateway / Ingress Router (Amazon API Gateway / ALB), Scoring Engine (ECS Fargate), Case Management API (ECS Fargate), Fraud Analyst SPA (Amazon S3 / CloudFront), Rule & Model Distribution Service (ECS Fargate), Audit & Persistence Store (Amazon Aurora PostgreSQL), Feature Store (Amazon ElastiCache Redis), Asynchronous Event Bus (Amazon EventBridge)
- **Rule & Model Distribution Service Components**: Admin API Controller (Spring MVC), Bundle Signer & Validator (AWS KMS / Ed25519), Storage Sync Agent (AWS SDK for Java), Rule Syntax Linter (JSON Schema Validator / ANTLR)

## Relationships
- Fraud Analyst SPA -> API Gateway / Ingress Router (HTTPS)
- Admin API Controller -> Rule Syntax Linter (In-process method call)
- Admin API Controller -> Bundle Signer & Validator (In-process call utilizing AWS KMS via HTTPS/AWS SDK)
- Storage Sync Agent -> Amazon S3 (HTTPS / AWS SDK) for rule bundle distribution
- Storage Sync Agent -> Amazon EventBridge (HTTPS / AWS SDK) for audit events
- Scoring Engine -> Amazon S3 (HTTPS) for polling signed rule bundles

## Technology Stack
- **Compute**: AWS ECS Fargate (cost-effective container management for a 3-person team)
- **Database & State**: Amazon Aurora PostgreSQL (tamper-evident audit store for 7-year retention), Amazon ElastiCache Redis (low-latency feature store)
- **Security & Cryptography**: AWS KMS with Ed25519 (cryptographic bundle signing without secret exfiltration)
- **Integration & Messaging**: Amazon EventBridge (asynchronous event distribution and decoupled audit notifications)
- **Validation**: JSON Schema Validator / ANTLR (static rule syntax linter protecting against DoS/injection)

## Rationale
This architecture uses serverless and managed AWS services (ECS Fargate, S3, EventBridge, KMS) to minimize operational overhead for a three-engineer team while easily scaling to meet 3,000 TPS at sub-50ms latency. Strict component isolation, KMS-backed cryptographic signing, and Aurora PostgreSQL satisfy PCI-DSS Level 1 and 7-year audit requirements within the 25,000 EUR monthly budget.