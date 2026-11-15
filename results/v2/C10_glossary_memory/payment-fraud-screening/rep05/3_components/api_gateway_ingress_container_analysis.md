## Overview
[The Real-Time Payment Fraud Screening System screens card-not-present payment authorizations for fraud to approve, decline, or flag suspicious transactions. It provides secure case management for fraud analysts while maintaining PCI-DSS Level 1 compliance.]

## Key Elements
- [API Gateway / Ingress Container (Amazon API Gateway)]
- [Fraud Scoring Engine Container (Go or Rust)]
- [Case Management Container (Node.js/Python + React SPA on Amazon S3 / CloudFront)]
- [Model Registry Container (MLflow on Amazon ECS)]
- [Database & Storage (Amazon Aurora Serverless v2)]
- [Caching Layer (Amazon ElastiCache with Redis OSS)]
- [Payment Gateway / Acquirer]
- [Card Networks / Tokenization Vault]
- [Identity Provider (IdP)]

## Relationships
- [Payment Gateway / Acquirer -> API Gateway / Ingress Container: Submits real-time authorization requests (HTTPS / gRPC)]
- [API Gateway / Ingress Container -> Card Networks / Tokenization Vault: Performs token resolution (HTTPS via mTLS)]
- [API Gateway / Ingress Container -> Identity Provider (IdP): Handles authentication (HTTPS via mTLS / OAuth2/SAML)]
- [API Gateway / Ingress Container -> Fraud Scoring Engine Container: Routes requests for fraud evaluation (gRPC over AWS VPC internal networks via mTLS)]
- [Fraud Scoring Engine Container -> Caching Layer: Performs feature lookups (Redis OSS Protocol)]
- [Fraud Scoring Engine Container -> Database & Storage: Reads/writes transactional data (PostgreSQL Wire Protocol)]
- [Case Management Container -> Database & Storage: Manages review cases (PostgreSQL Wire Protocol)]

## Technology Stack
- [AWS API Gateway (HTTP API): Minimizes operational overhead for a three-engineer team while supporting 3,000 TPS.]
- [Amazon Aurora Serverless v2: Provides auto-scaling relational storage for transactional and 7-year audit data within budget.]
- [Amazon ElastiCache with Redis OSS: Delivers low-latency feature lookups to satisfy the sub-50ms P99 latency requirement.]
- [AWS WAF: Enforces perimeter defense and OWASP rules for PCI-DSS Level 1 compliance.]

## Rationale
[This architecture leverages fully managed AWS services to fit the fixed 25,000 EUR monthly budget and operational constraints of a three-engineer team. It guarantees high performance, strict security, and auditable compliance required for real-time payment processing.]