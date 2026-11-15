## Overview
The Real-Time Payment Fraud Screening System evaluates card-not-present payment authorizations to approve, decline, or flag suspicious transactions while maintaining PCI-DSS Level 1 compliance. It delivers sub-50ms fraud decisions at scale while providing secure case management for fraud analysts.

## Key Elements
- Payment Merchants / End Consumers [person, context]
- Fraud Analysts & Risk/Compliance Officers [person, context]
- Risk / Data Scientists [person, context]
- Payment Gateway / Acquirer [externalSystem, context]
- Card Networks / Tokenization Vault [externalSystem, context]
- Identity Provider (IdP) [externalSystem, context]
- API Gateway / Ingress Container (AWS API Gateway or Envoy) [container]
- Fraud Scoring Engine Container (Go or Rust) [container]
- Case Management Container (Node.js/Python + React SPA on Amazon S3 / CloudFront) [container]
- Model Registry Container (MLflow on Amazon ECS) [container]
- Database & Storage (Amazon Aurora Serverless v2) [container]
- Caching Layer (Amazon ElastiCache with Redis OSS) [container]
  - Feature Store Cache Component [component]
  - Rate Limiter Component [component]

## Relationships
- Payment Gateway / Acquirer -> API Gateway / Ingress Container [HTTPS / gRPC]
- API Gateway / Ingress Container -> Fraud Scoring Engine Container [gRPC over AWS VPC internal networks via mTLS]
- Fraud Scoring Engine Container -> Feature Store Cache Component [Redis Protocol]
- Fraud Scoring Engine Container -> Rate Limiter Component [Redis Protocol]
- Fraud Scoring Engine Container -> Database & Storage [PostgreSQL Wire Protocol]
- Case Management Container -> Database & Storage [PostgreSQL Wire Protocol]
- Model Registry Container -> Fraud Scoring Engine Container [S3 memory caching]
- Fraud Analysts & Risk/Compliance Officers -> Case Management Container [HTTPS via TLS 1.3]

## Technology Stack
- AWS [target_cloud]: Core infrastructure provider hosted in eu-west-1 region.
- Go or Rust [programming_language]: Powers the Fraud Scoring Engine Container for sub-50ms P99 latency.
- Amazon Aurora Serverless v2 [database]: Provides transactional and audit data storage with append-only tables.
- Amazon ElastiCache with Redis OSS [database/cache]: Delivers low-latency feature lookups and sliding window rate limiting.
- MLflow on Amazon ECS [ml_platform]: Manages zero-downtime model and rule updates in the Model Registry Container.
- Node.js/Python & React on Amazon S3 / CloudFront [framework/hosting]: Powers the Case Management Container.

## Rationale
This architecture uses Go/Rust and Amazon ElastiCache Redis OSS to consistently achieve sub-50ms decision latency under high throughput. It satisfies strict compliance, security, and auditability requirements via AWS KMS encryption, tokenized card data handling, and immutable audit logs within a fixed 25,000 EUR monthly budget managed by a three-engineer team.