## Overview
The Real-Time Payment Fraud Screening System screens card-not-present payment authorizations in real time to prevent financial fraud while maintaining PCI-DSS Level 1 compliance. It evaluates transactions under 50 milliseconds and provides case management tools for fraud analysts.

## Key Elements
- Real-Time Payment Fraud Screening System [softwareSystem, context]
- Payment Merchants / End Consumers [person, context]
- Fraud Analysts & Risk/Compliance Officers [person, context]
- Risk / Data Scientists [person, context]
- Payment Gateway / Acquirer [externalSystem, context]
- Card Networks / Tokenization Vault [externalSystem, context]
- Identity Provider (IdP) [externalSystem, context]
- API Gateway / Ingress Container (AWS API Gateway or Envoy)
- Fraud Scoring Engine Container (Go or Rust)
- Case Management Container (Node.js/Python + React SPA on Amazon S3 / CloudFront)
- Model Registry Container (MLflow on Amazon ECS)
- Database & Storage (Amazon Aurora Serverless v2)
- Caching Layer (Amazon ElastiCache with Redis OSS)

## Relationships
- Payment Gateway / Acquirer -> API Gateway / Ingress Container (HTTPS / gRPC)
- Fraud Analysts & Risk/Compliance Officers -> Case Management Container (HTTPS via TLS 1.3)
- API Gateway / Ingress Container -> Card Networks / Tokenization Vault (HTTPS via mTLS)
- API Gateway / Ingress Container -> Identity Provider (IdP) (HTTPS via mTLS / OAuth2/SAML)
- API Gateway / Ingress Container -> Fraud Scoring Engine Container (gRPC over AWS VPC internal networks via mTLS)
- Fraud Scoring Engine Container -> Caching Layer (Redis OSS Protocol)
- Fraud Scoring Engine Container -> Database & Storage (PostgreSQL Wire Protocol)
- Case Management Container -> Database & Storage (PostgreSQL Wire Protocol)
- Model Registry Container -> Fraud Scoring Engine Container (S3 memory caching)
- Risk / Data Scientists -> Model Registry Container (HTTPS / AWS IAM)

## Technology Stack
- AWS (eu-west-1): Chosen as the target cloud provider to meet infrastructure constraints and latency requirements.
- Go or Rust: Selected for the Fraud Scoring Engine Container to achieve sub-50ms P99 latency at 3,000 requests per second.
- MLflow on Amazon ECS: Implemented for the Model Registry Container to manage zero-downtime model and rule updates.
- Amazon Aurora Serverless v2: Utilized for Database & Storage to persist transactional and audit data with append-only tables.
- Amazon ElastiCache with Redis OSS: Deployed as the Caching Layer for low-latency feature lookups and rate limiting.

## Rationale
This serverless-first, containerized architecture fits the requirements by maintaining high availability and sub-50ms performance under peak loads while strictly enforcing PCI-DSS compliance. It ensures robust 7-year auditability and secure cryptographic integrity within a 3-engineer operational model and a 25,000 EUR monthly budget.