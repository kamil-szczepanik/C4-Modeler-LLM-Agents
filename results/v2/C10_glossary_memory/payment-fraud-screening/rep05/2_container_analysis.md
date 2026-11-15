## Overview
[The system is a real-time payment fraud screening platform deployed on AWS that evaluates card-not-present payment authorizations to approve, decline, or flag suspicious transactions while maintaining PCI-DSS Level 1 compliance.]
[Its core purpose is to deliver sub-50ms fraud decisions at scale, support fraud analysts with secure case management, and ensure tamper-evident 7-year auditability within a fixed budget.]

## Key Elements
* API Gateway / Ingress Container (AWS API Gateway or Envoy)
* Fraud Scoring Engine Container (Go or Rust)
* Case Management Container (Node.js/Python + React SPA on Amazon S3 / CloudFront)
* Model Registry Container (MLflow on Amazon ECS)
* Database & Storage (Amazon Aurora Serverless v2 with append-only tables and immutable triggers)
* Caching Layer (Amazon ElastiCache with Redis OSS)
* External Systems: Payment Gateway / Acquirer, Card Networks / Tokenization Vault, Identity Provider (IdP)
* Personas: Payment Merchants / End Consumers, Fraud Analysts & Risk/Compliance Officers, Risk / Data Scientists

## Relationships
* Payment Gateway / Acquirer -> API Gateway / Ingress Container (HTTPS / gRPC)
* Fraud Analysts & Risk/Compliance Officers -> Case Management Container (HTTPS via TLS 1.3)
* API Gateway / Ingress Container -> Card Networks / Tokenization Vault (HTTPS via mTLS)
* All internal containers -> Identity Provider (IdP) (HTTPS via mTLS / OAuth2/SAML)
* Inter-container communication (API Gateway to Fraud Scoring Engine) -> gRPC over AWS VPC internal networks via mTLS

## Technology Stack
* Cloud Infrastructure: AWS (Region: eu-west-1) managed via Amazon ECS (Fargate) for minimal operational overhead.
* Core Scoring Language: Go or Rust for the Fraud Scoring Engine to guarantee P99 latency below 50ms at 3,000 TPS.
* Persistence & Audit: Amazon Aurora Serverless v2 with append-only tables and immutable cryptographic triggers for R-06 tamper-evident 7-year audit logs.
* Caching: Amazon ElastiCache (Redis OSS) for low-latency feature lookups and rate limiting.
* Model Management: MLflow on Amazon ECS for zero-downtime model and rule updates via S3 memory caching.
* Security & Observability: AWS IAM Roles for Tasks, AWS Certificate Manager (ACM) Private CA for mTLS rotation, and distributed tracing via AWS X-Ray or OpenTelemetry.

## Rationale
[This architecture uses managed AWS services like ECS Fargate and Aurora Serverless v2 to minimize operational overhead for a 3-engineer team while strictly staying under the 25,000 EUR monthly budget.]
[It guarantees high availability, sub-50ms P99 latency, and PCI-DSS Level 1 compliance through in-memory caching, boundary tokenization, and immutable audit logging.]