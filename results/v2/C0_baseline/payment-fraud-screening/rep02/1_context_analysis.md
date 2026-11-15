## Overview
[Real-Time Payment Fraud Screening System screens card-not-present payment authorizations in AWS eu-west-1 for PCI-DSS Level 1 compliance. It delivers sub-50ms fraud decisions and provides a case management UI for fraud analysts.]

## Key Elements
• Payment Gateway / Acquirer (External System)
• Card Schemes / Tokenization Service (External System)
• Identity Provider (External System)
• Audit / Compliance Archive (External System)
• Real-Time Fraud Screening System (System-in-Scope)
• Fraud Analysts and Risk Operations Managers (Users)

## Relationships
• Payment Gateway -> gRPC/HTTPS -> Real-Time Fraud Screening System (Authorization screening, R-01, R-04)
• Real-Time Fraud Screening System -> HTTPS -> Card Schemes / Tokenization Service (Tokenized card data, R-05)
• Fraud Analysts -> HTTPS/OIDC -> Real-Time Fraud Screening System (Case management & feedback loop, R-02, R-03)
• Real-Time Fraud Screening System -> AWS KMS / S3 Object Lock -> Audit / Compliance Archive (Tamper-evident logs, R-06)

## Technology Stack
• AWS ECS / AWS Lambda: Containerized microservices architecture optimized for cost and agility under a 3-engineer constraint
• AWS SageMaker / Optimized Redis Cache: High-throughput inference runtime meeting <50ms P99 latency at 3,000 TPS (R-04)
• Amazon DynamoDB: Low-latency state management for real-time feature stores and case management
• S3 Object Lock (WORM): Cryptographically secure, tamper-evident 7-year audit retention (R-06)
• AWS KMS: Encryption at rest and cryptographic binding for explainability integrity and secure model loading (R-03, R-05)
• OAuth2 / OIDC via External IdP: Enforces strict Role-Based Access Control (RBAC) and MFA for analysts

## Rationale
[This architecture leverages managed AWS services to minimize operational burden for a three-engineer team while respecting a 25,000 EUR monthly budget. Strict tokenization, circuit breakers, and immutable logging ensure PCI-DSS compliance, explainability, and high availability.]