## Overview
[The system is a real-time payment fraud screening platform that evaluates card-not-present transactions for a mid-size payment processor. Its core purpose is to instantly approve, decline, or flag suspicious payments while enabling fraud analysts to review cases securely and maintain strict PCI-DSS Level 1 compliance.]

## Key Elements
- Real-Time Payment Fraud Screening System [softwareSystem, context]
- Fraud Analysts & Risk/Compliance Officers [person, container]
- Risk / Data Scientists [person, container]
- Payment Gateway / Acquirer [externalSystem, container]
- API Gateway / Ingress Container (AWS API Gateway or Envoy)
- Fraud Scoring Engine Container (Go or Rust)
- Case Management Container (Node.js/Python + React SPA on Amazon S3 / CloudFront)
- Model Registry Container (MLflow on Amazon ECS)
- Database & Storage (Amazon Aurora Serverless v2 fronted by AWS RDS Proxy)
- Caching Layer (Amazon ElastiCache with Redis OSS)

## Relationships
- Payment Gateway / Acquirer -> API Gateway / Ingress Container (HTTPS / gRPC)
- Fraud Analysts & Risk/Compliance Officers -> Case Management Container (HTTPS via TLS 1.3)
- API Gateway / Ingress Container -> Fraud Scoring Engine Container (gRPC over AWS VPC internal networks via mTLS)
- Fraud Scoring Engine Container -> Caching Layer (Redis OSS Protocol)
- Fraud Scoring Engine Container -> Database & Storage (PostgreSQL Wire Protocol over TLS 1.3 via AWS IAM Authentication)
- Case Management Container -> Database & Storage (PostgreSQL Wire Protocol over TLS 1.3 via AWS IAM Authentication)

## Technology Stack
- AWS (eu-west-1): Chosen cloud provider for scalable, secure infrastructure within budget.
- Go or Rust: Selected for the Fraud Scoring Engine Container to guarantee sub-50ms P99 latency at 3,000 TPS.
- Amazon Aurora Serverless v2: Provides auto-scaling relational storage with PostgreSQL compatibility and `pgcrypto` support.
- AWS RDS Proxy: Manages connection pooling for high-throughput concurrency.
- Amazon ElastiCache with Redis OSS: Delivers ultra-low latency feature lookups.
- MLflow on Amazon ECS: Facilitates zero-downtime model and rule updates.

## Rationale
[This architecture fits requirements by combining high-performance languages and caching to achieve sub-50ms latency at 3,000 TPS. Consolidating database infrastructure with Aurora Serverless v2 and RDS Proxy ensures strict 7-year auditability and PCI-DSS Level 1 compliance while remaining maintainable by a three-engineer team within a 25,000 EUR monthly budget.]